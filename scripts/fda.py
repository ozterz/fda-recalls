import requests
from bs4 import BeautifulSoup
import os
import re

url = "https://www.fda.gov/medical-devices/medical-device-recalls/2022-medical-device-recalls"
request = requests.get(url)
request.raise_for_status()
site = BeautifulSoup(request.text, features = "lxml")

#def collect_links():

urls = []
for link in site.find_all("a", attrs = {"href": re.compile("^/medical-devices/medical-device-recalls/")}):
    result = link.get("href")
    full_link = "https://www.fda.gov" + result
    urls.append(full_link)
    
    #next: take result then add it to data/raw/name of unique id.html


#from pathlib import Path
#cwd = Path(__file__).resolve.parent.parent
#file = os.path.join(cwd, "data/raw")


#if __name__ == "__main__":
    #collect_links()