import requests

NEWSAPI_URL = "https://newsapi.org/v2/everything"

def search_news(query: str, api_key: str, page_size: int = 5):
    headers = {"Authorization": api_key}
    params = {"q": query, "language": "en", "sortBy": "publishedAt", "pageSize": page_size}
    resp = requests.get(NEWSAPI_URL, headers=headers, params=params)
    # NewsAPI uses 200 OK for both success and error with JSON payload; handle gracefully
    data = resp.json()
    if data.get("status") != "ok":
        # Bubble up a readable error message
        raise RuntimeError(data.get("message", "Unknown error from NewsAPI"))
    # Minimal projection
    articles = [
        {
            "title": a.get("title"),
            "source": (a.get("source") or {}).get("name"),
            "url": a.get("url"),
            "publishedAt": a.get("publishedAt"),
            "description": a.get("description"),
        }
        for a in data.get("articles", [])
    ]
    return articles
