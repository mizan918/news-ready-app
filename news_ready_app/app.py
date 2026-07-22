import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "b852327d6e1442c9af023ff388b05517"

@app.route("/")
def home():

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

    news = []

    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=10&apiKey={API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") == "ok":
            for article in data.get("articles", []):
                if article.get("title"):
                    news.append({
                        "title": article.get("title", "No title"),
                        "desc": article.get("description", "No description"),
                        "image": article.get("urlToImage"),
                        "link": article.get("url")
                    })

    except Exception as e:
        print("API ERROR:", e)

    # 👉 VERY IMPORTANT (prevents blank page)
    if not news:
        news = [{
            "title": "No news available (API issue)",
            "desc": "Check API key or internet connection",
            "image": None,
            "link": "#"
        }]

    # videos (unchanged)
    video_folder = os.path.join(app.static_folder, "videos")
    videos = []

    if os.path.exists(video_folder):
        for file in os.listdir(video_folder):
            if file.endswith(".mp4"):
                videos.append(f"/static/videos/{file}")

    return render_template(
        "index.html",
        newspapers=newspapers,
        videos=videos,
        news=news
    )


if __name__ == "__main__":
    app.run(debug=True)
