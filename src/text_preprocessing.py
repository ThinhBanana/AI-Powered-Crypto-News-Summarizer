import re

def preprocess_article_text(article: dict) -> str:
    result = ' '.join([article.get('title', ''),
                       article.get('description',''),
                       article.get('content','')])
    result = re.sub(r"<.*?>", "", result)
    result = re.sub(r"\s+", " ", result)
    result = result[:1000]

    return result

# print(preprocess_article_text({
#         "title": "Vietnam legalizes crypto under new digital technology law",
#         "description": "Vietnam\u2019s new digital tech law brings crypto assets under regulation and introduces bold incentives for AI and semiconductor industries, positioning itself for global tech leadership.",
#         "content": "The National Assembly of Vietnam approved the Law on Digital Technology Industry on June 14, bringing digital assets under regulatory oversight.\r\nThe legislation, set to take effect on Jan. 1, 2026, \u2026 [+2720 chars]"
#     }))
