import re

def extract_total(text: str):
    match = re.search(r'סה["\']?כ.*?(\d+\.\d{2})', text)
    if match:
        return float(match.group(1))
    return None
