# How to Use the Pecha Skill

**English** · [Português](como-usar.md)

This guide is for those who have never used artificial intelligence. It takes you from installation to the printed pecha, one step at a time. You do not need to type any technical command.

The pecha skill turns a [Lotsawa House](https://www.lotsawahouse.org) page into a PDF ready to print. Each A4 sheet carries two pechas, with a frame, a cover and credits. It is for those who practise and want the text in the form of a pecha, in Tibetan only or with transliteration and translation.

Every pecha is prepared with the help of artificial intelligence. That is why it must be reviewed before it is used for study and practice, and this guide shows how to do it before you print.

The menu names are in English, as they appear in Claude. They were checked in the Claude help centre on 11 October 2026 and may change.

## What You Will Need

- A [Claude](https://claude.ai) account. The skill works on the free plan and on the paid plans too ([Claude plans](https://claude.com/pricing), checked on 11 October 2026). Skills and code execution are on the Free, Pro, Max, Team and Enterprise plans ([Claude help](https://support.claude.com/en/articles/12512180-use-skills-in-claude), checked on 11 October 2026).
- Claude in the browser, in the Claude desktop app or in the phone app ([Claude help](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile), checked on 11 October 2026). The skill was tested in the phone app on 11 October 2026.
- A printer that prints on A4 paper, preferably a laser printer.

## Part 1: Prepare Claude (First Time Only)

### 1. Turn On Code Execution

The skill needs Claude to be able to run programs to build the PDF.

1. In Claude, open **Settings**.
2. Go to **Capabilities**.
3. Turn on **Code execution and file creation**.
4. Then, under **Customize**, click **Skills** and check that skills are turned on.

On the Team and Enterprise plans, whoever manages the organisation's account turns on code execution and skills in **Organization settings**, **Plugins & skills**, on the **Policy** tab.

Path checked in the [Claude help](https://support.claude.com/en/articles/12512180-use-skills-in-claude) on 11 October 2026.

### 2. Download the Skill Package

1. Click [pecha-2026.10.15a.skill](https://github.com/eltonmelo21/pecha/releases/download/v2026.10.15a/pecha-2026.10.15a.skill) to download the current version. If you need an earlier version, open this project's [Releases](https://github.com/eltonmelo21/pecha/releases) page.
2. Keep the file in a folder that is easy to find, such as Downloads. You do not need to open it.

### 3. Add the Skill to Claude

1. In Claude, click your initials and name, then **Settings**. Under **Customize**, click **Skills**.
2. Click the **+** button and then **+ Create skill**.
3. Choose **Upload a skill**.
4. Upload the file you downloaded in step 2.
5. Check that the **pecha** skill appears in the list with its switch on.

If you already have a version of the **pecha** skill installed, remove the old one before you upload the new one:

1. In **Settings**, under **Customize**, click **Skills** and then the **pecha** skill.
2. Turn off the switch, at the top.
3. Click the **...** button, next to the switch, and then **Delete**. Confirm with **Delete**.
4. Follow the steps above to upload the new file.

Path checked in the [Claude help](https://support.claude.com/en/articles/12512180-use-skills-in-claude) on 11 October 2026.

## Part 2: Make a Pecha

### 4. Choose the Text on Lotsawa House

1. Open [Lotsawa House](https://www.lotsawahouse.org) and find the text.
2. Copy the page address from the browser bar. It starts with `https://www.lotsawahouse.org/`.

Use only texts that you are able to practise. Some texts require an empowerment or a transmission from a teacher.

### 5. Ask Claude for the Pecha

Open a new conversation in Claude, copy one of the sentences below, replace the address with the one of your page and send it.

With Tibetan, transliteration and translation:

```
Make a pecha of this Lotsawa House page, with Tibetan, transliteration and translation: https://www.lotsawahouse.org/...
```

In Tibetan only:

```
Make a pecha in Tibetan only of this Lotsawa House page: https://www.lotsawahouse.org/...
```

Claude uses the skill on its own. The first time, it may take a few minutes to get ready. It makes the pecha with the defaults and, with the PDF, tells you which choices it used: layers, blocks, printing, frame and, when the page has them, the translator's headings. To change any of them, just ask in your own words.

If the PDF does not come out, see [Claude Models](#claude-models), just below. To change the layers, the frame, the printing or the translator's headings, see [Pecha Choices](#pecha-choices), at the end of this guide.

### Claude Models

Claude has different models, and each one has effort levels. To choose, click the model name, next to the send button, then **Effort**, and choose the level ([Claude help](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings), checked on 11 October 2026).

Tested on 11 October 2026, in the phone app: Haiku with the **High** effort level made the PDF. With the low and medium levels, Haiku did not. Sonnet has also been used with the skill and usually works well. Opus has not yet been tested with this version of the skill.

The recommendation is to use, at least, Haiku with the **High** effort level.

On other artificial intelligence platforms, such as ChatGPT, Gemini and Grok, the skill has not yet been tested.

### 6. If Claude Cannot Open the Address

Save the page on your computer and send the file to Claude:

1. On the Lotsawa House page, use the browser menu **Save Page As** (on the keyboard, Ctrl+S, or Cmd+S on a Mac).
2. Choose the format **Web Page, HTML Only**.
3. In the conversation with Claude, attach this file with the paper clip or the **+** button, and send the same sentence as in step 5, replacing the address with "of the page I attached".

### 7. Download the PDF

When it is done, Claude shows the PDF in the conversation. Click it to download.

## Part 3: Review and Print

### 8. Review Before Use

Review the pecha before you print it. Open every page of the PDF and check:

- that the text is complete, from beginning to end;
- whether any pecha came out nearly empty;
- whether any word is touching the frame or another word.

If something is wrong, tell Claude in the same conversation what you saw and on which page.

### 9. Print

1. Print on **A4** paper, in **landscape** orientation, preferably on a laser printer.
2. In the print window, choose a scale of **100%** (or "actual size"). Do not use "fit to page".
3. If you asked for the pecha for double-sided printing, choose flipping on the **long edge**.
4. Each sheet carries two pechas, one at the top and one at the bottom. Cut along the dashed line in the middle, preferably with a paper guillotine, so the cut comes out straight.

## Pecha Choices

Without any request, the pecha comes out with the default of each choice below. To change one, add the ready-made sentence to your request in step 5, or send the sentence afterwards, in the same conversation, to receive a new version of the PDF.

### Layers

The default is Tibetan, transliteration and translation: each verse in Tibetan, with its reading in Latin letters just below and the translation after it.

Tibetan only, as in traditional pechas. The Tibetan is a little larger when it is on its own:

```
I would like the pecha in Tibetan only.
```

Tibetan and translation, without the transliteration, suited to those who study the Tibetan language:

```
I would like the pecha with Tibetan and translation, without the transliteration.
```

Other combinations also work, for example Tibetan and transliteration, without the translation:

```
I would like the pecha with Tibetan and transliteration, without the translation.
```

### Two Blocks

The default keeps every layer together in each pecha. You can also have two blocks: first the whole text in Tibetan only and then, from a new pecha, the transliteration and translation, with one cover. This way the Tibetan and the Latin text keep their normal size even in texts with long paragraphs, at the cost of a few more sheets. With the PDF, Claude recommends two blocks when the whole text needed smaller type:

```
I would like the pecha in two blocks: first the Tibetan, then the transliteration and translation.
```

### Frame Lines

The default is the frame with two thin lines. The alternatives have one thick line and one thin line, with the thick one outside:

```
I would like the frame with the thick line outside.
```

or with the thick one inside:

```
I would like the frame with the thick line inside.
```

The text breaks at the same points in the three frames.

### Single-Sided or Double-Sided

The default is to print on one side of the sheet only. If your printer prints on both sides, ask for the pecha prepared for it. When printing, the sheet is flipped on the long edge:

```
I would like the pecha for double-sided printing.
```

### Translator's Headings

Some translations have headings that the translator placed in the middle of the text, without Tibetan, for example the name of each part of the practice. The default is to print these headings in the middle of the text, with the verse that each one opens. When the page has these headings, Claude names some of them with the PDF.

Each heading opening a new pecha, good when the headings open long parts of the text:

```
I would like each translator's heading to start a new pecha.
```

The headings left out, with only the text of the practice:

```
I would like the pecha without the translator's headings.
```

### Terma Mark

Treasure texts (terma) end the Tibetan verses with the mark ༔. In these texts, the skill repeats the mark at the end of the transliteration and of the translation of each verse that ends with it in Tibetan, on its own, without you having to ask. This is the default. To take the mark out of the transliteration and the translation:

```
I would like the pecha without repeating the terma mark in the transliteration and the translation.
```

---

A pecha made with texts from Lotsawa House follows the CC BY-NC 4.0 licence: it is for study and practice, not for sale.
