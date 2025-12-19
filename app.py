import streamlit as st
from pipeline.analyzer import GrammarAnalyzer
from pipeline.transcriber import AudioTranscriber


# Page Config
st.set_page_config(
    page_title="AI Grammar Scoring Engine",
    page_icon="🗣️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }
    .title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }
    .card {
        background: #0f172a;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }
    .score {
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        color: #22c55e;
    }
    .score-label {
        text-align: center;
        font-size: 1.1rem;
        color: #94a3b8;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .example {
        background: #020617;
        border-left: 4px solid #ef4444;
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 6px;
        font-family: monospace;
        color: #fecaca;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="title">AI Grammar Scoring Engine</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload spoken English audio and receive an instant grammar score with actionable feedback.</div>',
    unsafe_allow_html=True,
)

# Upload Card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🎧 Upload Audio</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Supported formats: .wav, .mp3", type=["wav", "mp3"], label_visibility="collapsed")

analyze = st.button("🔍 Analyze Audio", use_container_width=True, disabled=uploaded_file is None)

st.markdown('</div>', unsafe_allow_html=True)

# Processing
if analyze and uploaded_file:
    with st.spinner("Transcribing and analyzing speech..."):
        transcriber = AudioTranscriber()
        transcript = transcriber.transcribe(uploaded_file)

        analyzer = GrammarAnalyzer()
        result = analyzer.evaluate(transcript)

    # Results
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown('<div class="score">{}</div>'.format(round(result["score"], 1)), unsafe_allow_html=True)
    st.markdown('<div class="score-label">Grammar Proficiency Score (1–5)</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📝 Justification</div>', unsafe_allow_html=True)
    st.write(result["justification"])

    if result.get("examples"):
        st.markdown('<div class="section-title">❌ Example Errors</div>', unsafe_allow_html=True)
        for ex in result["examples"]:
            st.markdown(f'<div class="example">{ex}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    "<p style='text-align:center;color:#64748b;margin-top:2rem;'>All processing runs locally • No audio data is stored</p>",
    unsafe_allow_html=True,
)
