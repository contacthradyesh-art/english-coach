# English Coach

A Claude Skill for Hindi-speaking learners who want to improve English grammar, vocabulary, reading, and clear spoken communication.

## What's included

- **Correction mode:** fixes grammar and gives a natural alternative.
- **Practice mode:** roleplays for daily life, shops, offices, and interviews.
- **Vocabulary mode:** five useful words per session with Hindi meanings and a quiz.
- **Reading mode:** simplifies English passages and checks comprehension.
- **Voice-practice mode:** sentence-by-sentence transcript comparison and speaking-clarity drills.
- **Browser voice checker:** a no-library Web Speech API page for speech-to-text practice.

## Install the Claude Skill

1. Download or clone this repository.
2. Keep the folder structure unchanged.
3. Package the `english-coach` folder as a ZIP if your Claude interface asks for a ZIP Skill upload.
4. In Claude, open **Customize / Skills** (or the Skills area available in your account).
5. Choose **Add skill / Upload skill**, upload the ZIP, and enable it.
6. Start a chat and ask: “Help me practise English” or “Start voice practice.”

If your Claude version supports adding Skills from a folder or repository, follow its current import flow and select this folder.

## Run the voice checker locally

1. Open `scripts/voice-checker/index.html` in a supported browser.
2. Allow microphone access when prompted.
3. Choose English (India) or Hindi (India).
4. Enter a target sentence, press **Start**, and speak clearly.
5. Review the transcript and word-by-word comparison.
6. Press **Copy for Claude** and paste the result into your Claude chat.

**Browser note:** Web Speech API support varies. Chrome and Chromium-based browsers generally provide the best support. Microphone access may require HTTPS or localhost; if opening the file directly does not work, serve the folder through a local development server or publish it using HTTPS.

## Host the voice checker with GitHub Pages

1. Open this repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch **main** and folder **/(root)**, then save.
5. GitHub will publish the repository site. Open the Pages URL and append `/scripts/voice-checker/` if GitHub shows the repository root.
6. Allow microphone access on the HTTPS Pages site.

The voice checker runs in the browser. It does not send recordings to this repository. Speech recognition is provided by the browser and its speech service; review your browser's privacy settings.

## Repository structure

```text
english-coach/
├── SKILL.md
├── README.md
├── references/
│   ├── common-mistakes-hindi-speakers.md
│   ├── vocabulary-levels.md
│   ├── roleplay-scenarios.md
│   └── pronunciation-hindi-speakers.md
└── scripts/
    ├── quiz.py
    └── voice-checker/
        └── index.html
```

## Quiz script

Run with Python 3:

```bash
python scripts/quiz.py words.json
```

The JSON file should contain a list of objects with `word`, `meaning`, and `options` (four choices including the correct meaning). See the script's usage message for details.

## Learning tip

Practise for 15–20 minutes daily. Speak slowly enough to finish each word, pause between ideas, and focus on clarity before speed.
