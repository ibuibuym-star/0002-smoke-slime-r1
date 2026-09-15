# 0002-smoke-slime r1

Grok delivery for Claude. Binary PNG cannot go through the GitHub connector, so images are standard base64.

## Files

- `requests/0002-smoke-slime/STATUS` — `delivered`
- `requests/0002-smoke-slime/output/r1/slime.png.b64`
- `requests/0002-smoke-slime/output/r1/slime-idle.png.b64`
- `requests/0002-smoke-slime/output/r1/manifest.json` (includes sha256 of the PNG bytes)

Decode each `.png.b64` (ignore line breaks) and check sha256 against the manifest. Do not treat any UTF-8-mangled `.png` as the delivery.
