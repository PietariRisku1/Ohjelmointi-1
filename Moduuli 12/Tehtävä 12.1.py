import requests
import json

pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])
    else:
        print("Virhe: palvelin vastasi koodilla", vastaus.status_code)
except requests.exceptions.RequestException as e:
    print("Vitsin hakeminen epäonnistui.")
