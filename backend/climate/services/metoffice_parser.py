import requests

MONTHS = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
SEASONS = ["winter","spring","summer","autumn"]

def parse_value(val):
    return None if val == "---" else float(val)

def fetch_and_parse(url):
    text = requests.get(url).text.splitlines()
    data = []
    started = False

    for line in text:
        if line.lower().startswith("year"):
            started = True
            continue
        if not started or not line.strip():
            continue

        parts = line.split()
        year = int(parts[0])

        data.append({
            "year": year,
            "monthly": dict(zip(MONTHS, map(parse_value, parts[1:13]))),
            "seasonal": dict(zip(SEASONS, map(parse_value, parts[13:17]))),
            "annual": parse_value(parts[17])
        })

    return data
