---
name: pecha
description: Lay out a Tibetan liturgical text as a printable pecha PDF (two 297 x 105 mm folios per A4 landscape sheet, double frame, Tibetan page numbers, cover and credits). Use when the person asks for a pecha, a Tibetan practice text to print, or a PDF with Tibetan, transliteration and translation, from a Lotsawa House address or saved page, another site, their own translation, or numbered paragraphs.
---

# Pecha

The pecha is laid out by the layout engine (`assets/pecha-engine.html`), a single HTML file that only this skill
runs: `scripts/make_pecha.py` opens it in headless Chromium and saves the PDF it prints. The file is not given to
people to open on their own; the PDF always comes from the skill, which settles what the page leaves
open and makes the adjustments the person asks for after looking at the PDF. There are two paths, chosen by the
source:

- **Lotsawa House page** (address or saved page): read by the site's own layer markup, with no AI reading of the
  text. The same page with the same options always gives the same PDF.
- **Any other source** (another site, a translation the person gives, numbered paragraphs): you convert it to the
  intermediate format, the person checks it in the check sheet, and only the confirmed text becomes the PDF. Its
  credits page says it was prepared with the help of AI and must be reviewed before study and practice.

## Choices

Do not ask about these choices before the first PDF. Run with the defaults below, or with what the request already
says, and send the PDF with a short list of the choices used, each with its alternatives, saying that the person only
has to ask for something different to have it made again (step 3 shows the list). Before running, ask only for what
only the person can give: the text, or a saved page when the site cannot be reached.

- **Layers**: Tibetan, transliteration and translation (`--layers bo+phon+trans`). Any combination of `bo`, `phon`, `trans`.
  The Tibetan is set in 19 pt with other layers and in 21 pt when it is the only layer (`--layers bo`); do not ask
  about the size.
- **Blocks**: when the layers include the Tibetan and at least one other layer, every layer together in each pecha
  (`--blocks together`, default), or two blocks (`--blocks split`): the whole text in Tibetan first, then, from a
  new pecha, with no heading, the transliteration and translation, with one cover, one numbering and the credits
  at the end. In two blocks the Tibetan keeps the 21 pt of a Tibetan-only text and nothing is set down. Listed only
  when the layers include the Tibetan and another layer; step 3 says when to recommend two blocks.
- **Printing**: front only (`--mode single`), or double-sided (`--mode double`, long-edge flip).
- **Frame lines**: two thin lines (`--lines thin`, default), the outer line thick (`--lines thick-out`), or the inner
  line thick (`--lines thick-in`). The text breaks at the same points in the three frames.
- **Translator's headings** (titles the translator inserted, with no Tibetan, such as the names of the Guru's
  manifestations): printed in the flow, travelling with the stanza each one opens (`--inserts show`, default);
  printed with each one opening a new pecha (`--inserts sides`), for headings that open long parts of the text; or
  left out (`--inserts hide`). Listed only when the page has them: the report's `run.inserts_found` counts them and
  `run.inserts_names` gives the first ones (see step 3). Printed headings add space after them, so a text with many headings and full pechas takes more sheets than
  with `--inserts hide`.
- **Cover title**: when the page gives no title of its own and the translator added one before the text (a heading
  marked as the translator's, before the first verse), that title is the title of the text: it goes to the cover and
  to the PDF's title (`--cover-title show`, default), or is left out of the cover (`--cover-title hide`). It is never
  one of the translator's headings. Listed only when `run.cover_title.from` is `insert`.
- **Translator's notes**: left out (`--notes hide`, default), or printed (`--notes end`): each note's number where the
  page puts it, in the translation, the explanations and on the cover, and the notes, numbered as on the page, above
  the credits, or on pechas of their own before the credits when they do not fit there. Listed only when
  `run.notes.found` is above zero. The notes go with the translation: with `--notes end` and no translation layer,
  they are left out, numbers and all, and `run.notes.left_out` is `no_translation`.
- **Terma mark**: do not ask. `--terma auto` (default) adds ༔ to the transliteration and translation of each verse
  whose Tibetan ends with it, when most Tibetan verses do (a treasure text). Use `--terma on` or `--terma off` only
  when the person asks; the report's `terma` says what was detected and applied.
- **Margin title**: do not ask. The margin carries the name of the text, which you choose (see step 3).
  The engine's default is the Tibetan title without its opening marks, cut between syllables at 23 characters and
  closed with a shad; when that is not the name of the text, pass the right one with `--abbrev` (at most 24
  characters, the shad included).
- **Date and time on the credits page**: do not ask. Pass `--now` with the person's local date and time, ISO 8601
  with the offset (`--now 2026-10-08T19:53-03:00`), whenever you know their time zone; without it the machine's
  clock is used, and it is often in UTC. The credits print the date and time, then the dedication on its own line.
- **Credits language**: do not ask. It follows the language of the translation layer: leave `--lang` out (`auto`).
  Use `--lang en` or `--lang pt` only when the person asks for that language. The language of the conversation
  never decides it: a Portuguese conversation about an English page gives English credits.

## Steps For A Lotsawa House Page

1. Check the dependencies once: `python3 -c "import playwright"`. If it is missing:
   `pip install playwright --break-system-packages` and `python3 -m playwright install chromium`
   (skip the second command when a Chromium is already installed for Playwright).
2. Run, from this skill's folder:

   ```
   python3 scripts/make_pecha.py "<address or saved page>" --out <output folder> --layers bo+phon+trans \
     --mode single --lines thin
   ```

3. Read the exit code and act on it:
   - **0**: the last line printed is JSON with `pdf`, `report`, `sheets` and `all_sides_fit`. Send the PDF. In
     the message, call each folio a pecha, never a side, in any language (each entry of the report's `sides` is a
     pecha). Name the text by `run.title`, as it is, the title the PDF shows in its tab, and never translate it. If
     `all_sides_fit` is false, say which pechas do not fit (from the report's `sides`) instead of presenting the
     PDF as finished. If the report's `pairing.alerts` lists any pair, tell the person which pairs of verses cross a
     stanza mark of the source (a gap or a heading), quoting both verses, and do not present the PDF as finished.
     `pairing.odd_stanzas` is only information: stanzas with an odd number of verses are normal.
     Answer questions about the titles from the report (`run.title`, `run.title_bo`, `run.cover_title`), never from the address of the page.
     Check the margin before sending the PDF: `run.opts.abbrev` is the name the engine took from the title, and
     `run.title_bo` is the whole Tibetan title. When the abbreviation is not the name of this text (it names the
     cycle or collection the text belongs to, stops in the middle of the name, or keeps a heading word), take the
     text's own name from the title, the one it is known by (for a title ending in `…གསོལ་འདེབས་བསམ་པ་ལྷུན་གྲུབ་བཞུགས་སོ`
     the name is `བསམ་པ་ལྷུན་གྲུབ་མ།`), close it with a shad and run again with `--abbrev`. Say in one line which
     name went to the margin, so the person can ask for another.
     When `run.abbrev_cut` is true, the engine cut the title to fit the margin, often in the middle of a word: never
     send the margin as it was cut; take the text's own name from `run.title_bo`, run again with `--abbrev` and
     say which name went to the margin.
     Send the PDF with the list of the choices used (see Choices), in the language of the conversation, with the
     alternatives of each, for example:

     ```
     Made with:
     - Layers: Tibetan, transliteration and translation (or Tibetan only, or any two)
     - Blocks: together in each pecha (or two blocks: the Tibetan first, then the transliteration and translation)
     - Printing: front only (or double-sided)
     - Frame: two thin lines (or the thick line outside, or inside)
     - Translator's headings: in the flow (or each opening a new pecha, or left out)
     - Cover title: the translator's title (or left out)
     - Translator's notes: left out (or before the credits, with their numbers in the text)
     Anything different? Just ask and I will make it again.
     ```

     Leave out the Blocks line when the layers do not include the Tibetan and another layer, and the Translator's
     headings line when `run.inserts_found` is zero. Leave out the Cover title line unless `run.cover_title.from` is
     `insert`; when it is, name the title in that line. Leave out the Translator's notes line when `run.notes.found`
     is zero; when it is above zero, give the number of notes the page has. When `run.notes.left_out` is
     `no_translation`, say under the list that the notes go with the translation, which was not printed, so they were
     left out, and that a new PDF with the translation brings them in. When `run.inserts_found` is above zero, name two or three of the
     headings in that line, taken from `run.inserts_names` (the first ones, in the order of the text); when the parts after them are short (a heading for each stanza or two), say that a new
     pecha for each part leaves pechas almost empty. When `size.factor` is below 1 and the layers include the Tibetan
     and another layer, add the recommendation of two blocks under the list: the whole text was set down to fit a long
     paragraph, with the Tibetan at `size.bo` pt, and in two blocks it stays at 21 pt, with a few more sheets.
     When `size.split_paras` is above zero, the layers include the Tibetan and another layer and the PDF is not already in
     two blocks, also recommend two blocks under the list: say how many long paragraphs had their explanation carried to
     the next pecha, apart from its Tibetan, and that in two blocks each script runs on by itself.
     When any pecha in the report's `sides` has `scale` below 1, say under the list how many pechas had their type
     set down to fit and the smallest percentage (the lowest `scale`, rounded down, so 0.924 is 92%), and never say that the type was not set down. When every pecha has `scale` 1, say nothing about smaller type.
     In Portuguese, the printing line says "só frente (ou frente e verso)".
     When the person asks for something different, run again with that option and send the new PDF with the list
     updated and the number of sheets of each. Between a PDF in two blocks and one with the layers together, compare
     the number of sheets and never compare `size.split_paras`: in two blocks those cuts are in the transliteration
     and translation block, where each script runs on by itself.
   - **2**: the formatter refused the page; its message is on stderr (no layer markup, no Tibetan, or a class it
     does not know). Relay the message as it is. Do not lay the page out another way.
   - **3**: the page could not be downloaded (this environment often has no access to the site). Ask the person to
     save the page from the browser (complete page or HTML only) and attach the file, then run again with the file.
     Do not use a web-fetch tool as the source: it returns text without the layer markup.
   - **4**: not a Lotsawa House address: follow the steps for other sources.
   - **1**: a wrong option, a missing or unreadable file, or Playwright missing; the reason is on stderr. Fix what
     it names and run again.
4. Tell the person the PDF prints at A4 landscape with margins set to none and scale at 100%, and that it is cut
   along the dashed line into two folios.

## Steps For Other Sources

1. Read `references/intermediate-format.md` and convert the source into `<name>.pecha.txt`, following its shape and
   its conversion rules. Copy the Tibetan exactly; never write a layer, a licence or a credit the source does not give.
2. Run the check sheet (no PDF is made):

   ```
   python3 scripts/make_pecha.py --text <name>.pecha.txt --check --out <output folder> --labels pt
   ```

   `--labels` sets the language of the check sheet for the person who reads it (`pt` or `en`, the language of the
   conversation); it never changes the credits.

   It prints JSON with `check_sheet` (a Markdown file), `fingerprint`, `blocks`, `blocking` and `notes`.
   Anything under `blocking` (a missing `Site:`, a line printed nowhere) must be fixed in the text first.
3. Show the person the check sheet file as it is: every block with the role the formatter gave it (verse, mantra,
   prose, note, incipit, section heading, instruction) and its Tibetan, transliteration and translation, then the
   credits and the points to check. Add what you left out of the source and why. Ask them to confirm or correct.
   Stop here and wait for the answer: never make the PDF in the same turn as the first check sheet.
4. When the person corrects something, edit `<name>.pecha.txt`, run `--check` again and show the new check sheet.
   Repeat until they confirm.
5. Make the PDF from exactly the confirmed text, with the fingerprint of its last check sheet:

   ```
   python3 scripts/make_pecha.py --text <name>.pecha.txt --confirmed <fingerprint> --out <output folder> \
     --from "<where the text came from>" --layers bo+phon+trans --mode single --lines thin
   ```

   The address of another source does not always say the language: when `Address:` is missing or its path does not
   start with a language code (`/pt/`, `/pt-br/`, `/en/`), pass `--lang` with the language of the translation you
   converted (`en` or `pt`), never the conversation's.

   - **5**: the text changed since that check sheet, or it lacks `Site:`: run `--check` again and show it.
   - **0**, **1**: as for a Lotsawa House page, and send the PDF with the list of the choices used, as in step 3 of
     the steps for a Lotsawa House page.

## Rules

- An address may be given with or without `https://`. Redirects are followed only within Lotsawa House.
- Never edit the PDF, the text or the layers by hand: every change of result comes from an option. The formatter
  itself may cut long prose between lines, rebalance pechas, set a pecha's type down to 92%, carry a last single line
  of continuous Tibetan back to the pecha before it, and split a pair of verses too wide for the pecha into two rows,
  each with its translation; the report lists each pecha's `fill` and `scale` under `sides`, `size.split_pairs` and
  `size.flow_tails`.
- No images are added in this version.
- When Chromium cannot run, say so and stop: install it as step 1 says, or continue in an environment that has
  it. Do not give the person `assets/pecha-engine.html` to open on their own.
- Every run writes a new PDF and a JSON report next to it; nothing is overwritten. The report records the source,
  a fingerprint of the page or text, the options, the date, the version of the skill, and whether AI converted the
  text.
- The credits page states what the source states (translator, address, version, licence, Tibetan source), the
  closing paragraph, in two lines: "Prepared on <date>, <time>, with the help of AI (pecha.skill, version
  <version>)." and "It must be reviewed before use for study and practice. May all beings benefit!" (in Portuguese
  when the credits are). The version is the skill's own, also recorded in the report's `skill.version`. The text of Lotsawa House is CC BY-NC 4.0: the PDF is for practice and study, not for sale. For other
  sources, respect the licence the source states; when it states none, say so to the person.
- Licences: the code is MIT (`LICENSE.txt`); the Noto fonts in `assets/fonts/` keep the SIL Open Font License
  1.1, with their copyright notices (`assets/fonts/OFL.txt`). Keep the fonts folder with its `OFL.txt` whenever the
  skill is copied or shared. Fonts embedded in a PDF do not put the PDF under the font licence.
