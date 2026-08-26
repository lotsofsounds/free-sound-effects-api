# Free Sound Effects API

Search and stream free sound effects for apps, games, videos, websites, and AI agents. No API key is required.

This public API is powered by [Lots of Sounds](https://www.lotsofsounds.com), a developer-first sound effects API for royalty-free audio.

## Try the free API

Search by a clear keyword:

```bash
curl -G "https://api.lotsofsounds.com/api/v1/sounds/sample" \
  --data-urlencode "q=notification" \
  --data-urlencode "limit=6"
```

Search by tags:

```bash
curl -G "https://api.lotsofsounds.com/api/v1/sounds/sample" \
  --data-urlencode "tags=door,creak" \
  --data-urlencode "limit=6"
```

The endpoint returns sound names, descriptions, tags, durations, IDs, and stream paths. It returns up to 12 results.

## Stream a free sound

Use the `stream_url` from a search result:

```bash
curl "https://api.lotsofsounds.com/api/v1/sounds/sample/SOUND_ID/stream"
```

The response contains a temporary audio URL that you can play or preview.

## JavaScript

```js
const query = new URLSearchParams({ q: "notification", limit: "6" });
const response = await fetch(
  `https://api.lotsofsounds.com/api/v1/sounds/sample?${query}`,
);
const { data } = await response.json();

console.log(data);
```

Run the complete example:

```bash
node examples/javascript.mjs "notification"
```

## Python

```python
import requests

response = requests.get(
    "https://api.lotsofsounds.com/api/v1/sounds/sample",
    params={"q": "notification", "limit": 6},
    timeout=20,
)
response.raise_for_status()
print(response.json()["data"])
```

Run the dependency-free example:

```bash
python3 examples/python.py "notification"
```

## AI agent skill

This repository includes an installable [`find-free-sound-effects` skill](skills/find-free-sound-effects/SKILL.md). It helps an AI coding agent search the free endpoint, compare results, and get a stream URL.

Example request:

> Find a short, calm notification sound for an AI assistant.

## Free API and full API

The free endpoint is useful for prototypes, previews, examples, and AI-agent tests. It needs no account or API key.

Use the [full Lots of Sounds API](https://www.lotsofsounds.com/docs) when you need:

- More results and pagination
- Category and duration filters
- Full sound metadata
- Download URLs
- Production API limits
- The [Lots of Sounds MCP server](https://www.lotsofsounds.com/docs/mcp)

[View the full sound library](https://www.lotsofsounds.com/sounds) or [compare API plans](https://www.lotsofsounds.com/pricing).

## Common questions

### Is this a free sound effects API?

Yes. The sample search and stream endpoints need no API key. The full Lots of Sounds API has paid plans for advanced search and download features.

### Can an AI agent use this API?

Yes. The API returns structured JSON. An agent can choose useful search keywords, inspect the results, and request a temporary stream URL.

### Can I use it for game and app sound effects?

Yes. Search for UI clicks, notifications, impacts, doors, ambience, weather, transitions, and other sound effects. Review the [Lots of Sounds license information](https://www.lotsofsounds.com/license) before you publish audio.

### Does this repository contain audio files?

No. It contains examples and an agent skill. Audio is served by the Lots of Sounds API, so the repository stays small.

## License

The code in this repository uses the [MIT License](LICENSE). Audio returned by the API has separate [Lots of Sounds license terms](https://www.lotsofsounds.com/license).
