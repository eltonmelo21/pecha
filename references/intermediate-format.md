# Intermediate Format

The text the AI writes for any source without Lotsawa House layer markup: another site, a translation the person
gives, numbered paragraphs. The formatter reads it by position, so the shape below is the whole contract. Save it as
`<name>.pecha.txt` in UTF-8.

## Shape

Paragraphs are separated by one blank line. Inside a paragraph, each line has a fixed role.

```
༄༅། །<Tibetan title>།
<English title>

by <author>

རྒྱ་གར་སྐད་དུ། <Sanskrit title in Tibetan script> བོད་སྐད་དུ། <Tibetan title>

<Tibetan verse line>
<transliteration of that line>
<translation of that line>

<Tibetan line>
~
<translation>

Section Heading In Title Case

An instruction to the reader, as a sentence:

<Tibetan prose paragraph, one line>
~
<translation of the whole paragraph>

| <translator, as the source states it>
Version: <version, only if the source gives one>
Source
<bibliographic reference of the Tibetan source, only if the source gives one>
Site: <where the text was taken from: site name, book, or "Translation provided by the person">
Address: <https:// address of the source, if it has one>
Licence: <licence, only as the source states it>
```

- **First paragraph**: the Tibetan title starting with the yig mgo (༄༅), then the English title. It goes to the cover.
- **Tibetan paragraph**: line 1 Tibetan, line 2 transliteration, line 3 translation, and nothing more: a
  fourth line is printed nowhere, and the check sheet stops the PDF until it is placed. When the source has no
  transliteration, line 2 is `~`; the position must still be kept. Never write a transliteration or translation
  the source does not give, unless the person provides it.
- **Incipit**: a Tibetan-only paragraph starting with རྒྱ་གར་སྐད་དུ (Sanskrit and Tibetan titles). It goes to the cover.
- **Mantras** are recognised by the formatter (ཨོཾ, ཏདྱ་ཐཱ, or several visargas). Their Sanskrit transliteration
  goes on line 3, the translation layer; line 2 holds the Tibetan-style transliteration or `~`.
- **Colophon**: a Tibetan paragraph opening with ཅེས, ཞེས, འདི་ཡང and similar, then `~` and its translation
  (it is printed as a note).
- **Prose**: a long Tibetan paragraph (more than 16 syllables), then `~` and its translation, is printed as prose.
- **Section headings**: Latin lines in Title Case, up to 9 words. **Instructions** (rubrics): any other Latin line,
  for example a sentence or a line ending in a colon.
- **Credits block**: always last, always opening with the `|` line (it may be just `|` when no translator is
  named). `Site:` is required: the PDF is not made without it. `Licence:` is written only when the source states it.

## Conversion Rules

1. Copy the Tibetan exactly as the source has it, character for character. Do not retype, correct or normalise it.
2. Keep the source's order. Do not merge, split or drop passages; when a passage does not fit the shape, keep it as
   an instruction line and say so in the check sheet.
3. Do not invent a translator, version, licence, address or bibliographic reference. Leave out what the source does
   not state.
4. Verses: one Tibetan line per paragraph, with its own transliteration and translation, when the source aligns
   them line by line. When it gives a whole stanza with one translation, keep the stanza as one paragraph
   (Tibetan on one line, `~` or the transliteration, then the translation).
5. Numbered paragraphs (1.1, 1.2, c.1 and similar, often translation first and Tibetan after): drop the numbers,
   put each Tibetan passage first with its translation on line 3 and `~` on line 2. Put headings that the
   numbering implies as section headings only when the source names them.
6. A footnote, a commentary or an editor's note is not part of the text to recite: leave it out and mention it in
   the check sheet.
