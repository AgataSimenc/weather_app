
from flask import Flask, render_template, request

# komunikacija med dvema strežnikoma
import requests

# Za dostop do okoljske spremeljivke (enviroment variable)
# Namesto klasične spremenljivke, uporabimo okoljsko spremeljivko, ki je shranjena v sistemu. 
# Na ta način zavarujemo/skrijemo svoj API ključ 


import os 



# API KEY: ""
# Samo za testno okolje, zamenjaj z okoljsko spremenjivko


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        mesto = request.form.get("mesto")
        # tukaj klic na API
        return render_template("index.html")

    elif request.method == "POST":

        #API klic potrebuje spodnje 3 podatke oziroma spremenljivke:
        # 1. Kraj
        city = request.form.get("city")

        # 2. Merska enota("metric" ali "imperial")
        unit = "metric"

        # 3. API ključ
        # api_key = ""
        api_key = os.environ.get("API_KEY")

        # URL za klic/zahtevek, ki vključuje zgornje 3 informacije
        url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(city, unit, api_key)

        # Klic/zahtevek > povratne informacije shranjene v spremenljivki "data"
        data = requests.get(url=url)

        print(data.json())

        return render_template("index.html", data=data.json())

if __name__ == "__main__":
    app.run()