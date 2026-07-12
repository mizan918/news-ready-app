from flask import Flask, render_template

app = Flask(__name__)

newspapers = [
    {"name": "Prothom Alo", "url": "https://www.prothomalo.com"},
    {"name": "Daily Star", "url": "https://www.thedailystar.net"},
    {"name": "BBC", "url": "https://www.bbc.com"},
    {"name": "CNN", "url": "https://www.cnn.com"},
    {"name": "Al Jazeera", "url": "https://www.aljazeera.com"},
    {"name": "The Guardian", "url": "https://www.theguardian.com"},
    {"name": "New York Times", "url": "https://www.nytimes.com"},
    {"name": "Reuters", "url": "https://www.reuters.com"},
    {"name": "Jugantor", "url": "https://www.jugantor.com"},
    {"name": "Kaler Kantho", "url": "https://www.kalerkantho.com"},
]

@app.route("/")
def home():
    return render_template("index.html", newspapers=newspapers)

if __name__ == "__main__":
    app.run()