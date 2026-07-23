import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "b852327d6e1442c9af023ff388b05517"

@app.route("/")
def home():

    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=20&apiKey={API_KEY}"

    articles = []

    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":
            articles = data["articles"]

    except:
        pass

    return render_template("index.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
