import requests
from bs4 import BeautifulSoup
import os
import re
from pathlib import Path

data_dir = os.environ["DATA_DIR"]
join_raw = data_dir + "/raw/" 
new_file = Path(join_raw)

all_text = []
reason_text = []

for html_file in new_file.iterdir():
    if html_file.is_file() and html_file.suffix == ".html":
        with open(html_file) as grab_text:
            soup = BeautifulSoup(grab_text, "lxml")
            for string in soup.stripped_strings:
                text_only = repr(string)
                all_text.append(text_only)
            #print(all_text)
                for site_text in all_text:
                    if site_text == "Reason for Recall":
                        reason_text.append(site_text)
            print(reason_text)
            #I'm trying to grab the paragraph below <h2>Reason for Recall</h2>
            #after that I'll send it to the API for entity extraction
            #the .json files that are returned, ill store along the .html files but it'll have .json
            #print(reason_text)
            #flag = soup.h2.string.parent
            #flag.find_next(text = True)
            #if found_all == "<h2>Reason for Recall </h2>":
            #reason_text.append(flag)
            #print(reason_text)
            #this just prints empty lists
            #figure out if i can use <h2>Reason for Recall</h2> to grab the paragraph below it
            

#if __name__ == "__main__":
    #grab_recall_reason()