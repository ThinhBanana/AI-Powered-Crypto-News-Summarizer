from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze(text: str) -> dict:
    if len(text.split()) < 10:
        return {'label': 'NEUTRAL', 'score': 0.0}

    output = sentiment_analyzer(text)
    return output[0]

# print(analyze("Trump pocketed more than $57 million from token sales by the crypto venture he and his sons helped launch last year, according to federal financial disclosure forms released by the White House."))
# print(analyze("Bitcoin reached a new all-time high, exciting investors worldwide."))
# print(analyze("Massive hacks have made the crypto market unstable and unreliable."))
