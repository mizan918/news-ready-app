import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "b852327d6e1442c9af023ff388b05517"

@app.route("/")
def home():
    source = request.args.get("source")

    # ✅ YOUR FULL NEWSPAPER LIST (UNCHANGED)
    newspapers = [
        {"name": "Prothom Alo", "url": "https://www.prothomalo.com", "category": "bd"},
        {"name": "Daily Star", "url": "https://www.thedailystar.net", "category": "bd", "source": "bbc-news"},
        {"name": "Jugantor", "url": "https://www.jugantor.com", "category": "bd"},
        {"name": "Kaler Kantho", "url": "https://www.kalerkantho.com", "category": "bd"},
        {"name": "Ittefaq", "url": "https://www.ittefaq.com.bd", "category": "bd"},
        {"name": "Somoy News", "url": "https://www.somoynews.tv", "category": "bd"},
        {"name": "BBC", "url": "https://www.bbc.com", "category": "int", "source": "bbc-news"},
        {"name": "CNN", "url": "https://www.cnn.com", "category": "int", "source": "cnn"},
        {"name": "Al Jazeera", "url": "https://www.aljazeera.com", "category": "int", "source": "al-jazeera-english"},
        {"name": "Reuters", "url": "https://www.reuters.com", "category": "int", "source": "reuters"},
    ]

    # ✅ API FETCH
    if source:
        url = f"https://newsapi.org/v2/top-headlines?sources={source}&apiKey={API_KEY}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url).json()

    news = []
    for a in response.get("articles", []):
        news.append({
            "title": a.get("title"),
            "desc": a.get("description"),
            "image": a.get("urlToImage"),
            "link": a.get("url")
        })

    # ✅ VIDEO AUTO LOAD
    video_folder = os.path.join(app.static_folder, "videos")
    videos = []

    if os.path.exists(video_folder):
        for file in os.listdir(video_folder):
            if file.endswith(".mp4"):
                videos.append(f"/static/videos/{file}")

    return render_template(
        "index.html",
        newspapers=newspapers,
        news=news,
        videos=videos
    )


if __name__ == "__main__":
    app.run(debug=True)
