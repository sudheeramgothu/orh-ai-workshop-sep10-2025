import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory


from services.open_meteo import get_weather_for_city
from services.newsapi import search_news
from services.jokes import get_joke
from services.crypto import get_price

load_dotenv()

app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.get("/")
def root():
    return jsonify({
        "ok": True,
        "message": "Welcome to the ORH Workshop Bot API. Try /api/weather?city=Atlanta or /api/news?q=ai"
    })

@app.get("/api/weather")
def api_weather():
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify({"ok": False, "error": "Missing required query param: city"}), 400
    try:
        data = get_weather_for_city(city)
        return jsonify({"ok": True, "city": city, "data": data})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.get("/api/news")
def api_news():
    q = (request.args.get("q") or "ai").strip()  # default query
    try:
        api_key = os.getenv("NEWSAPI_KEY", "")
        if not api_key:
            return jsonify({
                "ok": False,
                "error": "NEWSAPI_KEY not set in environment. Create a .env with NEWSAPI_KEY or use /api/weather and /api/joke which need no key."
            }), 400
        articles = search_news(q, api_key)
        return jsonify({"ok": True, "query": q, "articles": articles})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500




@app.get("/ui")
def ui():
    # Serve the HTML UI from the static folder
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/joke")
def api_joke():
    try:
        data = get_joke()
        return jsonify({"ok": True, **data})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.get("/api/crypto")
def api_crypto():
    symbol = request.args.get("symbol", "bitcoin").strip().lower()
    vs = request.args.get("vs", "usd").strip().lower()
    try:
        data = get_price(symbol, vs)
        return jsonify({"ok": True, **data})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500
    
# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
