import requests
from bs4 import BeautifulSoup

url = "https://www.fda.gov/medical-devices/medical-device-recalls/2022-medical-device-recalls"
request = requests.get(url)
request.raise_for_status()
site = BeautifulSoup(request.text, features = "lxml")



