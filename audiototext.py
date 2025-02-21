import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]

# Path to your audio file
audio_path = r"C:\Users\princ\Downloads\ENGLISH SPEECH ｜ MARK ZUCKERBERG： Free Speech (English Subtitles).wav"  # Make sure the path is correct
transcribed_text = transcribe_audio(audio_path)

print("Transcribed Text:\n", transcribed_text)
