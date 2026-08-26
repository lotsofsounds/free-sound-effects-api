#!/usr/bin/env python3
import argparse
import json
import urllib.parse
import urllib.request

API_ROOT = "https://api.lotsofsounds.com"
SEARCH_PATH = "/api/v1/sounds/sample"


def request_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "free-sound-effects-api/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description="Search and preview free Lots of Sounds audio.")
    search = parser.add_mutually_exclusive_group()
    search.add_argument("--query", help="Natural-language sound description")
    search.add_argument("--tags", help="Comma-separated sound tags")
    search.add_argument("--stream-id", help="Sound ID to preview")
    parser.add_argument("--limit", type=int, default=6, choices=range(1, 13))
    args = parser.parse_args()

    if args.stream_id:
        sound_id = urllib.parse.quote(args.stream_id, safe="")
        url = f"{API_ROOT}{SEARCH_PATH}/{sound_id}/stream"
    else:
        params = {"limit": args.limit}
        if args.query:
            params["q"] = args.query
        if args.tags:
            params["tags"] = args.tags
        url = f"{API_ROOT}{SEARCH_PATH}?{urllib.parse.urlencode(params)}"

    print(json.dumps(request_json(url), indent=2))


if __name__ == "__main__":
    main()
