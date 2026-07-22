import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "b852327d6e1442c9af023ff388b05517"

@app.route("/")
def home():

    # ✅ FULL NEWSPAPER LIST (UNCHANGED)
    newspapers = [
        {"name": "Prothom Alo", "url": "https://www.prothomalo.com", "category": "bd"},
        {"name": "Daily Star", "url": "https://www.thedailystar.net", "category": "bd"},
        {"name": "Jugantor", "url": "https://www.jugantor.com", "category": "bd"},
        {"name": "Kaler Kantho", "url": "https://www.kalerkantho.com", "category": "bd"},
        {"name": "Ittefaq", "url": "https://www.ittefaq.com.bd", "category": "bd"},
        {"name": "Somoy News", "url": "https://www.somoynews.tv", "category": "bd"},
        {"name": "BBC", "url": "https://www.bbc.com", "category": "int"},
        {"name": "CNN", "url": "https://www.cnn.com", "category": "int"},
        {"name": "Al Jazeera", "url": "https://www.aljazeera.com", "category": "int"},
        {"name": "Reuters", "url": "https://www.reuters.com", "category": "int"},
        {"name": "The Guardian", "url": "https://www.theguardian.com", "category": "int"},
        {"name": "New York Times", "url": "https://www.nytimes.com", "category": "int"},
    ]

    # ✅ API NEWS
    news = []
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=12&apiKey={API_KEY}"
        res = requests.get(url, timeout=5)
        data = res.json()

        if data.get("status") == "ok":
            for a in data.get("articles", []):
                news.append({
                    "title": a.get("title"),
                    "desc": a.get("description") or "No description",
                    "image": a.get("urlToImage"),
                    "link": a.get("url")
                })
    except Exception as e:
        print("API ERROR:", e)

    if not news:
        news = [{
            "title": "No news available",
            "desc": "Check API or internet",
            "image": None,
            "link": "#"
        }]

    # ✅ VIDEO AUTO LOAD
    video_folder = os.path.join(app.static_folder, "videos")
    videos = []

    if os.path.exists(video_folder):
        for f in os.listdir(video_folder):
            if f.endswith(".mp4"):
                videos.append(f"/static/videos/{f}")

    return render_template(
        "index.html",
        newspapers=newspapers,
        news=news,
        videos=videos
    )

if __name__ == "__main__":
    app.run(debug=True)
