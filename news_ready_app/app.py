from flask import Flask, render_template

app = Flask(__name__)

newspapers = [
# 🇧🇩 Bangladeshi Newspapers
{"name": "Prothom Alo", "url": "https://www.prothomalo.com"},
{"name": "The Daily Star", "url": "https://www.thedailystar.net"},
{"name": "Kaler Kantho", "url": "https://www.kalerkantho.com"},
{"name": "Jugantor", "url": "https://www.jugantor.com"},
{"name": "Bangladesh Pratidin", "url": "https://www.bd-pratidin.com"},
{"name": "Ittefaq", "url": "https://www.ittefaq.com.bd"},
{"name": "Samakal", "url": "https://www.samakal.com"},
{"name": "Janakantha", "url": "https://www.dailyjanakantha.com"},
{"name": "Amar Desh", "url": "https://www.amardesh.com"},
{"name": "Inqilab", "url": "https://www.dailyinqilab.com"},
{"name": "Naya Diganta", "url": "https://www.dailynayadiganta.com"},
{"name": "Manab Zamin", "url": "https://mzamin.com"},
{"name": "Bhorer Kagoj", "url": "https://www.bhorerkagoj.com"},
{"name": "Dhaka Tribune", "url": "https://www.dhakatribune.com"},
{"name": "Business Standard", "url": "https://www.tbsnews.net"},
{"name": "Bangla Tribune", "url": "https://www.banglatribune.com"},
{"name": "UNB", "url": "https://www.unb.com.bd"},

```
# 🌍 International (selected)
{"name": "BBC", "url": "https://www.bbc.com"},
{"name": "CNN", "url": "https://www.cnn.com"},
{"name": "Al Jazeera", "url": "https://www.aljazeera.com"},
{"name": "Reuters", "url": "https://www.reuters.com"},
{"name": "The Guardian", "url": "https://www.theguardian.com"},
{"name": "New York Times", "url": "https://www.nytimes.com"},
```

]


@app.route("/")
def home():
    return render_template("index.html", newspapers=newspapers)

if __name__ == "__main__":
    app.run()
