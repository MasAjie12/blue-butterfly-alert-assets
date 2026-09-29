# -*- coding: utf-8 -*-
"""Generate responsive theme 29 (Blue Butterfly) preview from production alert/widget files."""
from pathlib import Path
import json, re

BASE = Path(__file__).parent
W = BASE / "widgets"
OUT = BASE / "preview-blue-butterfly.html"
RAW = "https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/bgkupu.jpg"
KUPU = "https://raw.githubusercontent.com/MasAjie12/blue-butterfly-alert-assets/main/kupu.png"

def strip_style(text):
    return re.sub(r"<style>.*?</style>", "", text, flags=re.S).strip()

def dummy(text, sb):
    text = text.replace("{amount}", "IDR 1.000.000")
    text = text.replace("{message}", "Makasih banyak supportnya, I'm ready!")
    text = text.replace("{supporter}", "AuliaBunga" if sb else "{supporter}")
    text = text.replace("{from_text}", "dari Instagram" if sb else "{from_text}")
    text = text.replace("{donator}", "MasAjiSquad")
    return text

def read_css(name, rescope=None):
    text = (W / name).read_text(encoding="utf-8")
    text = re.sub(r"(?:html\s*,\s*)?body\s*\{[^}]*overflow[^}]*hidden[^}]*\}", "", text, flags=re.I)
    return text.replace(rescope[0], rescope[1]) if rescope else text

SB_ALERT = dummy(strip_style((BASE / "sociabuzz-alert.html").read_text(encoding="utf-8")), True)
SW_ALERT = dummy(strip_style((BASE / "saweria-alert.html").read_text(encoding="utf-8")), False)
assert "{amount}" not in SB_ALERT and "{supporter}" not in SB_ALERT and "{donator}" not in SW_ALERT

CSS_ALERT = (BASE / "sociabuzz-alert.css").read_text(encoding="utf-8")

sb_files = ["sociabuzz-top-donator.css", "sociabuzz-milestone.css",
            "sociabuzz-subathon.css", "sociabuzz-queue.css",
            "sociabuzz-top-donator-runningtext.css"]
SB_CSS = "\n".join(read_css(n) for n in sb_files)
SW_CSS = "\n".join(read_css(n).replace("#__next > div", ".sw-root") for n in [
    "saweria-top-donator.css", "saweria-milestone.css", "saweria-subathon.css"
])
SW_CSS += "\n" + read_css("saweria-top-donator.css").replace("#__next > div", "#sw-top").replace(".sw-root", "#sw-top").replace(".w-top ", "#sw-top ")

HTML = f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Preview Tema 29 — Blue Butterfly</title>
<style>
html,body{{margin:0;padding:0;background:#0d1117;color:#c9d1d9;font-family:Segoe UI,Trebuchet MS,sans-serif}}
body{{padding:24px 16px 60px}}
h1{{text-align:center;font-weight:900;margin:0 0 6px;font-size:28px;letter-spacing:1px}}
.sub{{text-align:center;color:#8b949e;font-size:13px;margin-bottom:28px}}
.section{{margin:0 auto 32px;max-width:980px}}
.section h2{{font-size:14px;text-transform:uppercase;letter-spacing:1.4px;color:#58a6ff;margin:0 0 10px;border-left:3px solid #58a6ff;padding-left:10px}}
.section h2 small{{font-weight:400;color:#8b949e;text-transform:none;letter-spacing:0}}
.alert-wrap{{display:flex;flex-wrap:wrap;gap:18px;justify-content:center;margin-bottom:10px}}
.alert-box{{flex:1 1 420px;max-width:760px}}
.widget-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}}
.widget-box{{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:14px}}
.widget-box h3{{margin:0 0 8px;font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:#8b949e}}
.widget-box iframe{{width:100%;height:220px;border:0;border-radius:6px;background:#0d1117}}
.widget-box.running iframe{{height:60px}}
.widget-box.mediashare iframe{{height:260px}}
pre{{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:12px;font-size:11px;overflow:auto;white-space:pre-wrap;word-break:break-all;color:#c9d1d9}}
.copy{{display:inline-block;margin-top:6px;padding:5px 10px;border:1px solid #30363d;border-radius:6px;background:#21262d;color:#c9d1d9;font-size:11px;cursor:pointer}}
.copy:hover{{background:#30363d}}
.tabs{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}}
.tab{{padding:5px 10px;border-radius:6px;background:#21262d;border:1px solid #30363d;font-size:12px;cursor:pointer}}
.tab.active{{background:#1f6feb;color:#fff;border-color:#1f6feb}}
.tab-content{{display:none}}
.tab-content.active{{display:block}}
{CSS_ALERT}
{SB_CSS}
{SW_CSS}
</style>
</head>
<body>
<h1>🦋 Blue Butterfly Theme (t29)</h1>
<p class="sub">Preview lengkap alert + widget Saweria &amp; Sociabuzz</p>

<div class="section">
<h2>Alert Card <small>— CSS inline di preview, produksi pakai file terpisah</small></h2>
<div class="alert-wrap">
<div class="alert-box">
<h3 style="margin:0 0 8px;font-size:12px;color:#8b949e">Sociabuzz</h3>
{SB_ALERT}
</div>
<div class="alert-box">
<h3 style="margin:0 0 8px;font-size:12px;color:#8b949e">Saweria</h3>
{SW_ALERT}
</div>
</div>
</div>

<div class="section">
<h2>Widget Sociabuzz</h2>
<div class="widget-grid">
<div class="widget-box"><h3>Top Donator</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('sociabuzz-top-donator.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='w-top'>&lt;div class='card'>&lt;div class='card-header'>&lt;h4>Top Donator&lt;/h4>&lt;/div>&lt;table class='show_donate'>&lt;tr>&lt;td>1&lt;/td>&lt;td>&lt;span class='text-limit'>AuliaBunga&lt;/span>&lt;/td>&lt;td>&lt;span class='text-limit-r'>Rp 500.000&lt;/span>&lt;/td>&lt;/tr>&lt;tr>&lt;td>2&lt;/td>&lt;td>&lt;span class='text-limit'>MasAjiSquad&lt;/span>&lt;/td>&lt;td>&lt;span class='text-limit-r'>Rp 250.000&lt;/span>&lt;/td>&lt;/tr>&lt;/table>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box"><h3>Milestone</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('sociabuzz-milestone.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='w-mile'>&lt;div class='card'>&lt;div class='card-header'>&lt;h4>Target Donasi&lt;/h4>&lt;/div>&lt;div class='progress-bar' style='width:65%'>&lt;/div>&lt;div class='progress-text'>Rp 650.000 / Rp 1.000.000&lt;/div>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box"><h3>Subathon</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('sociabuzz-subathon.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='w-sub'>&lt;div class='subathon-container'>&lt;div class='sub_judul'>&lt;strong>Subathon Timer&lt;/strong>&lt;/div>&lt;div class='sub_timer'>02:34:56&lt;/div>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box"><h3>Queue</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('sociabuzz-queue.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='w-queue'>&lt;div class='card'>&lt;div class='card-header'>&lt;h4>Antrian&lt;/h4>&lt;/div>&lt;table class='show_donate'>&lt;tr>&lt;td>1&lt;/td>&lt;td>&lt;span class='text-limit'>User123&lt;/span>&lt;/td>&lt;/tr>&lt;/table>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box running"><h3>Running Text</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('sociabuzz-top-donator-runningtext.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='custom-font'>&lt;marquee class='text-center' scrollamount='5'>&lt;strong>SULTAN SAWER&lt;/strong> &lt;strong>AuliaBunga&lt;/strong> Rp 500.000 · &lt;strong>MasAjiSquad&lt;/strong> Rp 250.000&lt;/marquee>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box mediashare"><h3>MediaShare</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('sociabuzz-mediashare.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div id='ms_container'>&lt;div class='text-container'>&lt;span class='text-title'>Judul Lagu&lt;/span>&lt;span class='text-requester'>Requested by AuliaBunga&lt;/span>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
</div>
</div>

<div class="section">
<h2>Widget Saweria</h2>
<div class="widget-grid">
<div class="widget-box"><h3>Top Donator</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('saweria-top-donator.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='sw-root'>&lt;div class='w-top'>&lt;div class='card'>&lt;div class='card-header'>&lt;h4>Top Donator&lt;/h4>&lt;/div>&lt;table class='show_donate'>&lt;tr>&lt;td>1&lt;/td>&lt;td>&lt;span class='text-limit'>MasAjiSquad&lt;/span>&lt;/td>&lt;td>&lt;span class='text-limit-r'>Rp 750.000&lt;/span>&lt;/td>&lt;/tr>&lt;/table>&lt;/div>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box"><h3>Milestone</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('saweria-milestone.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='sw-root'>&lt;div class='w-mile'>&lt;div class='card'>&lt;div class='card-header'>&lt;h4>Target Donasi&lt;/h4>&lt;/div>&lt;div class='progress-bar' style='width:75%'>&lt;/div>&lt;div class='progress-text'>Rp 750.000 / Rp 1.000.000&lt;/div>&lt;/div>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box"><h3>Subathon</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('saweria-subathon.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div class='sw-root'>&lt;div class='w-sub'>&lt;div class='subathon-container'>&lt;div class='sub_judul'>&lt;strong>Subathon Timer&lt;/strong>&lt;/div>&lt;div class='sub_timer'>01:45:22&lt;/div>&lt;/div>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
<div class="widget-box mediashare"><h3>MediaShare</h3><iframe srcdoc="&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;style>{read_css('saweria-mediashare.css').replace(chr(34),chr(39))}&lt;/style>&lt;/head>&lt;body>&lt;div id='ms_container'>&lt;div class='text-container'>&lt;span class='text-title'>Judul Lagu&lt;/span>&lt;span class='text-requester'>Requested by MasAjiSquad&lt;/span>&lt;/div>&lt;/div>&lt;/body>&lt;/html>"></iframe></div>
</div>
</div>

<div class="section">
<h2>File Produksi</h2>
<div class="tabs">
<span class="tab active" onclick="showTab('sb-html')">sociabuzz-alert.html</span>
<span class="tab" onclick="showTab('sb-css')">sociabuzz-alert.css</span>
<span class="tab" onclick="showTab('sw-html')">saweria-alert.html</span>
<span class="tab" onclick="showTab('sw-css')">saweria-alert.css</span>
</div>
<div id="sb-html" class="tab-content active"><pre>{(BASE/"sociabuzz-alert.html").read_text(encoding="utf-8")}</pre></div>
<div id="sb-css" class="tab-content"><pre>{(BASE/"sociabuzz-alert.css").read_text(encoding="utf-8")}</pre></div>
<div id="sw-html" class="tab-content"><pre>{(BASE/"saweria-alert.html").read_text(encoding="utf-8")}</pre></div>
<div id="sw-css" class="tab-content"><pre>{(BASE/"saweria-alert.css").read_text(encoding="utf-8")}</pre></div>
</div>

<script>
function showTab(id){{
  document.querySelectorAll('.tab-content').forEach(e=>e.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(e=>e.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  event.target.classList.add('active');
}}
</script>
</body>
</html>
'''

OUT.write_text(HTML, encoding="utf-8")
print("preview written", OUT, len(HTML.encode()))
