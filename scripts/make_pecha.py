#!/usr/bin/env python3
"""Lay out a Lotsawa House page as a pecha PDF with the layout engine, in headless Chromium.

The skill pecha is a conductor: the page is read by its layer markup inside the same assembled file that
the skill runs, so the same page with the same options always gives the same PDF.
No AI reads the page on this path.

    python3 make_pecha.py https://www.lotsawahouse.org/... --out OUT [options]
    python3 make_pecha.py saved-page.html --out OUT [options]

Exit codes: 0 PDF written; 2 the formatter refused the page (message on stderr, report written);
3 the page could not be fetched (save it from the browser and pass the file); 4 not a Lotsawa House address
(convert the source to the intermediate format and use --text); 5 the intermediate text changed since the
check sheet, or it lacks what the PDF needs; 1 the file is missing or unreadable, a wrong option, or Playwright
is missing.

    python3 make_pecha.py --text converted.pecha.txt --check --out OUT       # the check sheet, no PDF
    python3 make_pecha.py --text converted.pecha.txt --confirmed FINGERPRINT --out OUT [options]
"""
import argparse, contextlib, datetime, hashlib, json, pathlib, re, sys, urllib.parse, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
FORMATTER = HERE.parent / "assets" / "pecha-engine.html"
SKILL_VERSION = "2026.10.18a"   # printed on the credits page; the same as the README badge and the last CHANGELOG release
SITE_HOSTS = ("lotsawahouse.org", "www.lotsawahouse.org")
USER_AGENT = "pecha-skill/1.0 (one page per request; personal practice material)"


class NotLotsawaHouse(ValueError):
    """The address is not a page of the Lotsawa House site."""


class Laid:
    """One run of the formatter: the PDF (None after a refusal), the engine's report and the refusal, if any."""
    def __init__(self, pdf, report):
        self.pdf, self.report = pdf, report
        self.refusal = report.get("refusal") or None


ABBREV_MAX = 24                                # as in the formatter's form
MAX_PAGE_BYTES = 8_000_000                     # the longest Lotsawa House pages are well under 2 MB


class _SameSiteRedirects(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an allowed host (the site moves pages between its own addresses)."""
    def __init__(self, allowed):
        self.allowed = allowed

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not allowed_address(newurl, self.allowed):
            raise NotLotsawaHouse(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def allowed_address(url, allowed=SITE_HOSTS):
    parts = urllib.parse.urlsplit(url)
    return parts.scheme in ("http", "https") and parts.hostname in allowed


def as_address(source):
    """An address typed without its scheme ("www.lotsawahouse.org/...") is still an address."""
    if re.match(r"^(www\.)?lotsawahouse\.org(/|$)", source):
        return "https://" + source
    return source


def fetch(url, allowed=SITE_HOSTS, timeout=30):
    """The page's HTML, downloaded once. Only Lotsawa House addresses are fetched, redirects included."""
    if not allowed_address(url, allowed):
        raise NotLotsawaHouse(url)
    opener = urllib.request.build_opener(_SameSiteRedirects(allowed))
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with opener.open(request, timeout=timeout) as response:
        body = response.read(MAX_PAGE_BYTES + 1)
        if len(body) > MAX_PAGE_BYTES:
            raise ValueError(f"the page is larger than {MAX_PAGE_BYTES} bytes")
        return body.decode(response.headers.get_content_charset() or "utf-8")


@contextlib.contextmanager
def _formatter(items, formatter=FORMATTER, on_request=None, timeout_ms=180_000):
    """A headless tab with the assembled file laid out from the sessionStorage `items`, with no network."""
    from playwright.sync_api import sync_playwright
    init = "".join(f"sessionStorage.setItem({json.dumps(k)}, {json.dumps(v)});" for k, v in items)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        try:
            tab = browser.new_page()
            tab.add_init_script(init)

            def local_only(route):                       # the engine needs no network: nothing else may load
                if on_request:
                    on_request(route.request.url)
                if route.request.url.startswith(("file://", "data:")):
                    route.continue_()
                else:
                    route.abort()
            tab.route("**/*", local_only)
            tab.goto(pathlib.Path(formatter).resolve().as_uri())
            tab.wait_for_function("document.body.dataset.ready === '1'", timeout=timeout_ms)
            yield tab
        finally:
            browser.close()


def lay_out(page_html, opts, now=None, formatter=FORMATTER, on_request=None, timeout_ms=180_000, text=None):
    """Open the assembled file with the page (or, through the internal input, the intermediate text) and the
    options, as its own form does, and print it to PDF."""
    items = [("pecha-opts", json.dumps(opts))]
    items.append(("pecha-src", text) if text is not None else ("pecha-page", page_html))
    if now:
        items.append(("pecha-now", now))
    with _formatter(items, formatter, on_request, timeout_ms) as tab:
        report = tab.evaluate("window.__report")
        pdf = None if report.get("refusal") else tab.pdf(prefer_css_page_size=True, print_background=True)
    return Laid(pdf, report)


def interpret(text, formatter=FORMATTER):
    """What the formatter's reader understands from the intermediate text: {meta, blocks}. Same code as the PDF."""
    with _formatter([], formatter) as tab:
        return tab.evaluate("t => parse(t)", text)


def fingerprint(text):
    """Short fingerprint of the exact text shown in the check sheet; the PDF is made only from that text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


LABELS = {
    "en": {"title": "Check sheet", "fp": "Fingerprint", "credits": "Credits", "text": "Text", "check": "Points to check",
           "none": "Nothing to point out.", "tibetan_title": "Tibetan title", "latin_title": "Title", "author": "Author",
           "translator": "Translator", "version": "Version", "site": "Taken from", "url": "Address",
           "licence": "Licence", "source_ref": "Tibetan source", "missing": "(not stated)",
           "types": {"verse": "verse", "mantra": "mantra", "prose": "prose", "note": "note or colophon",
                     "incipit": "incipit (cover)", "section": "section heading", "rubric": "instruction"},
           "bo": "Tibetan", "phon": "transliteration", "trans": "translation",
           "no_site": "The text does not say where it was taken from (Site: line). The PDF is not made without it.",
           "no_phon": "block {n}: verse without transliteration", "no_trans": "block {n}: verse without translation",
           "empty": "No Tibetan block was found.",
           "dropped": "This line is not printed anywhere; fix its place in the text: {line}",
           "no_trans_note": "block {n}: note without translation"},
    "pt": {"title": "Conferência", "fp": "Impressão digital", "credits": "Créditos", "text": "Texto",
           "check": "Pontos a conferir", "none": "Nada a apontar.", "tibetan_title": "Título tibetano",
           "latin_title": "Título", "author": "Autor", "translator": "Tradutor", "version": "Versão",
           "site": "Fonte", "url": "Endereço", "licence": "Licença", "source_ref": "Fonte tibetana",
           "missing": "(não informado)",
           "types": {"verse": "verso", "mantra": "mantra", "prose": "prosa", "note": "nota ou colofão",
                     "incipit": "incipit (capa)", "section": "título de seção", "rubric": "instrução"},
           "bo": "tibetano", "phon": "transliteração", "trans": "tradução",
           "no_site": "O texto não diz de onde foi tirado (linha Site:). O PDF não é feito sem ela.",
           "no_phon": "bloco {n}: verso sem transliteração", "no_trans": "bloco {n}: verso sem tradução",
           "empty": "Nenhum bloco tibetano foi encontrado.",
           "dropped": "Esta linha não é impressa em lugar nenhum; corrija o lugar dela no texto: {line}",
           "no_trans_note": "bloco {n}: nota sem tradução"},
}


def labels_lang(args):
    """Language of the check sheet's labels: --labels, else the credits language asked for, else English."""
    for lang in (args.labels, args.lang):
        if lang in LABELS:
            return lang
    return "en"


def problems_of(parsed, layers, lang):
    """(blocking, notes): what stops the PDF and what the person should look at."""
    L, meta, blocks = LABELS[lang], parsed["meta"], parsed["blocks"]
    blocking = [] if meta.get("site") else [L["no_site"]]
    blocking += [L["dropped"].format(line=x) for x in meta.get("dropped", [])]
    if not any(b.get("bo") for b in blocks):
        blocking.append(L["empty"])
    notes = []
    for n, b in enumerate(blocks, 1):
        if b["type"] == "verse":
            if "phon" in layers and not b.get("phon"):
                notes.append(L["no_phon"].format(n=n))
            if "trans" in layers and not b.get("trans"):
                notes.append(L["no_trans"].format(n=n))
        elif b["type"] == "note" and "trans" in layers and not b.get("trans"):
            notes.append(L["no_trans_note"].format(n=n))
    return blocking, notes


def shown_as_printed(t):
    """The field as the PDF prints it: the reader escapes the Tibetan for HTML, so the entities are undone here and
    nothing else is changed (a tag typed in the text is printed as typed, so it is shown as typed)."""
    return (t or "").replace("\u00a0", " ").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&")


def check_sheet_markdown(parsed, fp, layers, lang):
    """The check sheet: every block with the role the reader gave it, the credits, and what to check."""
    L, meta = LABELS[lang], parsed["meta"]
    plain = shown_as_printed
    out = [f"# {L['title']}: {plain(meta.get('title') or meta.get('title_bo') or '')}".rstrip(": "),
           "", f"{L['fp']}: `{fp}`", "", f"## {L['credits']}", ""]
    for key in ("tibetan_title", "latin_title", "author", "translator", "version", "site", "url", "licence", "source_ref"):
        field = {"tibetan_title": "title_bo", "latin_title": "title"}.get(key, key)
        out.append(f"- {L[key]}: {plain(meta.get(field)) or L['missing']}")
    out += ["", f"## {L['text']}", ""]
    for n, b in enumerate(parsed["blocks"], 1):
        kind = L["types"].get(b["type"], b["type"])
        if b["type"] in ("section", "rubric"):
            out.append(f"{n}. **[{kind}]** {plain(b.get('title') or b.get('text'))}")
            continue
        out.append(f"{n}. **[{kind}]**")
        out.append(f"   - {L['bo']}: {plain(b.get('bo'))}")
        if b.get("phon"):
            out.append(f"   - {L['phon']}: {plain(b['phon'])}")
        trans = b.get("trans") or b.get("extra")
        if isinstance(trans, list):
            trans = " ".join(trans)
        if trans:
            out.append(f"   - {L['trans']}: {plain(trans)}")
    blocking, notes = problems_of(parsed, layers, lang)
    out += ["", f"## {L['check']}", ""] + [f"- **{x}**" for x in blocking] + [f"- {x}" for x in notes]
    if not blocking and not notes:
        out.append(L["none"])
    return "\n".join(out) + "\n"


def slug_of(source):
    name = urllib.parse.urlsplit(source).path if "://" in source else pathlib.Path(source).stem
    name = re.sub(r"\.(html?|pecha|txt)$", "", name.rstrip("/").split("/")[-1] or "pecha")
    name = re.sub(r"\.pecha$", "", name)
    return re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-") or "pecha"


def free_name(out, slug, stamp):
    """A file stem in `out` that no earlier run used: nothing is ever overwritten."""
    stem, n = f"{slug}-{stamp}", 2
    while any(out.glob(stem + ".*")):
        stem, n = f"{slug}-{stamp}-{n}", n + 1
    return out / stem


class _Arguments(argparse.ArgumentParser):
    def error(self, message):                    # exit 2 means a refused page; a wrong option is exit 1
        self.print_usage(sys.stderr)
        self.exit(1, f"{self.prog}: error: {message}\n")


def parse_args(argv):
    a = _Arguments(description=__doc__.split("\n\n")[0])
    a.add_argument("source", nargs="?", help="Lotsawa House address, or a page saved from the browser")
    a.add_argument("--text", help="intermediate format written by the AI conversion (other sources)")
    a.add_argument("--check", action="store_true", help="with --text: write the check sheet, make no PDF")
    a.add_argument("--labels", choices=("en", "pt"), help="with --check: language of the check sheet's labels")
    a.add_argument("--confirmed", help="with --text: fingerprint of the text the person confirmed in the check sheet")
    a.add_argument("--from", dest="origin", default="", help="with --text: where the text came from, for the report")
    a.add_argument("--out", default=".", help="folder for the PDF and the report")
    a.add_argument("--layers", default="bo+phon+trans", help="bo, phon and trans joined by +")
    a.add_argument("--mode", choices=("single", "double"), default="single")
    a.add_argument("--lines", choices=("thin", "thick-out", "thick-in"), default="thin",
                   help="frame lines: two thin (default), the outer one thick, or the inner one thick")
    a.add_argument("--abbrev", default="", help="title abbreviation in the margin; empty uses the title")
    a.add_argument("--lang", choices=("auto", "en", "pt"), default="auto",
                   help="language of the credits page; auto (default) follows the language of the translation")
    a.add_argument("--inserts", choices=("show", "sides", "hide"), default="show",
                   help="the translator's own headings (Heading3 Insert): printed in the flow (show), printed with "
                        "each one opening a new side (sides), or left out (hide)")
    a.add_argument("--cover-title", choices=("show", "hide"), default="show",
                   help="the translator's title of the whole text (a Heading3 Insert before the text, when the page "
                        "gives no title): on the cover (show) or left out (hide)")
    a.add_argument("--notes", choices=("hide", "end"), default="hide",
                   help="the translator's notes: left out (hide, default), or printed with their numbers in the text "
                        "and the notes before the credits (end); without the translation layer they are left out")
    a.add_argument("--blocks", choices=("together", "split"), default="together",
                   help="together: every layer in each pecha; split: the whole text in Tibetan first, then the "
                        "transliteration and translation, from a new pecha, with one cover")
    a.add_argument("--terma", choices=("auto", "on", "off"), default="auto",
                   help="add the terma mark to the transliteration and translation of verses whose Tibetan ends with it; "
                        "auto (default) when most Tibetan verses end with it")
    a.add_argument("--now", help="local date and time printed on the credits page, ISO 8601 with offset "
                                 "(2026-10-08T19:53-03:00); default: this machine's clock")
    a.add_argument("--timeout", type=float, default=30, help="seconds to wait for the page download")
    args = a.parse_args(argv)
    if not args.now:                             # the credits page prints the date and time of the run
        args.now = datetime.datetime.now().astimezone().isoformat(timespec="minutes")
    if len(args.abbrev) > ABBREV_MAX:
        a.error(f"--abbrev takes at most {ABBREV_MAX} characters (the margin box holds no more)")
    if bool(args.source) == bool(args.text):
        a.error("give either a Lotsawa House address or page, or --text with an intermediate format file")
    if args.text and not args.check and not args.confirmed:
        a.error("--text needs --check first, then --confirmed with the fingerprint the check sheet shows")
    layers = set(args.layers.split("+"))
    if not layers or layers - {"bo", "phon", "trans"}:
        a.error("--layers takes bo, phon and trans joined by +")
    return args, layers


def read_source(source, timeout):
    """(page HTML, None) or (None, (exit code, message))."""
    if "://" in source:
        try:
            return fetch(source, timeout=timeout), None
        except NotLotsawaHouse as e:
            return None, (4, f"Not a Lotsawa House address: {e}. Convert the source to the intermediate format "
                             "and use --text, with the check sheet.")
        except Exception as e:                       # no network here, or the site answered with an error
            return None, (3, f"Could not fetch {source} ({e}). Save the page from the browser (complete page or "
                             "HTML only) and pass the saved file instead.")
    path = pathlib.Path(source)
    if not path.is_file():
        return None, (1, f"No such file: {source}")
    try:
        return path.read_text("utf-8"), None
    except UnicodeDecodeError:
        return None, (1, f"{source} is not UTF-8 text. Save the page again from the browser as HTML.")


def stamp_of(now):
    return (now or datetime.datetime.now().astimezone().isoformat())[:16].replace(":", "").replace("T", "-")


def from_text(args, layers, opts):
    """The other sources: the check sheet first, then the PDF from exactly the text the person confirmed."""
    path = pathlib.Path(args.text)
    if not path.is_file():
        print(f"No such file: {args.text}", file=sys.stderr)
        return 1
    text = path.read_text("utf-8")
    fp = fingerprint(text)
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)
    try:
        parsed = interpret(text)
    except ImportError:
        print("Playwright is not installed: pip install playwright, then python3 -m playwright install chromium.",
              file=sys.stderr)
        return 1
    blocking, notes = problems_of(parsed, layers, labels_lang(args))
    if args.check:
        stem = free_name(out, slug_of(args.text) + "-check-sheet", stamp_of(args.now))
        shown = stem.with_suffix(".md")
        shown.write_text(check_sheet_markdown(parsed, fp, layers, labels_lang(args)), "utf-8")
        print(json.dumps({"check_sheet": str(shown), "fingerprint": fp, "blocks": len(parsed["blocks"]),
                          "blocking": blocking, "notes": notes}, ensure_ascii=False))
        return 0
    if args.confirmed != fp:
        print(f"The text changed since the check sheet (fingerprint {fp}, confirmed {args.confirmed}). "
              "Run --check again and show the new check sheet before making the PDF.", file=sys.stderr)
        return 5
    if blocking:
        print(" ".join(blocking), file=sys.stderr)
        return 5
    laid = lay_out(None, dict(opts, ai=1), now=args.now, text=text)
    stem = free_name(out, slug_of(args.text), stamp_of(args.now))
    report = dict(laid.report, skill={"reader": "intermediate", "ai": True, "source": args.origin,
                                      "text": str(path), "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                                      "confirmed": fp, "version": SKILL_VERSION})
    return finish(laid, report, stem)


def finish(laid, report, stem):
    stem.with_suffix(".json").write_text(json.dumps(report, ensure_ascii=False, indent=1), "utf-8")
    if laid.refusal:
        print(laid.refusal["message"], file=sys.stderr)
        return 2
    stem.with_suffix(".pdf").write_bytes(laid.pdf)
    fits = all(s.get("fits", True) for s in laid.report.get("sides", []))
    print(json.dumps({"pdf": str(stem.with_suffix(".pdf")), "report": str(stem.with_suffix(".json")),
                      "sheets": laid.report.get("sheets"), "all_sides_fit": fits}))
    return 0


def main(argv=None):
    args, layers = parse_args(argv)
    opts = {"bo": int("bo" in layers), "phon": int("phon" in layers), "trans": int("trans" in layers),
            "mode": args.mode, "lines": args.lines, "abbrev": args.abbrev, "lang": args.lang,
            "inserts": args.inserts, "coverTitle": args.cover_title, "notes": args.notes, "terma": args.terma, "blocks": args.blocks, "version": SKILL_VERSION}
    if args.text:
        return from_text(args, layers, opts)
    source = as_address(args.source)
    page, failure = read_source(source, args.timeout)
    if failure:
        print(failure[1], file=sys.stderr)
        return failure[0]
    try:
        laid = lay_out(page, opts, now=args.now)
    except ImportError:
        print("Playwright is not installed: pip install playwright, then python3 -m playwright install chromium.",
              file=sys.stderr)
        return 1
    out = pathlib.Path(args.out); out.mkdir(parents=True, exist_ok=True)
    stem = free_name(out, slug_of(source), stamp_of(args.now))
    report = dict(laid.report, skill={"reader": "markup", "ai": False, "source": source,
                                      "page_sha256": hashlib.sha256(page.encode("utf-8")).hexdigest(),
                                      "version": SKILL_VERSION})
    return finish(laid, report, stem)


if __name__ == "__main__":
    sys.exit(main())
