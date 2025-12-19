# 🗣️ AI Grammar Scoring Engine

A **local-first AI application** that evaluates spoken English grammar in real time. The system transcribes user speech and scores grammatical proficiency using a zero-shot Large Language Model (LLM), returning both a **numerical score** and **actionable feedback** — all while keeping user data private.

---

## 🚀 Overview

The AI Grammar Scoring Engine is a proof-of-concept project designed to explore:

* Zero-shot grammatical evaluation using LLMs
* Speech-to-text pipelines for spoken language assessment
* Privacy-preserving, fully local AI systems

The application is ideal for **English language learners**, **educational demos**, and **AI/ML portfolios**.

---

## ✨ Features

* **Speech-to-Text Transcription**
  Uses OpenAI Whisper for accurate transcription across accents and dialects.

* **LLM-Powered Grammar Analysis**
  Employs a lightweight LLM (TinyLlama) to perform rubric-based grammatical evaluation.

* **Rubric-Based Scoring (1–5)**
  Scores spoken grammar according to a predefined proficiency rubric.

* **Qualitative Feedback**
  Provides a clear justification and concrete examples of grammatical errors.

* **Privacy-First Architecture**
  All processing runs 100% locally. No audio or text data leaves the user’s machine.

* **Interactive Web UI**
  Clean, modern interface built with Streamlit.

---

## 🧠 How It Works

The engine operates as a **two-stage AI pipeline**:

### 1️⃣ Transcription Stage

* User uploads a `.wav` or `.mp3` audio file
* Whisper transcribes speech into raw text

### 2️⃣ Analysis Stage

* The transcript is embedded into a structured prompt
* The LLM evaluates grammar using a predefined rubric
* The model returns structured JSON containing:

  * `score` – Grammar score (1.0–5.0)
  * `justification` – Explanation of the score
  * `examples` – Direct quotes highlighting errors

The Streamlit frontend parses and displays these results clearly.

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **Streamlit** – Web interface
* **OpenAI Whisper** – Speech-to-text
* **TinyLlama (Transformers)** – Grammar analysis
* **PyTorch** – Model execution
* **Hugging Face Hub** – Model management

---

## 📂 Project Structure

```text
AI_Grammar/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
├── pipeline/
│   ├── analyzer.py        # LLM grammar evaluation
│   ├── transcriber.py     # Whisper-based transcription
│   ├── rubric.py          # Grammar scoring rubric
│   └── __init__.py
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

* Python **3.11 or later**
* FFmpeg (required for Whisper)

#### Verify FFmpeg

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

```powershell
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

## ▶️ Usage

Launch the Streamlit app:

```bash
streamlit run app.py
```

On first launch, the AI models will be downloaded locally (one-time setup).

### Steps

1. Upload a `.wav` or `.mp3` file
2. Click **Analyze Audio**
3. View your grammar score and feedback

---

## 🔒 Privacy

This application is **fully local-first**:

* No audio is uploaded to external servers
* No transcripts are stored or transmitted
* All models run on the user’s machine

Ideal for privacy-sensitive demos and offline use.

---

## 🧪 Future Enhancements

* Fine-tuned grammar regression model
* Hybrid scoring (ML model + LLM explanation)
* Fluency & pronunciation metrics
* User accounts and progress tracking
* Microphone-based live recording
* Quantized models for faster CPU inference

---

## 📌 Disclaimer

This project is a **proof of concept** and not intended for high-stakes language assessment or certification.

---

## 👤 Author

Developed as an AI/ML portfolio project demonstrating:

* End-to-end AI pipelines
* Local LLM deployment
* Applied NLP & speech processing

---

⭐ If you find this project useful, feel free to star the repository!
