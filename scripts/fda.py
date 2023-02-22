import requests
from bs4 import BeautifulSoup
import os
import re

url = "https://www.fda.gov/medical-devices/medical-device-recalls/2022-medical-device-recalls"
request = requests.get(url)
request.raise_for_status()
site = BeautifulSoup(request.text, features = "lxml")

urls = []
for link in site.find_all("a", attrs = {"href": re.compile("^/medical-devices/medical-device-recalls/")}):
    result = link.get("href")
    links = urls.append(result) #it only prints the unique ids for each url, i would need to figure out how to grab the whole link (starting with https://)
    #next: take that link then add it to data/raw/name of unique id.html


#from pathlib import Path
#cwd = Path(__file__).resolve.parent.parent
#file = os.path.join(cwd, "data/raw")


#def collect_links():


#if __name__ == "__main__":
    #collect_links()



