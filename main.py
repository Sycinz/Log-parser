# Simple IDS/IDR log parser
import json

# Handling suricata log alerts (eve.json)
def suricata_logs(log_entry):
    params = ["timestamp", "src_ip", "src_port", "dest_ip", "dest_port"]
    
    if log_entry["event_type"] in ["flow", "stats", "alert"]:
            output = "\n".join(f'{ param }: { log_entry.get(param, "---") }' for param in params)
            print(output, end="\n\n")
 
def main():
    with open("./logs/eve.json", 'r') as data:
        for line in data:
            try:
                log_entry = json.loads(line)
            except json.JSONDecodeError:
               continue
               
            suricata_logs(log_entry)
main()