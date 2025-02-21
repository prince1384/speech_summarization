from transformers import pipeline
from audiototext import transcribed_text

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Truncate long transcribed text
MAX_INPUT_LENGTH = 1024
transcribed_text = transcribed_text[:MAX_INPUT_LENGTH]

# Summarize the text
def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

# Check input length
print("Input text length:", len(transcribed_text))

summary = summarize_text(transcribed_text)

print("\nSummarized Text:\n", summary)
