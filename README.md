# AI Grammar Scoring Engine

A **local-first AI application** that evaluates spoken English grammar from audio input. The system transcribes user speech using **OpenAI Whisper** and presents the transcript for analysis. The application is designed with a **privacy-preserving architecture** where all processing runs entirely on the user’s machine.

---

## Current Features

### Speech-to-Text Transcription

* Uses **OpenAI Whisper (local model)** to transcribe `.wav` and `.mp3` audio files
* Handles diverse accents and speaking styles
* Runs fully offline after initial model download

### Interactive Web Interface

* Built with **Streamlit**
* Simple audio upload workflow
* Clear presentation of results
* Custom dark-themed UI styling

### Privacy-First Architecture

* No external API calls
* No audio or transcript data is stored or transmitted
* All inference runs locally on the user’s machine

---

## Planned / Scaffolded Features

The codebase includes structure for future enhancements:

* **Grammar analysis using a lightweight LLM (TinyLlama)**
* **Rubric-based grammar scoring (1–5)**
* **Structured output** (score, justification, example errors)
* **Actionable feedback for language learners**

These components are intentionally modular and can be extended by implementing the `GrammarAnalyzer.evaluate()` method.

---

## How the Application Works

### Transcription Stage

1. User uploads a `.wav` or `.mp3` file
2. Audio is processed locally using Whisper
3. Spoken English is converted into raw text

### Analysis Stage (Scaffolded)

* A grammar analysis pipeline is initialized
* A scoring rubric is defined
* The evaluation logic is prepared for future LLM-based processing

---

## Tech Stack

* **Python 3.11+**
* **Streamlit** – Web interface
* **OpenAI Whisper** – Speech-to-text transcription
* **TinyLlama (Transformers)** – Grammar analysis (scaffolded)
* **PyTorch** – Model execution
* **Hugging Face Transformers** – Model loading
* **FFmpeg** – Audio processing dependency

---

## Project Structure

```text
AI_Grammar/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
├── pipeline/
│   ├── analyzer.py        # Grammar analysis scaffold (LLM-based)
│   ├── transcriber.py     # Whisper-based transcription
│   ├── rubric.py          # Grammar scoring rubric
│   └── __init__.py
└── README.md
```

---

## Installation

### Prerequisites

* Python **3.11 or later**
* **FFmpeg** (required for Whisper)

Verify FFmpeg installation:

```bash
ffmpeg -version
```

---

### Setup

Clone the repository:

```bash
git clone https://github.com/your-username/AI_Grammar.git
cd AI_Grammar
```

Create and activate a virtual environment:

**Windows**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Launch the Streamlit app:

```bash
streamlit run app.py
```

On first launch, the required AI models will be downloaded locally (one-time setup).

### Steps

1. Upload a `.wav` or `.mp3` file
2. Click **Analyze Audio**
3. View the transcription and UI output

---

## Privacy

This application is **fully local-first**:

* No audio is uploaded to external servers
* No transcripts are stored
* All AI models run on-device

---


