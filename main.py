# Simple IDS/IDR log parser
import json
from pprint import pprint

# Handling suricata log alerts (eve.json) just for now
def main():
    with open("./logs/eve.json") as data:
        log = json.load(data)
        if "alert" in log:
            pprint(log)

main()
