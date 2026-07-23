import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    newspapers = [
        {"name": "Prothom Alo", "url": "https://www.prothomalo.com", "category": "bd"},       
        {"name": "Jugantor", "url": "https://www.jugantor.com", "category": "bd"},
        {"name": "Kaler Kantho", "url": "https://www.kalerkantho.com", "category": "bd"},      
        {"name": "Somoy News", "url": "https://www.somoynews.tv", "category": "bd"},

        {"name": "BBC", "url": "https://www.bbc.com", "category": "int"},
        {"name": "CNN", "url": "https://www.cnn.com", "category": "int"},
        {"name": "Al Jazeera", "url": "https://www.aljazeera.com", "category": "int"},
        {"name": "Reuters", "url": "https://www.reuters.com", "category": "int"},
    ]

    return render_template("index.html", newspapers=newspapers)


if __name__ == "__main__":
    app.run(debug=True)
