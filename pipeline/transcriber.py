import whisper
import tempfile

class AudioTranscriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, uploaded_file) -> str:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        result = self.model.transcribe(tmp_path)
        return result["text"]
