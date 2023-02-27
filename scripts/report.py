import json
import csv
import os
from pathlib import Path

def entity_to_csv():
  data_dir = os.environ["DATA_DIR"]
  join_raw = data_dir + "/raw/" 
  join_done = data_dir + "/processed/fda_tags.csv"
  search_file = Path(join_raw)
  csv_file = Path(join_done)

  entities = []

  with open(csv_file, "w", newline = "") as data_plop:
    writer = csv.writer(data_plop)
    writer.writerow(["entity", "source_file"])
      
  for json_file in search_file.iterdir():
          if json_file.is_file() and json_file.suffix == ".json":
              with open(json_file, "r") as read_text:
                entity_data = json.load(read_text)
                key = list(entity_data)[2]
                entities = entity_data[key]["name"]
                      
                with open(csv_file, "a", newline = "") as data_dump:
                  writer = csv.writer(data_dump)
                  writer.writerow([entities,json_file.name])

if __name__ == '__main__':
   entity_to_csv()