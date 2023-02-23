import requests
from bs4 import BeautifulSoup
import os
import re
from pathlib import Path

data_dir = os.environ["DATA_DIR"]
join_raw = data_dir + "/raw/" 
new_file = Path(join_raw)

for html_file in new_file.iterdir():
    if html_file.is_file() and html_file.suffix == ".html":
        with open(html_file) as grab_text:
            soup = BeautifulSoup(grab_text, "lxml")
            soup.find_all("<h2>Reason for Recall</h2>")
            print(soup)