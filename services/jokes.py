import requests

def get_joke():
    # icanhazdadjoke.com supports JSON with an Accept header
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json", "User-Agent": "orh-workshop-bot"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return {"joke": data.get("joke")}
