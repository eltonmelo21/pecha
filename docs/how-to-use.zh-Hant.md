# 如何使用 pecha 技能

[English](how-to-use.md) · [Português](como-usar.md) · **繁體中文**

> [!NOTE]
> 本頁中文版在人工智慧的協助下翻譯，希望方便華人佛教修行者閱讀。譯文尚未經熟悉佛法的中文譯者審閱，難免有疏漏之處，若有錯誤，敬請見諒；日後的版本將繼續校訂改進。🙏

這份指南寫給從未使用過人工智慧的人。它一步一步帶您從安裝走到印好的藏式長條經書（pecha）。您不需要輸入任何技術指令。

pecha 技能（skill）把 [Lotsawa House](https://www.lotsawahouse.org) 的網頁轉成可以直接列印的 PDF。每張 A4 紙印兩條 pecha，附有邊框、封面和致謝頁。它是為修行、並希望經文以 pecha 形式呈現的人而做的，可以只有藏文，也可以附上音譯和翻譯。

每一份 pecha 都是在人工智慧的協助下製作的。因此，用於學習和修持之前必須先校對，本指南會說明如何在列印前校對。

選單名稱保留英文，與 Claude 中顯示的一致。這些名稱已於 2026年10月11日在 Claude 說明中心核對，日後可能會變動。

## 您需要準備的

- 一個 [Claude](https://claude.ai) 帳號。這個技能在免費方案和付費方案上都能使用（[Claude 方案](https://claude.com/pricing)，2026年10月11日核對）。技能和程式碼執行功能適用於 Free、Pro、Max、Team 和 Enterprise 方案（[Claude 說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)，2026年10月11日核對）。
- 在瀏覽器、Claude 桌面應用程式或手機應用程式中使用 Claude（[Claude 說明](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)，2026年10月11日核對）。這個技能已於 2026年10月11日在手機應用程式中測試過。
- 一台能列印 A4 紙的印表機，最好是雷射印表機。

## 第 1 部分：設定 Claude（只需第一次）

### 1. 開啟程式碼執行

這個技能需要 Claude 能夠執行程式，才能製作 PDF。

1. 在 Claude 中打開 **Settings**。
2. 進入 **Capabilities**。
3. 開啟 **Code execution and file creation**。
4. 接著在 **Customize** 下點選 **Skills**，確認技能已開啟。

在 Team 和 Enterprise 方案中，由管理組織帳號的人在 **Organization settings** 的 **Plugins & skills** 中、**Policy** 分頁裡開啟程式碼執行和技能。

路徑已於 2026年10月11日在 [Claude 說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)中核對。

### 2. 下載技能套件

1. 點選 [pecha-2026.10.22.skill](https://github.com/eltonmelo21/pecha/releases/download/v2026.10.22/pecha-2026.10.22.skill) 下載目前的版本。如果需要較早的版本，請打開本專案的 [Releases](https://github.com/eltonmelo21/pecha/releases) 頁面。
2. 把檔案存放在容易找到的資料夾，例如「下載」。不需要打開它。

### 3. 把技能加入 Claude

1. 在 Claude 中點選您的姓名縮寫和名字，然後點 **Settings**。在 **Customize** 下點選 **Skills**。
2. 點選 **+** 按鈕，再點 **+ Create skill**。
3. 選擇 **Upload a skill**。
4. 上傳您在第 2 步下載的檔案。
5. 確認 **pecha** 技能出現在清單中，而且開關是開啟的。

![Claude 桌面應用程式的 Upload a skill 畫面，2026年10月16日：在 Customize、Skills 下，Skill file 欄位已選取檔案 pecha-2026.10.16a.skill（1 MB）](images/claude-upload-a-skill.png)

路徑已於 2026年10月11日在 [Claude 說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)中核對。

### 更新到新版本

新版本推出時，您已安裝的技能不會自動更新。想知道自己用的是哪個版本，請打開它製作的任何一份 PDF 的最後一條 pecha：致謝頁上寫著「pecha.skill, version」，後面接著版本號，例如 2026.10.22。

要換成新版本，請像第 2 步那樣下載新檔案，再替換舊的技能：

1. 在 **Settings** 的 **Customize** 下點選 **Skills**，再點 **pecha** 技能。
2. 關閉上方的開關。
3. 點選開關旁的 **...** 按鈕，再點 **Delete**。按 **Delete** 確認。
4. 像第 3 步那樣上傳新檔案。

Claude 說明中沒有提到其他更換已上傳技能的方法：只能刪除後重新上傳（[Claude 說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)，2026年10月16日核對）。

### 新版本推出時收到通知

如果有 GitHub 帳號，每次推出新版本時都可以收到通知：

1. 打開本專案在 GitHub 上的頁面 [eltonmelo21/pecha](https://github.com/eltonmelo21/pecha)，並登入。
2. 點選頁面上方的 **Watch**，再點 **Custom**。
3. 勾選 **Releases** 並確認。

之後每個新版本都會出現在您的 GitHub 通知中；如果您在 GitHub 設定中開啟了電子郵件通知，也會收到電子郵件（[GitHub Docs](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications)，2026年10月16日核對）。沒有帳號的話，請不時打開 [Releases](https://github.com/eltonmelo21/pecha/releases) 頁面看看。

## 第 2 部分：製作 pecha

### 4. 在 Lotsawa House 選擇經文

1. 打開 [Lotsawa House](https://www.lotsawahouse.org)，找到經文。
2. 從瀏覽器的網址列複製網頁地址。它以 `https://www.lotsawahouse.org/` 開頭。

請只使用您能夠修持的經文。有些經文需要從上師那裡得到灌頂或口傳。

### 5. 請 Claude 製作 pecha

在 Claude 中開啟新的對話，複製下面其中一句話，把網址換成您的網頁網址，然後送出。

藏文、音譯和翻譯：

```
Make a pecha of this Lotsawa House page, with Tibetan, transliteration and translation: https://www.lotsawahouse.org/...
```

只有藏文：

```
Make a pecha in Tibetan only of this Lotsawa House page: https://www.lotsawahouse.org/...
```

Claude 會自行使用這個技能。第一次可能需要幾分鐘準備。它會用預設值製作 pecha，並在附上 PDF 時告訴您用了哪些選擇：層、區塊、列印、邊框，以及網頁中有的話，譯者的標題。想改變其中任何一項，用您自己的話提出即可。

如果沒有產生 PDF，請看下方的 [Claude 模型](#claude-模型)。想改變層、邊框、列印或譯者的標題，請看本指南最後的 [pecha 的選項](#pecha-的選項)。

### Claude 模型

Claude 有不同的模型，每個模型都有不同的思考強度（effort）。要選擇時，點選送出按鈕旁的模型名稱，再點 **Effort**，選擇程度（[Claude 說明](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)，2026年10月11日核對）。

![從模型名稱打開的 Claude 應用程式選單，2026年10月16日：模型 Fable 5.1、Opus 5.5、Sonnet 5.5（已勾選）和 Haiku 5.5，以及 Effort 子選單，其中有 Low（已勾選）、Medium、High、Extra 和 Max](images/claude-model-and-effort-menu.png)

2026年10月11日在手機應用程式中測試：Haiku 在 **High** 思考強度下製作出了 PDF。在低和中等程度下，Haiku 沒有做到。2026年10月13日測試：Sonnet 在低思考強度下製作出了一份三層日修法的 PDF。Opus 尚未用這個版本的技能測試過。

建議使用 Claude Sonnet 或更大的模型。到目前為止的測試中，低思考強度已經足夠；在較複雜的情況下，可能需要更大的模型（例如 Opus）或更高的思考強度。

在其他人工智慧平台上，例如 ChatGPT、Gemini 和 Grok，這個技能尚未測試過。

### 6. 如果 Claude 無法打開網址

把網頁存到您的電腦上，再把檔案傳給 Claude：

1. 在 Lotsawa House 的網頁上，使用瀏覽器選單的 **Save Page As**（鍵盤快速鍵 Ctrl+S，Mac 上是 Cmd+S）。
2. 選擇 **Web Page, HTML Only** 格式。
3. 在與 Claude 的對話中，用迴紋針或 **+** 按鈕附上這個檔案，送出與第 5 步相同的句子，把網址換成「of the page I attached」。

### 7. 下載 PDF

完成後，Claude 會在對話中顯示 PDF。點選它即可下載。

## 第 3 部分：校對與列印

### 8. 使用前先校對

列印前請先校對 pecha。打開 PDF 的每一頁，檢查：

- 經文是否從頭到尾完整；
- 是否有哪一條 pecha 幾乎是空白的；
- 是否有哪個字碰到邊框或其他字。

如果發現問題，請在同一個對話中告訴 Claude 您看到了什麼、在哪一頁。

### 9. 列印

1. 用 **A4** 紙、**橫向**列印，最好使用雷射印表機。
2. 在列印視窗中選擇 **100%** 比例（或「實際大小」）。不要使用「符合頁面大小」。
3. 如果您要的是雙面列印的 pecha，請選擇沿**長邊**翻頁。
4. 每張紙印兩條 pecha，一條在上，一條在下。沿著中間的虛線裁切，最好使用裁紙機，這樣切口才會平直。

各種印表機的選項名稱、雙面列印時 pecha 的順序，以及裁切線需要注意的地方，請看[如何列印 pecha](printing.zh-Hant.md)。

## pecha 的選項

如果沒有特別要求，pecha 會以下面每一項選擇的預設值製作。想改變其中一項，可以在第 5 步的請求中加上現成的句子，或在同一個對話中隨後送出這句話，就會收到新版本的 PDF。

### 層

預設是藏文、音譯和翻譯：每一句偈頌先是藏文，緊接著下方是拉丁字母的讀法，然後是翻譯。

只有藏文，就像傳統的 pecha。藏文單獨出現時會稍微大一點：

```
I would like the pecha in Tibetan only.
```

藏文和翻譯，不含音譯，適合學習藏文的人：

```
I would like the pecha with Tibetan and translation, without the transliteration.
```

其他組合也可以，例如藏文和音譯，不含翻譯：

```
I would like the pecha with Tibetan and transliteration, without the translation.
```

### 兩個區塊

預設會把所有的層放在每一條 pecha 裡。您也可以選擇兩個區塊：先是只有藏文的整部經文，然後從新的一條 pecha 開始放音譯和翻譯，共用一個封面。這樣即使是段落很長的經文，藏文和拉丁文字也能保持正常大小，代價是多用幾張紙。附上 PDF 時，如果整部經文需要用較小的字，Claude 會建議使用兩個區塊：

```
I would like the pecha in two blocks: first the Tibetan, then the transliteration and translation.
```

### 邊框線條

預設是兩條細線的邊框。另外的選擇是一條粗線和一條細線，粗線在外：

```
I would like the frame with the thick line outside.
```

或粗線在內：

```
I would like the frame with the thick line inside.
```

三種邊框中，經文換行的位置都相同。

### 單面列印或雙面列印

預設只印在紙的一面。如果您的印表機可以印兩面，請要求為雙面列印準備的 pecha。列印時，紙張沿長邊翻轉：

```
I would like the pecha for double-sided printing.
```

### 譯者的標題

有些翻譯中，譯者在經文中間加了沒有藏文的標題，例如修法每個部分的名稱。預設是把這些標題印在經文中間，與它所開啟的偈頌放在一起。網頁中有這類標題時，Claude 會在附上 PDF 時列出其中幾個。

每個譯者標題都從新的一條 pecha 開始，適合標題開啟的是經文中較長的部分時：

```
I would like each translator's heading to start a new pecha.
```

省略這些標題，只保留修法的經文：

```
I would like the pecha without the translator's headings.
```

### 伏藏符號

伏藏經文的藏文偈頌以符號 ༔ 結尾。在這類經文中，凡是藏文以這個符號結尾的偈頌，技能會自動在其音譯和翻譯的結尾重複這個符號，不需要您提出。這是預設值。要從音譯和翻譯中去掉這個符號：

```
I would like the pecha without repeating the terma mark in the transliteration and the translation.
```

---

以 Lotsawa House 的經文製作的 pecha 遵循 CC BY-NC 4.0 授權：僅供學習和修持，不可販售。
