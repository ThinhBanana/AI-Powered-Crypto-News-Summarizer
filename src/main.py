import json
from text_preprocessing import preprocess_article_text
from summarize import summarize
from analyze_sentiment import analyze


def run_pipeline():
    articles = []
    with open("../data/news_output.json", "r") as f:
        articles = json.load(f)

    results = []
    for article in articles:
        print(f"[+] Processed: {article['title'][:50]}...")

        # 1. Preprocess
        clean_text = preprocess_article_text(article)

        # 2. Summarize
        try:
            summary = summarize(clean_text)
        except:
            summary = "N/a"
            print("Summary error")

        # 3. Sentiment
        try:
            sentiment = analyze(clean_text)
        except:
            sentiment = "N/a"
            print("Analyze sentiment error")

        # 4. Add result
        results.append({
            "title": article["title"],
            "summary": summary,
            "sentiment": sentiment["label"],
            "confidence": round(sentiment["score"], 3)
        })

    with open("../data/processed_output.json", "w") as out_file:
        json.dump(results, out_file, indent=4)

if __name__ == "__main__":
    run_pipeline()

