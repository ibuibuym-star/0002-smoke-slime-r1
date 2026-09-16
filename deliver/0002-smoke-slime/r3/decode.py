#!/usr/bin/env python3
"""Rebuild hero-slime.png from hero-slime.txt (64x64 RGBA)."""
from pathlib import Path
from PIL import Image

src = Path(__file__).with_name("hero-slime.txt")
lines = src.read_text().splitlines()
pal_hex = lines[0].split(",")
rows = lines[1:65]
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
pal = {ch: tuple(int(h[i:i+2], 16) for i in (1, 3, 5)) + (255,) for ch, h in zip(alphabet, pal_hex)}
im = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
px = im.load()
for y, row in enumerate(rows):
    if len(row) != 64:
        raise SystemExit(f"row {y} length {len(row)}")
    for x, ch in enumerate(row):
        if ch != "." :
            px[x, y] = pal[ch]
out = Path(__file__).with_name("hero-slime.png")
im.save(out)
print("wrote", out, "64x64")
