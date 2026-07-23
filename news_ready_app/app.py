import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "b852327d6e1442c9af023ff388b05517"

@app.route("/")
def home():

    newspapers = [
        {"name": "Prothom Alo", "url": "https://www.prothomalo.com"},
        {"name": "Daily Star", "url": "https://www.thedailystar.net"},
        {"name": "Jugantor", "url": "https://www.jugantor.com"},
        {"name": "Kaler Kantho", "url": "https://www.kalerkantho.com"},
        {"name": "Ittefaq", "url": "https://www.ittefaq.com.bd"},
        {"name": "Somoy News", "url": "https://www.somoynews.tv"},
        {"name": "BBC", "url": "https://www.bbc.com"},
        {"name": "CNN", "url": "https://www.cnn.com"},
        {"name": "Al Jazeera", "url": "https://www.aljazeera.com"},
        {"name": "Reuters", "url": "https://www.reuters.com"},
        {"name": "The Guardian", "url": "https://www.theguardian.com"},
        {"name": "New York Times", "url": "https://www.nytimes.com"},
    ]

    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=10&apiKey={API_KEY}"
    res = requests.get(url).json()

    articles = res.get("articles", [])

    return render_template("index.html", newspapers=newspapers, articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
