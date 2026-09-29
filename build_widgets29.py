# -*- coding: utf-8 -*-
"""Tema 29 — Blue Butterfly. Widget generator: skin ulang output tema 28 (sudah hardening OBS) ke palet kupu biru."""
from pathlib import Path
import re

BASE = Path(__file__).parent
SRC = BASE.parent / "28-spongebob-bikini-bottom" / "widgets"
DST = BASE / "widgets"
DST.mkdir(exist_ok=True)
RAW_BG = "https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/bgkupu.jpg"
RAW_KUPU = "https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/kupu.png"

# Palet kupu biru: biru laut #4FA8FF, biru tua #2E7DFF, navy #061B33, langit #9FD4FF, krem→pucat biru #EAF6FF.
SWAPS = [
    # artwork
    ("https://raw.githubusercontent.com/MasAjie12/spongebob-alert-assets/main/spongebobbg.jpg", RAW_BG),
    ("https://raw.githubusercontent.com/MasAjie12/spongebob-alert-assets/main/spongebobkiri-nobg.png", RAW_KUPU),
    # hex
    ("#FFF8EC", "#EAF6FF"), ("#FFD93D", "#4FA8FF"), ("#FFE600", "#9FD4FF"),
    ("#FFE4B5", "#BFE3FF"), ("#E64545", "#2E7DFF"), ("#0A6E8C", "#1E5FA8"),
    ("#0B3049", "#0A2C52"), ("#04101A", "#03101E"), ("#10314A", "#0B2E52"),
    ("#8B4513", "#0B2E52"), ("#8B2A00", "#0B2E52"), ("#061E2A", "#04182E"),
    # hex ter-encode di badge SVG
    ("%23E64545", "%232E7DFF"), ("%23FFD93D", "%234FA8FF"), ("%230A6E8C", "%231E5FA8"),
    # rgb triplet (kompak + berspasi)
    ("255,217,61", "79,168,255"), ("255, 217, 61", "79, 168, 255"),
    ("230,69,69", "46,125,255"), ("230, 69, 69", "46, 125, 255"),
    ("10,110,140", "30,95,168"),
    ("10,58,82", "10,44,82"), ("6,30,42", "4,24,48"), ("6,17,38", "4,16,36"),
    ("4,16,28", "3,14,30"), ("4, 16, 28", "3, 14, 30"),
    ("16,49,74", "11,46,82"),
    ("255,105,180", "124,107,255"), ("135,206,250", "191,227,255"),
    ("255,248,231", "234,246,255"), ("255,244,214", "214,238,255"),
    # teks/emoji dekorasi
    ("🪣", "🦋"), ("\U0001fabc", "🦋"), ("🫧", "✨"),
    ("KRUSTY KRAB LEADERBOARD", "BLUE BUTTERFLY LEADERBOARD"),
    ("BIKINI BOTTOM badge on every widget card", "BLUE BUTTERFLY badge on every widget card"),
    ("BIKINI %3C/tspan", "BLUE %3C/tspan"),
    ("%3EBOTTOM%3C/tspan", "%3EBUTTERFLY%3C/tspan"),
    ("SpongeBob Bikini Bottom Theme (t28", "Blue Butterfly Theme (t29"),
    ("Krusty Krab stripe", "butterfly stripe"), ("Krusty Krab", "Butterfly"),
    ("SpongeBob", "Blue Butterfly"),
    # prefix kelas + komentar tema
    ("sb28-", "bf29-"), ("t28", "t29"),
]
LEFTOVER = ["spongebob", "#FFD93D", "#E64545", "#0A6E8C", "#FFF8EC", "#8B2A00",
            "sb28-", "t28", "🪣", "SpongeBob", "BIKINI", "%3EBOTTOM", "KRUSTY"]


def transform(text):
    for old, new in SWAPS:
        text = text.replace(old, new)
    return text


for src in sorted(SRC.glob("*.css")):
    text = transform(src.read_text(encoding="utf-8"))
    (DST / src.name).write_text(text, encoding="utf-8")
    bad = [w for w in LEFTOVER if w in text]
    assert not bad, f"{src.name}: sisa {bad}"
    print("widget", src.name, len(text.encode()))

# alert pakai prefix bf29 juga — pastikan tak ada nama class/keyframe yang tabrakan
ALERT_NAMES = ["bf29-card", "bf29-bg", "bf29-veil", "bf29-k", "bf29-k1", "bf29-k2", "bf29-c",
               "bf29-kicker", "bf29-amount", "bf29-tag", "bf29-who", "bf29-name", "bf29-msg",
               "bf29-in", "bf29-breathe", "bf29-zoom", "bf29-rise", "bf29-glow", "bf29-flap", "bf29-flapr"]
pat = re.compile("|".join(re.escape(n) + r"(?![-a-z0-9])" for n in ALERT_NAMES))
hits = set()
for f in DST.glob("*.css"):
    t = f.read_text(encoding="utf-8")
    for m in pat.findall(t):
        hits.add((f.name, m))
print("collision:", sorted(hits) or "none")
assert not hits, f"alert/widget class collision: {sorted(hits)}"
print("OK widgets", len(list(DST.glob('*.css'))))
