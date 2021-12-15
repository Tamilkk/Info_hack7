import json, phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate
from urllib.request import urlopen

number = input("Enter the number with region code: ")
numbers = phonenumbers.parse(number)
url = "https://ipinfo.io/"

def analyzer():
    description = geocoder.description_for_number(numbers, "en")
    supplier = carrier.name_for_number(numbers, "en")
    response = urlopen(url)
    data = json.load(response)
    return [description, supplier, data]

def parse_data():
    country, supplier, device = analyzer()
    region = device["region"]
    city = device["city"]
    lat, lon = str(device["loc"]).split(",")
    location = f"Latitude: {lat}, Longtitude: {lon}"
    postal = device["postal"]
    timezone = device["timezone"]
    server = device["org"]
    ip = device["ip"]
    datas = [["Country", country], ["Region", region], ["city", city], ["Location", location],
             ["Postal", postal], ["Timezone", timezone], ["Server", server],
             ["Supplier", supplier], ["IP", ip]]
    print(*datas, sep="\n")

parse_data()