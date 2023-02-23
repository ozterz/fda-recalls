import requests
from bs4 import BeautifulSoup
import os
import re
from pathlib import Path

def collect_links():

    url = "https://www.fda.gov/medical-devices/medical-device-recalls/2022-medical-device-recalls"
    request = requests.get(url)
    request.raise_for_status()
    site = BeautifulSoup(request.text, features = "lxml")

    urls = []

    for link in site.find_all("a", attrs = {"href": re.compile("^/medical-devices/medical-device-recalls/")}):
        result = link.get("href")
        full_link = "https://www.fda.gov" + result
        urls.append((full_link, result.replace("/medical-devices/medical-device-recalls/", "")))

    for route in urls:
        cwd = Path(__file__).parents[1]
        data_dir = "data/raw/"
        html_link = data_dir + route[1] + ".html"
        new_file = os.path.join(cwd, Path(html_link))
        with open (new_file, "w") as saved_file:
            grab_text = requests.get(route[0]).text
            saved_file.write(grab_text)

if __name__ == "__main__":
    collect_links()