#!/usr/bin/env python3
import json
import sys
import urllib.parse
import urllib.request

API_URL = "https://api.lotsofsounds.com/api/v1/sounds/sample"
query = " ".join(sys.argv[1:]) or "notification"
url = f"{API_URL}?{urllib.parse.urlencode({'q': query, 'limit': 6})}"

with urllib.request.urlopen(url, timeout=20) as response:
    print(json.dumps(json.load(response), indent=2))
