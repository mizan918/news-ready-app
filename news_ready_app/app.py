import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

newspapers = [
    # 🇧🇩 Bangladeshi Newspapers
    {"name": "Prothom Alo", "url": "https://www.prothomalo.com", "category": "bd"},
    {"name": "The Daily Star", "url": "https://www.thedailystar.net", "category": "bd"},
    {"name": "Kaler Kantho", "url": "https://www.kalerkantho.com", "category": "bd"},
    {"name": "Jugantor", "url": "https://www.jugantor.com", "category": "bd"},
    {"name": "Bangladesh Pratidin", "url": "https://www.bd-pratidin.com", "category": "bd"},
    {"name": "Ittefaq", "url": "https://www.ittefaq.com.bd", "category": "bd"},
    {"name": "Samakal", "url": "https://www.samakal.com", "category": "bd"},
    {"name": "Janakantha", "url": "https://www.dailyjanakantha.com", "category": "bd"},
    {"name": "Amar Desh", "url": "https://www.amardesh.com", "category": "bd"},
    {"name": "Inqilab", "url": "https://www.dailyinqilab.com", "category": "bd"},
    {"name": "Naya Diganta", "url": "https://www.dailynayadiganta.com", "category": "bd"},
    {"name": "Manab Zamin", "url": "https://mzamin.com", "category": "bd"},
    {"name": "Bhorer Kagoj", "url": "https://www.bhorerkagoj.com", "category": "bd"},
    {"name": "Dhaka Tribune", "url": "https://www.dhakatribune.com", "category": "bd"},
    {"name": "Business Standard", "url": "https://www.tbsnews.net", "category": "bd"},
    {"name": "Bangla Tribune", "url": "https://www.banglatribune.com", "category": "bd"},
    {"name": "UNB", "url": "https://www.unb.com.bd", "category": "bd"},

    # 🌍 International News
    {"name": "BBC", "url": "https://www.bbc.com", "category": "int"},
    {"name": "CNN", "url": "https://www.cnn.com", "category": "int"},
    {"name": "Al Jazeera", "url": "https://www.aljazeera.com", "category": "int"},
    {"name": "Reuters", "url": "https://www.reuters.com", "category": "int"},
    {"name": "The Guardian", "url": "https://www.theguardian.com", "category": "int"},
    {"name": "New York Times", "url": "https://www.nytimes.com", "category": "int"},
]

  # 👉 scan videos folder
    video_folder = os.path.join(app.static_folder, "videos")
    videos = []

    if os.path.exists(video_folder):
        for file in os.listdir(video_folder):
            if file.endswith(".mp4"):
                videos.append(f"/static/videos/{file}")

    # ✅ MUST pass videos
    return render_template(
        "index.html",
        newspapers=newspapers,
        videos=videos
    )


if __name__ == "__main__":
    app.run(debug=True)
