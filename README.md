# Free Sound Effects API

A public, no-key API for searching and previewing curated free sound effects. Built for apps, games, videos, automation, and AI agents by [Lots of Sounds](https://www.lotsofsounds.com).

- **No API key** for the sample list and sample streams
- **Structured JSON** with IDs, descriptions, tags, and durations
- **CC0 sound effects** in the sample collection
- **No audio binaries** stored in this repository

Looking for a maintained **Freesound API alternative**? Start with the free sample endpoint below, then use the full Lots of Sounds API when you need catalog search, filters, and downloads.

## Quick start

```bash
curl -G "https://api.lotsofsounds.com/api/v1/sounds/sample" \
  --data-urlencode "q=door knock" \
  --data-urlencode "limit=6"
```

No account or API key is required. The response contains up to 12 curated samples:

```json
{
  "data": [
    {
      "id": "fs-133889",
      "name": "Large Wood Door Knocking",
      "description": "Knocking on a door to a large entry",
      "tags": ["door", "knocking", "wood"],
      "duration": 2.86766,
      "stream_url": "/api/v1/sounds/sample/fs-133889/stream"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 6,
    "total": 6,
    "totalPages": 1
  }
}
```

The example is abbreviated; fields and matching results can change as the curated sample set improves.

## Free endpoints

| Method | Endpoint | Authentication | Purpose |
| --- | --- | --- | --- |
| `GET` | `/api/v1/sounds/sample` | None | List or search curated samples |
| `GET` | `/api/v1/sounds/sample/{id}/stream` | None | Get a temporary stream URL |

### Search samples

Use `q` for a text query or `tags` for comma-separated tags. `limit` accepts `1` through `12`.

```bash
curl -G "https://api.lotsofsounds.com/api/v1/sounds/sample" \
  --data-urlencode "tags=door,knock" \
  --data-urlencode "limit=6"
```

### Stream a sample

Use the relative `stream_url` returned with a sound:

```bash
curl "https://api.lotsofsounds.com/api/v1/sounds/sample/fs-133889/stream"
```

This returns JSON containing a time-limited `stream_url`; it does not put an MP3 in this repository.

## JavaScript

Requires Node.js 18 or newer.

```js
const params = new URLSearchParams({ q: "notification", limit: "6" });
const response = await fetch(
  `https://api.lotsofsounds.com/api/v1/sounds/sample?${params}`,
);

if (!response.ok) {
  throw new Error(`Lots of Sounds returned HTTP ${response.status}`);
}

const { data } = await response.json();
console.log(data);
```

Run the complete dependency-free example:

```bash
node examples/javascript.mjs "notification"
```

For a typed client that also supports authenticated search, metadata, and downloads, see [`lotsofsounds/js`](https://github.com/lotsofsounds/js).

## Python

The included example uses only the Python standard library:

```bash
git clone https://github.com/lotsofsounds/free-sound-effects-api.git
cd free-sound-effects-api
python3 examples/python.py "notification"
```

Or use `requests` directly:

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

## AI agents

### Agent skill

This repository includes a dependency-free [`find-free-sound-effects` skill](skills/find-free-sound-effects/SKILL.md). Copy that directory into your agent's skills directory, or point your agent at the checked-out repository.

Example request:

> Find a short, calm notification sound for an AI assistant.

The skill searches the free endpoint, compares metadata, and requests a temporary stream URL for the selected sample.

### MCP server

Lots of Sounds also provides a hosted [Model Context Protocol server](https://www.lotsofsounds.com/docs/mcp):

```bash
claude mcp add lotsofsounds --transport http https://api.lotsofsounds.com/mcp
```

The `browse_samples` MCP tool works without authentication. Full-catalog tools require an API key:

```bash
claude mcp add lotsofsounds --transport http https://api.lotsofsounds.com/mcp \
  --header "x-api-key: $LOS_API_KEY"
```

Cursor, ChatGPT, Claude Desktop, Windsurf, and other Streamable HTTP clients can connect to the same endpoint. See the [MCP setup guide](https://www.lotsofsounds.com/docs/mcp) for client-specific configuration.

## Full API

The public samples are intentionally small and curated. The authenticated API adds:

- Natural-language catalog search
- Tags, category, duration, sorting, and pagination
- Full sound metadata
- Time-limited stream and download URLs
- Higher production limits

```bash
curl -G "https://api.lotsofsounds.com/api/v1/sounds" \
  -H "x-api-key: $LOS_API_KEY" \
  --data-urlencode "q=gentle notification chime" \
  --data-urlencode "max_duration=2"
```

[Read the API docs](https://www.lotsofsounds.com/docs), [compare plans](https://www.lotsofsounds.com/pricing), or [sign up and create an API key](https://www.lotsofsounds.com/dashboard/api-keys).

Keep API keys on the server. Do not expose `LOS_API_KEY` in browser bundles or public repositories.

## Lots of Sounds vs. the Freesound API

Both services help developers find sound effects, but this project is not a drop-in implementation of the Freesound API. Lots of Sounds provides a smaller no-key CC0 sample surface, a first-party hosted MCP server for AI agents, and an authenticated API for production search and downloads. Expect different endpoints, response shapes, catalog coverage, and account terms.

## Common questions

### Is this a free sound effects API?

Yes. The sample list and sample stream endpoints need no account and no API key. Full-catalog search and downloads require a paid Lots of Sounds plan.

### Are the sounds CC0?

The curated sample collection is CC0. For the full catalog and current usage terms, review the [Lots of Sounds license information](https://www.lotsofsounds.com/license) before publishing audio.

### Can an AI agent use this API?

Yes. The REST API returns structured JSON, the repository includes an agent skill, and the hosted MCP server exposes purpose-built sound tools.

### Does this repository contain audio files?

No. It contains documentation, small code examples, and an agent skill. Audio is served by the Lots of Sounds API.

## License

Repository code is available under the [MIT License](LICENSE). Audio returned by the API is governed separately by the [Lots of Sounds license terms](https://www.lotsofsounds.com/license).
