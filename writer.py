import json
from config import OUTPUT_FILE
def save_json(data):
    with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
    print(f"\nSaved:{OUTPUT_FILE}")