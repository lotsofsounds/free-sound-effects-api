const API_URL = "https://api.lotsofsounds.com/api/v1/sounds/sample";
const query = process.argv.slice(2).join(" ") || "notification";
const params = new URLSearchParams({ q: query, limit: "6" });

const response = await fetch(`${API_URL}?${params}`);
if (!response.ok) {
  throw new Error(`Lots of Sounds returned HTTP ${response.status}`);
}

const body = await response.json();
console.log(JSON.stringify(body, null, 2));
