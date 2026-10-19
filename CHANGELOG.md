# Changelog

Versions are named by date and letter, as in `2026.10.08z`. This log starts with `2026.10.08z`, the version in use when the repository was prepared for publication.

## [Unreleased]

## [2026.10.19a] - 2026-10-19

### Added

- Pages that open with the translator's introduction are no longer refused. The introduction is left out unless the person asks for it; when the page has one, the skill asks whether to print it at the beginning or keep only the main text. When printed, it comes right after the cover, in one column, on pechas of its own, with each link followed by its address in square brackets.
- Forty-six pechas in the library: forty-four prayers, praises and aspirations, the Amitāyus Dhāraṇī and a short practice of homage and offering to the Buddha and the Arhats.
- The library's prayers are now in four sections: Prayers to the Masters, Prayers of Truth, Aspirations, and Praises and Dedication.
- Two aspirations by Jamyang Khyentse Chökyi Lodrö in the library, each with the translator's introduction at the beginning.

## [2026.10.18a] - 2026-10-18

### Added

- Fifteen pechas in the library: three sūtras, eleven dhāraṇīs and mantras, in a new section, and one prayer, in varied styles.
- When a page gives a shad touching the next syllable, the skill puts in the space it lacks, never changing a Tibetan letter, and says how many it put in.

### Changed

- The reminder at the end of the library pages is shorter.
- On the Portuguese library page, every title that has a translation is in Portuguese, followed by the original.
- Within each section of the library, the pechas are in alphabetical order, in the language of the page.
- The README has a section on the library, with its categories and how many pechas each one has.
- A pecha that opens with transliteration is centred in its height only from 90% full; below that, its text starts at the top, as on the pechas around it.
- The message with the PDF calls each strip a pecha, never a folio, and gives the print settings in plain words in English and Portuguese.

### Fixed

- A version line without a colon on the source page no longer takes the place of the translator on the credits page.

## [2026.10.16b] - 2026-10-16

### Changed

- The images have English names, in `docs/images/`; the opening image of the READMEs is sharper.
- The guides show the Claude menu where the model and the effort level are chosen.
- The guides show the Claude screen where the skill file is uploaded, explain how to see which version is installed and how to change to a new one, and how to be told of new versions on GitHub.
- The example pechas are now a library, in `library/`, with a page in English and another in Portuguese, grouped by type of text: sūtras; prayers, praises and aspirations; and practices. The READMEs show three of them: the Heart Sūtra, the Treasury of Blessings and the Praises to the Twenty-One Tārās.
- The Treasury of Blessings example has the thick line inside the frame.
- When the translator's notes take more than one pecha of their own, the notes on the last one stay in the left column when they fit there, starting at the height of the first note of the pecha before.
- Without the translation layer, the translator's notes are left out, numbers and all, even when they are asked for, and the message sent with the PDF says why.
- The example of the Praises to the Twenty-One Tārās, in Tibetan only, no longer has the translator's notes.
- In the library, the reminder to review each pecha before use is a note at the end of the page.

## [2026.10.16a] - 2026-10-16

### Added

- When the original text has no title and the translator added one before the first verse, that title goes to the cover and to the PDF's title instead of opening the first pecha; it can be left out of the cover.
- The translator's notes can be printed on request: each number where the page puts it, and the notes, numbered as on the page, in two columns above the credits, or on pechas of their own before the credits when they do not fit there. By default they are left out, as before.

### Changed

- The message sent with the PDF names the text by the title the PDF shows in its tab, without translating it, calls each folio a pecha, and calls single-sided printing "front only".
- When some pechas had their type set down to fit, the message says how many and the smallest percentage; a PDF in two blocks is compared with one with the layers together by the number of sheets.
- The report records the title the PDF shows in its tab.
- The report says when the Tibetan title was cut to fit the margin, and the skill then puts the text's own name there instead.
- In Tibetan only, a pecha no longer opens with the shad that closes the verse before it: the last syllables of that verse go to the next pecha with the pair.
- The READMEs open with two more badges, to download pecha.skill and to say it is for Claude; the review notice joins the note on which texts are included, right after the first paragraph about the skill; a tip box right after the steps of "Make Your Own" says which Claude models to use and how to dictate; translators and institutions share one section; each example says its layers and frame in the same form.
- The guides recommend Claude Sonnet or a larger model.
- When a text opens with a homage (Namo…) and then an explanation, that explanation is set apart from the text as the opening explanation, as it is when there is no homage.
- In Tibetan only, when the last line of the Tibetan cannot join the pecha before it, the last two pechas share the lines, both with the text at the top, instead of leaving one line on a pecha of its own.
- The example of the Praises to the Twenty-One Tārās now prints the translator's notes before the credits.

## [2026.10.15a] - 2026-10-15

### Changed

- In the READMEs, the note on which texts are included stresses the absence of a requirement, the Heart Sūtra recitation videos are in a new order, and the Treasury of Blessings credit is shorter.
- The example pechas are made with this version: the PDF tab shows the title of the text, and the credits name the version.

### Fixed

- An explanation that opens the text, before its first verse, stands 7 mm apart from it, instead of almost touching it when the space between verses closes up.

## [2026.10.14e] - 2026-10-14

### Added

- Three example pechas in three layers, with their recitation videos: Barche Lamsel, the Verses of the Eight Noble Auspicious Ones and the Noble Sūtra of Recalling the Three Jewels.
- Recitation videos for the Heart Sūtra, the Sūtra of Boundless Life, Maitreya's Aspiration, the Seven Branches and the Praises to the Twenty-One Tārās.

### Changed

- In the READMEs, the film caption is all in italics, the note on which texts are included comes before the example pechas, and the closing line is plain.

### Fixed

- The PDF carries the title of the text, which PDF readers show in the tab.

## [2026.10.14d] - 2026-10-14

### Added

- A ninth example pecha, the Treasury of Blessings, a practice of Buddha Śākyamuni, in two blocks, with two recitation videos.

### Fixed

- When continuous Tibetan would end with a single line on a pecha of its own, the line goes back to the pecha before it, whose type may be set down to 92%.

## [2026.10.14c] - 2026-10-14

### Changed

- The download link in the READMEs and guides points to the file of the current version, named after it.
- When long paragraphs had their explanation carried to the next pecha, apart from their Tibetan, Claude also recommends two blocks under the list of choices and says how many there are.

### Fixed

- A long paragraph cut across two pechas no longer ends a pixel past the frame.

## [2026.10.14b] - 2026-10-14

### Changed

- When the page has translator's headings, Claude names two or three of them in the list of choices it sends with the PDF.
- The section for translators is shorter, and the paragraphs on how the skill reads the page now sit in the section on the skill.

## [2026.10.14a] - 2026-10-14

### Added

- The credits page says which version of the skill made the pecha, between brackets after the date: "Prepared on <date>, <time>, with the help of AI (pecha.skill, version <version>)." The request to review it and the dedication go on the next line.

### Changed

- Installing the skill takes three short steps in the READMEs, starting from a link that always downloads the latest version. The step-by-step guide stays for the first time.
- The closing line of the READMEs ends with a smiling face.
- The story that opens the READMEs is shorter.
- Claude makes the pecha with the default choices and, with the PDF, lists the choices it used (layers, blocks, printing, frame and the translator's headings), so you can ask for something different. It no longer stops to ask about the blocks or the headings before the first PDF.

## [2026.10.13e] - 2026-10-13

### Changed

- A transliteration and its translation stay on the same pecha even without the Tibetan, in the second of two blocks or in transliteration and translation only.
- A Latin heading that opens a pecha now has the same white space above it as below the last line, as the translator's headings already had.

### Added

- A choice of two blocks: the whole text in Tibetan first, then, from a new pecha, the transliteration and translation, with one cover, one numbering and the credits at the end. The Tibetan keeps the size of a Tibetan-only text, and nothing is set down to fit a long paragraph. Claude asks which layout you prefer and recommends two blocks when the whole text would otherwise need smaller type.

## [2026.10.13d] - 2026-10-13

### Changed

- When a long paragraph makes the whole text smaller, the transliteration no longer gets smaller than the translation, so it stays easy to read. The Tibetan and the translation keep their sizes. Texts with such a paragraph take a few more sheets.
- A long subtitle on the cover now breaks into lines of similar width, instead of leaving a few words alone on the last line.
- The READMEs list the examples by kind of text, from the sūtras to the dedication of merit, name the font section after Google Noto with a link to the Noto project on GitHub, and keep both links to the film scene, dubbed in Portuguese and original in English, in the caption of the photo.

### Added

- A page of ideas for the future, in English and Portuguese, linked from the section for institutions.

## [2026.10.13c] - 2026-10-13

### Changed

- A centred pecha that opens with Tibetan now balances its white space between the vowel signs and the body of the letters: the text sits about 0.8 mm higher than in 2026.10.13b and no longer looks pressed to the bottom. A pecha at the top that opens with Tibetan starts at the same height as the full ones.
- A short pecha that opens with Latin text, with the text at the top, now leaves more white space above its first line: the text starts about 4.5 mm lower than before.
- In a Tibetan-only text, the pair of shads that closes a verse (། །) now sits against the first syllable of the next verse, as in traditional pechas: the space between verses opens between the two shads, a line never breaks between them, and no line ends with the second shad. No character changes.
- The Dedication of Merit example now comes in Tibetan, transliteration and translation. All examples are made again with these changes; their text and their sheets are the same.
- The READMEs open with badges for the licences and the version, and highlight the notice on unreviewed examples and the note that only texts open without empowerment or transmission are included.

## [2026.10.13b] - 2026-10-13

### Changed

- A pecha that opens with Tibetan shares its white space by the highest ink, the vowel signs: the white above them now equals the white below the last line, and the text sits 1.5 mm lower than before.
- A pecha that opens with Tibetan is centred only from 93% full. A shorter one keeps the text at the same height as its neighbours and leaves the rest of the white space below. A pecha that opens with Latin text is still centred from 80% full.
- The examples whose pechas move in height are made again; their text and their sheets are the same.

## [2026.10.13a] - 2026-10-13

### Changed

- When one more verse almost fits on a pecha, the space between verses closes up, from 5 mm down to 3 mm, before the type is set smaller, so fewer pechas are left a third empty. A pecha filled this way never goes above 97.5% of its height, so the vowel signs keep clear of the frame.
- The last line of a Tibetan verse or paragraph always holds at least three syllables: one or two syllables no longer stand alone on a line.
- In single-sided printing, a pecha left over in the middle of a text is dropped and the following pechas are numbered again. Some texts need fewer sheets, such as the Sampa Lhündrupma (15 instead of 16).
- The examples in three layers and in transliteration and translation are made again with these changes; their text is the same.

## [2026.10.11b] - 2026-10-11

### Changed

- The skill files no longer refer to internal development notes. Pechas come out exactly as in 2026.10.11a.
- The licence notice in `LICENSE.txt` points to the example pechas in `examples/`, under CC BY-NC 4.0.

## [2026.10.11a] - 2026-10-11

### Changed

- The opening mark is written ༄༅།།, with the two strokes together and a space after them, and the cover carries it only when the page gives a Tibetan title.
- In the README, the sentence on the formats a pecha can take moves from the story to the section on the skill, and the images show the new opening mark.
- The Seven Branches example is in transliteration and translation, and the Dedication of Merit is a new example in transliteration and translation.
- A pecha is centred in its height from 80% full, instead of 85%; a shorter one keeps the text at the top.
- The frame has three choices: two thin lines (the default), the outer line thick (`--lines thick-out`) or the inner line thick (`--lines thick-in`); `--lines thick` no longer exists. The text breaks at the same points in the three frames.
- In the translation lines, the terma mark has a little space before it, apart from the punctuation.
- The pecha number in the right margin is set in 14 pt; the short title in the left margin stays in 9 pt.

### Added

- The guide on how the skill works has a section on the Tibetan font, Noto Serif Tibetan, with credit to the Monotype design team and to Toshi Omagari.
- The README opens with the story of how the project began, with a scene from the opening of Little Buddha; the guide on how the skill works covers only its parts, with a diagram of the flow. Google's image about how the Noto fonts were made is in the README.
- Eight examples: Leu Dünma, chapter 7, in place of the Sampa Lhundrupma, with two recitations on video; the Seven Branches from Zangchö Mönlam, the Auspicious Verses of Seven Buddhas and the Dedication of Merit in transliteration and translation; the Praises to the Twenty-One Tārās with the thick line outside the frame; and The Sūtra of Boundless Life with the thick line inside.

## [2026.10.10a] - 2026-10-10

### Changed

- The left margin of each pecha carries only the short title; the number of the pecha stays in the right margin.
- The engine is now `assets/pecha-engine.html`. The sheet the person checks before the PDF of other sources is called the check sheet (`check_sheet` in the script's output), and the engine's refusal messages are in English.

### Added

- README in English and Portuguese, with links between them.
- Contributor guide, code of conduct and this changelog.

## [2026.10.08z] - 2026-10-08

### Changed

- The pecha always comes from the skill; the engine is no longer handed out as a separate file.
- Fonts moved out of the engine into `assets/fonts/`, and the engine dropped from 1.5 MB to 74 KB.
- Tibetan at 19 pt with other layers and 21 pt when alone, with optical balance between the top and bottom of each pecha.
- The translated title on the cover goes from 12 pt to 14 pt.
- A pair of verses too wide for the pecha becomes two lines, without shrinking the text, and each verse keeps its translation.
- Translator's headings set on the left, in small capitals, with the new option `--inserts sides` to open a new pecha at each heading.
- A translation rubric stays with the verse before it, and a paragraph with Tibetan and another layer is not split between pechas unless it does not fit alone.
- A pecha that opens with a translator's heading keeps space above the heading.
- Numbered subheadings come out as one block, and line breaks from the source are kept.
- The credits end in one paragraph, with the date, the notice that the pecha was prepared with the help of artificial intelligence and must be reviewed before use, and the dedication.
