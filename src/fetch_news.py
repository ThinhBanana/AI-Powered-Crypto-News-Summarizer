import os
import json
import requests

from dotenv import load_dotenv, dotenv_values

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_articles():
    url = (
        "https://newsapi.org/v2/everything?"
        "q=crypto&"
        "sortBy=publishedAt&"
        "language=en&"
        f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("✅ Success!")

        results = []
        for article in data['articles']:
            title = article.get('title', "N/A")
            description = article.get('description', "N/A")
            content = article.get('content', 'N/A')

            results.append({"title": title, "description": description, "content": content})

        with open("../data/news_output.json", "w") as out_file:
            json.dump(results, out_file, indent=4)

    else:
        print(f"❌ Failed with status code {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    fetch_articles()