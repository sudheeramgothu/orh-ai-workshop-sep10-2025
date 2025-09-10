import requests

def get_price(symbol: str, vs: str = "usd"):
    # CoinGecko simple price (no API key required)
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": symbol, "vs_currencies": vs}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if symbol not in data or vs not in data.get(symbol, {}):
        raise ValueError("Price not found. Check symbol (e.g., bitcoin) and vs currency (e.g., usd).")
    return {"symbol": symbol, "vs": vs, "price": data[symbol][vs]}
