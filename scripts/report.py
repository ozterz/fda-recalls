import json
import csv
import os
from pathlib import Path

data_dir = os.environ["DATA_DIR"]
join_raw = data_dir + "/raw/" 
join_done = data_dir + "/processed/fda_tags.csv"
search_file = Path(join_raw)
csv_file = Path(join_done)

entities = []

for json_file in search_file.iterdir():
        if json_file.is_file() and json_file.suffix == ".json":
            with open(json_file, "r") as read_text:
                    entity_data = json.load(read_text)
                    print(entity_data[2]["name"])
                 
                  #grab social tage name (3rd dictionary in dictionary of dicts)
                    #with open(csv_file, "w", newline = "") as data_dump:
                        #writer =  csv.writer(data_dump)
                        #writer.writerow(["entity", "source_file"])
                        #writer.writerows(entities)
                  
                  