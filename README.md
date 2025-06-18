# AI-Powered-Crypto-News-Summarizer

A lightweight NLP pipeline that fetches real-time crypto news, summarizes it using a large language model, and analyzes sentiment.

---

## 🔧 Features

- Fetch crypto news from NewsAPI.org
- Clean and truncate article text
- Summarize using `facebook/bart-large-cnn`
- Analyze sentiment using `distilbert-base-uncased-finetuned-sst-2-english`
- Save results in JSON

---

## 🛠️ Setup

```bash
git clone https://github.com/<your-username>/crypto-news-llm-pipeline.git
cd crypto-news-llm-pipeline
pip install -r requirements.txt
```

Add your API key to src/.env file
- NEWS_API_KEY = "your_api_key_here"

---

## ▶️ Run

```bash
python src/fetch_news.py     # Step 1: Fetch news
python src/main.py           # Step 2: Run pipeline (preprocess + summarize + analyze)
```

---

## 📁 Outputs

- data/news_output.json — Raw articles
- data/processed_output.json — Summarized & tagged results

---