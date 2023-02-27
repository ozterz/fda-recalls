from fda import collect_links
from entities import grab_recall_reason
from report import entity_to_csv

def main():
    collect_links()
    grab_recall_reason()
    entity_to_csv()

if __name__ == "__main__":
    main()