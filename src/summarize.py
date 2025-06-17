from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text: str) -> str:
    if len(text) < 20:
        return "Text too short to summarize."

    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]['summary_text']

print(summarize("US President Donald Trump pocketed more than $57 million from token sales by the crypto venture he and his sons helped launch last year, according to federal financial disclosure forms released by the White House."))