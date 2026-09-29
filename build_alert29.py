# -*- coding: utf-8 -*-
"""Tema 29 — Blue Butterfly. Card alert Saweria + Sociabuzz, CSS wajib <= 5120 byte."""
from pathlib import Path
BASE = Path(__file__).parent
RAW = 'https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/bgkupu.jpg'
KUPU = 'https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/kupu.png'
LIMIT = 5120

CSS = (
    '.bf29-card{box-sizing:border-box;position:relative;isolation:isolate;display:flex;align-items:center;justify-content:center;'
    'width:720px;max-width:100%;height:280px;margin:0 auto;border:3px solid #4FA8FF;border-radius:18px;overflow:hidden;'
    'font-family:Trebuchet MS,Segoe UI,sans-serif;color:#fff;background:#061B33;text-align:center;'
    'box-shadow:0 14px 38px rgba(3,12,26,.74),0 0 26px rgba(79,168,255,.34),inset 0 0 0 2px rgba(255,255,255,.5);'
    'animation:bf29-in .7s cubic-bezier(.2,.9,.25,1.12) both,bf29-breathe 5s ease-in-out .7s infinite}'
    '.bf29-bg{position:absolute;inset:0;z-index:0;width:100%;height:100%;object-fit:cover;pointer-events:none;'
    'filter:saturate(1.18) brightness(.52) blur(2.6px);animation:bf29-zoom 16s ease-in-out infinite alternate}'
    '.bf29-veil{position:absolute;inset:0;z-index:1;pointer-events:none;'
    'background:linear-gradient(180deg,rgba(6,27,51,.48),rgba(3,14,30,.7)),radial-gradient(circle at 50% 46%,rgba(79,168,255,.22),transparent 62%)}'
    '.bf29-k{position:absolute;z-index:4;width:196px;max-width:34%;height:auto;pointer-events:none;'
    'filter:drop-shadow(0 8px 16px rgba(2,10,22,.62));animation:bf29-flap 3.6s ease-in-out infinite}'
    '.bf29-k1{left:4px;bottom:0}'
    '.bf29-k2{right:4px;top:0;transform:rotate(180deg);animation-name:bf29-flapr}'
    '.bf29-c{position:relative;z-index:6;box-sizing:border-box;width:56%;min-width:0;padding:0 14px;'
    'display:flex;flex-direction:column;align-items:center;justify-content:center;text-shadow:0 2px 8px rgba(3,14,30,.95)}'
    '.bf29-kicker{color:#8FD0FF;font-size:11px;font-weight:800;letter-spacing:2.4px;text-transform:uppercase;'
    'text-shadow:0 2px 6px rgba(3,14,30,.95),0 0 12px rgba(79,168,255,.6);animation:bf29-rise .6s cubic-bezier(.2,.9,.3,1.2) .1s both}'
    '.bf29-amount{margin:4px 0;font-size:38px;font-weight:900;line-height:1.1;letter-spacing:1px;color:#EAF7FF;'
    'word-break:break-all;max-width:100%;text-shadow:0 3px 0 #0B2E52,0 0 22px rgba(79,168,255,.75);'
    'animation:bf29-rise .6s cubic-bezier(.2,.9,.3,1.2) .18s both,bf29-glow 3.4s ease-in-out 1s infinite}'
    '.bf29-tag{margin-top:4px;color:#7CC7FF;font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;'
    'animation:bf29-rise .6s cubic-bezier(.2,.9,.3,1.2) .26s both}'
    '.bf29-who{margin-top:4px;min-width:0;display:flex;align-items:center;justify-content:center;animation:bf29-rise .6s cubic-bezier(.2,.9,.3,1.2) .34s both}'
    '.bf29-name{min-width:0;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:27px;font-weight:900;color:#fff;'
    'text-shadow:0 2px 0 #061B33,0 2px 10px rgba(3,14,30,.95),0 0 14px rgba(191,227,255,.5)}'
    '.bf29-msg{margin-top:6px;font-size:18px;font-weight:600;line-height:1.35;color:#DCEEFF;max-width:100%;'
    'display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;animation:bf29-rise .6s cubic-bezier(.2,.9,.3,1.2) .42s both}'
    '@keyframes bf29-in{0%{opacity:0;transform:translateY(22px) scale(.94)}100%{opacity:1;transform:none}}'
    '@keyframes bf29-breathe{0%,100%{box-shadow:0 14px 38px rgba(3,12,26,.74),0 0 20px rgba(79,168,255,.22),inset 0 0 0 2px rgba(255,255,255,.42)}'
    '50%{box-shadow:0 14px 38px rgba(3,12,26,.74),0 0 34px rgba(79,168,255,.46),inset 0 0 0 2px rgba(255,255,255,.66)}}'
    '@keyframes bf29-zoom{from{transform:scale(1)}to{transform:scale(1.08) translateY(-1%)}}'
    '@keyframes bf29-rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}'
    '@keyframes bf29-glow{0%,100%{text-shadow:0 3px 0 #0B2E52,0 0 18px rgba(79,168,255,.6)}'
    '50%{text-shadow:0 3px 0 #0B2E52,0 0 32px rgba(143,208,255,.95)}}'
    '@keyframes bf29-flap{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-8px) scale(.985)}}'
    '@keyframes bf29-flapr{0%,100%{transform:rotate(180deg) translateY(0) scale(1)}50%{transform:rotate(180deg) translateY(8px) scale(.985)}}'
    '@media(prefers-reduced-motion:reduce){.bf29-card,.bf29-bg,.bf29-k,.bf29-amount,.bf29-kicker,.bf29-tag,.bf29-who,.bf29-msg{animation:none!important}}'
)

TAG = '<div class="bf29-tag">{from_text}</div>'


def build(name_token, tag_html):
    return (
        '<div class="bf29-card">'
        f'<img class="bf29-bg" src="{RAW}" alt="">'
        '<div class="bf29-veil"></div>'
        f'<img class="bf29-k bf29-k1" src="{KUPU}" alt="">'
        f'<img class="bf29-k bf29-k2" src="{KUPU}" alt="">'
        '<div class="bf29-c">'
        '<div class="bf29-kicker">MAKASIH SEMOGA MAKIN KAYA</div>'
        '<div class="bf29-amount">{amount}</div>'
        f'{tag_html}'
        f'<div class="bf29-who"><span class="bf29-name">{name_token}</span></div>'
        '<div class="bf29-msg">{message}</div>'
        '</div>'
        '</div>'
    )


for slug, name_token, tag_html in (
    ("sociabuzz", "{supporter}", TAG),
    ("saweria", "{donator}", ""),
):
    html = build(name_token, tag_html)
    (BASE / f"{slug}-alert.html").write_text(html, encoding="utf-8")
    (BASE / f"{slug}-alert.css").write_text(CSS, encoding="utf-8")
    print(slug, "html", len(html.encode()), "css", len(CSS.encode()))

# guard: CSS <= 5KB, HTML satu baris tanpa style inline
assert len(CSS.encode()) <= LIMIT, f"CSS {len(CSS.encode())}B > {LIMIT}B"
assert CSS.count("{") == CSS.count("}"), "brace imbalance in CSS"
for slug in ("sociabuzz", "saweria"):
    h = (BASE / f"{slug}-alert.html").read_text(encoding="utf-8")
    assert "\n" not in h and "  " not in h, f"{slug} html formatting"
    assert "<style" not in h and 'style="' not in h, f"{slug} inline style"
    for tok in ("{amount}", "{message}"):
        assert tok in h, f"{slug} missing {tok}"
assert "{supporter}" in (BASE / "sociabuzz-alert.html").read_text(encoding="utf-8")
assert "{from_text}" in (BASE / "sociabuzz-alert.html").read_text(encoding="utf-8")
assert "{donator}" in (BASE / "saweria-alert.html").read_text(encoding="utf-8")
print("OK css", len(CSS.encode()), "<=", LIMIT)
