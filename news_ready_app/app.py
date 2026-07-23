import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "b852327d6e1442c9af023ff388b05517"

@app.route("/")
def home():

    # 🔹 YOUR EXISTING NEWSPAPER LIST (UNCHANGED)
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

    # 🔹 API NEWS (RIGHT SIDE)
    articles = []
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=20&apiKey={API_KEY}"
        res = requests.get(url)
        data = res.json()
        if data["status"] == "ok":
            articles = data["articles"]
    except:
        pass

    return render_template("index.html", newspapers=newspapers, articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
