import requests
from bs4 import BeautifulSoup
import os
import re
from pathlib import Path
import json
import time

def grab_recall_reason():
    data_dir = os.environ["DATA_DIR"]
    join_raw = data_dir + "/raw/" 
    new_file = Path(join_raw)

    all_text = []
    reason_text = []

    for html_file in new_file.iterdir():
        if html_file.is_file() and html_file.suffix == ".html":
            with open(html_file) as grab_text:
                soup = BeautifulSoup(grab_text, "lxml")
                h_tag = re.compile("h[0-9]")
                found = soup.find(h_tag, string = re.compile("Reason for Recall.*"))
                paragraph = ""
                print(html_file)
                for grab_all in found.next_siblings:
                    if h_tag.match(str(grab_all.name)):
                        break
                    else:
                        paragraph += grab_all.get_text()
                json_file = Path(os.path.splitext(html_file)[0] + ".json")
                reason_text.append((json_file, paragraph))
    
    CALAIS_URL = "https://api-eit.refinitiv.com/permid/calais"
    API_KEY = os.environ['OPENCALAIS_API_KEY']

    headers = {
        'charset' : "UTF-8",
        'X-AG-Access-Token' : API_KEY,
        'Content-Type' : 'text/raw',
        'outputformat' : 'application/json',
        'x-calais-selectiveTags': 'company,industry,socialtags'
    }

    for reason in reason_text:
        time.sleep(1)
        response = requests.post(
            CALAIS_URL,
            data = reason[1].encode("utf8"),
            headers = headers,
            timeout = 80
        )
            
        with open(reason[0],"w", encoding = "utf8") as out:
            if response.status_code == 200 and response.json():
                print("Writing response to {}".format(reason[0]))
                json.dump(response.json(), out, indent = 4, ensure_ascii = False)

if __name__ == '__main__':
    grab_recall_reason()