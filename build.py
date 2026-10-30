import math
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
SITE = "https://vm-text.laveryjonez.uk"
APP_ID = "1565793546844377099"
USER_LINK = f"https://discord.com/oauth2/authorize?client_id={APP_ID}&integration_type=1&scope=applications.commands"
SERVER_LINK = (
    f"https://discord.com/oauth2/authorize?client_id={APP_ID}&integration_type=0"
    "&scope=bot+applications.commands&permissions=117760"
)
EMAIL = "contact@laveryjonez.uk"
UPDATED = "30 October 2026"

STROKE = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'

MENU_ICONS = {
    "smile": '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/>',
    "reply": '<polyline points="9 14 4 9 9 4"/><path d="M20 20v-7a4 4 0 0 0-4-4H4"/>',
    "forward": '<polyline points="15 14 20 9 15 4"/><path d="M4 20v-7a4 4 0 0 1 4-4h12"/>',
    "thread": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "copy": '<rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
    "bookmark": '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "apps": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>',
    "unread": '<path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><polyline points="22 6 12 13 2 6"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    "speak": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
    "id": '<line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/>',
}

MENU_GROUPS = [
    [("smile", "Add Reaction", "sub")],
    [("reply", "Reply", ""), ("forward", "Forward", ""), ("thread", "Create Thread", "")],
    [
        ("copy", "Copy Text", ""),
        ("bookmark", "Bookmark Message", ""),
        ("clock", "Create Reminder", "sub"),
        ("apps", "Apps", "on"),
        ("unread", "Mark Unread", ""),
        ("link", "Copy Message Link", ""),
        ("speak", "Speak Message", ""),
    ],
    [("flag", "Report Message", "danger")],
    [("id", "Copy Message ID", "")],
]


def head(title, desc, path, robots=None):
    url = SITE + path
    extra = f'<meta name="robots" content="{robots}">' if robots else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#ebe6da" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0d0c0b" media="(prefers-color-scheme: dark)">
{extra}
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/icon.png">
<link rel="preload" href="/fonts/serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<meta property="og:type" content="website">
<meta property="og:site_name" content="VM-Text">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<script src="/k.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current=""):
    def link(href, label, key=""):
        mark = ' aria-current="page"' if key and key == current else ""
        return f'<a href="{href}"{mark}>{label}</a>'

    return f"""<header class="top">
  <div class="wrap">
    <a class="brand" href="/"><img src="/icon.png" alt="" width="30" height="30">VM-Text</a>
    <nav aria-label="Main">
      {link("/#features", "Features")}
      {link("/#using", "Using it")}
      {link("/#faq", "FAQ")}
      {link("/tos", "Terms", "tos")}
      {link("/pp", "Privacy", "pp")}
      <a class="add" href="{USER_LINK}">Add to Discord</a>
    </nav>
  </div>
</header>
"""


FOOTER = f"""<footer class="foot">
  <div class="wrap">
    <div>
      <a class="brand" href="/"><img src="/icon.png" alt="" width="30" height="30">VM-Text</a>
      <p>A Discord app that turns voice messages into text. Run by Lavery.Jonez in Scotland.</p>
    </div>
    <div class="cols">
      <div>
        <h2>Add it</h2>
        <ul>
          <li><a href="{USER_LINK}">To your account</a></li>
          <li><a href="{SERVER_LINK}">To a server</a></li>
        </ul>
      </div>
      <div>
        <h2>Legal</h2>
        <ul>
          <li><a href="/tos">Terms of Service</a></li>
          <li><a href="/pp">Privacy Policy</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <p class="fine">VM-Text is an independent project. It is not affiliated with or endorsed by Discord Inc.</p>
  </div>
</footer>
</body>
</html>
"""


def waveform():
    heights = [30, 55, 80, 45, 100, 60, 35, 70, 40, 90, 55, 30, 65, 85, 50, 35, 75, 45, 25, 60, 40, 30, 50, 35]
    bars = []
    for i, h in enumerate(heights):
        bh = max(5, h * 0.24)
        fill = "#8b95ff" if i < 9 else "#6d7580"
        bars.append(f'<rect x="{i * 6}" y="{(26 - bh) / 2:.1f}" width="3" height="{bh:.1f}" rx="1.5" fill="{fill}"/>')
    return f'<svg class="wave" viewBox="0 0 144 26" aria-hidden="true">{"".join(bars)}</svg>'


def ctx_menu(active="Transcribe (private)"):
    send = f'<svg viewBox="0 0 24 24" {STROKE}><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>'
    chevron = f'<svg viewBox="0 0 24 24" {STROKE}><polyline points="9 18 15 12 9 6"/></svg>'
    search = f'<svg viewBox="0 0 24 24" {STROKE}><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
    icon = '<img src="/icon.png" alt="" width="20" height="20">'

    def item(name):
        on = " on" if name == active else ""
        return f'<div class="ctx-item{on}">{name}{send}</div>'

    groups = []
    for group in MENU_GROUPS:
        rows = []
        for key, label, state in group:
            cls = {"on": " on", "danger": " danger"}.get(state, "")
            arrow = chevron if state in ("sub", "on") else ""
            rows.append(
                f'<div class="mrow{cls}"><svg viewBox="0 0 24 24" {STROKE}>{MENU_ICONS[key]}</svg><span>{label}</span>{arrow}</div>'
            )
        groups.append('<div class="mgroup">' + "".join(rows) + "</div>")

    return f"""<div class="ctx3" role="img" aria-label="Discord's right-click menu: Apps, then VM-Text, then {active}">
  <div class="ctx-menu">{"".join(groups)}</div>
  <div class="ctx">
    <div class="ctx-panel">
      <div class="ctx-search">{search}Search commands</div>
      <div class="ctx-label">Frequently Used Commands</div>
      <div class="ctx-row">{icon}<span>Transcribe (public)</span>{send}</div>
      <div class="ctx-label">Apps</div>
      <div class="ctx-row open">{icon}<span>VM-Text</span>{chevron}</div>
    </div>
    <div class="ctx-sub">{item("Transcribe (private)")}{item("Transcribe (public)")}</div>
  </div>
</div>"""


LANGS = [
    "English", "Spanish", "French", "German", "Italian", "Portuguese", "Dutch", "Polish", "Russian", "Ukrainian",
    "Latvian", "Lithuanian", "Swedish", "Czech", "Romanian", "Turkish", "Arabic", "Hindi", "Japanese", "Korean", "Chinese",
]


def field():
    bars = []
    for i in range(120):
        h = 10 + 62 * abs(math.sin(i * 0.37) * math.cos(i * 0.11 + 1.3)) + 6 * abs(math.sin(i * 1.9))
        h = min(h, 76)
        cls = "p" if i < 60 else "q"
        bars.append(f'<rect class="{cls}" x="{i * 10}" y="{(80 - h) / 2:.1f}" width="6" height="{h:.1f}" rx="3"/>')
    return f'<svg class="bars" viewBox="0 0 1200 80" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{"".join(bars)}</svg>'


def strip():
    items = "".join(f"<span>{n}</span>" for n in LANGS)
    return (
        f'<div class="strip" role="img" aria-label="Works in {len(LANGS)} languages: {", ".join(LANGS)}">'
        f'<div class="track" aria-hidden="true"><div>{items}</div><div>{items}</div></div></div>'
    )


def index():
    page = head(
        "VM-Text: voice messages, as text",
        "VM-Text is a free Discord app that turns voice messages into text. Add it to your account or a server.",
        "/",
    )
    page += header()
    page += f"""<main id="main">
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p class="tc"><span class="rec"></span>Discord app &middot; free</p>
      <h1><span class="cap">Voice messages,</span> <span class="cap hot">as text.</span></h1>
      <p class="lede">Right-click a voice message, pick Apps, and a few seconds later you have the words. The audio is never saved.</p>
      <div class="btns">
        <a class="btn solid" href="{USER_LINK}">Add to my account</a>
        <a class="btn" href="{SERVER_LINK}">Add to a server</a>
      </div>
      <p class="small">Works in DMs, group chats and servers.</p>
    </div>

    <div class="discord" role="img" aria-label="Example: a voice message from Alex, followed by VM-Text's transcript of it">
      <div class="msg">
        <div class="av">A</div>
        <div>
          <div class="msg-head"><b>Alex</b><time>Today at 18:46</time></div>
          <div class="voice">
            <span class="play"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21"/></svg></span>
            {waveform()}
            <span class="dur">0:07</span>
          </div>
        </div>
      </div>
      <div class="msg">
        <div class="av bot"><img src="/icon.png" alt=""></div>
        <div>
          <div class="msg-head"><b>VM-Text</b><span class="tag">APP</span><time>Today at 18:46</time></div>
          <div class="embed">
            <div class="embed-author"><span class="av">A</span>Alex</div>
            <p class="embed-text">Hey, are we still on for the game tonight? I'll be online around eight.</p>
            <p class="embed-sub">0:07 voice message &nbsp;&middot;&nbsp; <span class="lnk">Jump to voice message</span></p>
            <div class="embed-foot"><span class="av">S</span>Requested by Sam &nbsp;&middot;&nbsp; English &nbsp;&middot;&nbsp; transcribed in 3.2s</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="field">{field()}<div class="head"><span>0:03 / 0:07</span></div></div>
</section>

{strip()}

<section class="part" id="features">
  <div class="wrap split">
    <div class="rail"><p class="tc">00:07</p><h2>What it does</h2></div>
    <div class="rows">
      <div><h3>Transcribe (private)</h3><p>Only you see the result. Good for DMs, meetings, or anywhere you can't play audio.</p></div>
      <div><h3>Transcribe (public)</h3><p>Posts the transcript in the channel so everyone there can read it.</p></div>
      <div><h3>Automatic replies</h3><p>In a server, the bot can reply to every voice message by itself. Anyone with Manage Server can switch that off.</p></div>
      <div><h3>A queue</h3><p>Requests are handled one at a time, in order. If you have to wait, it tells you your place.</p></div>
      <div><h3>Done once</h3><p>Each voice message is transcribed a single time. Ask again later and you get the saved text straight away.</p></div>
      <div><h3>Languages</h3><p>It works out the language on its own. If it keeps guessing wrong, pick one from the list of 21 in <code>/config</code>.</p></div>
      <div><h3>Settings</h3><p>Run <code>/config</code> to choose your language and whether replies are embeds or plain text. Server admins can set a default language and the automatic replies.</p></div>
    </div>
  </div>
</section>

<section class="part" id="using">
  <div class="wrap">
    <div class="rail flat"><p class="tc">00:14</p><h2>Using it</h2></div>
    <ol class="steps">
      <li><b>Add it</b><span>Add VM-Text to your Discord account, or to a server.</span></li>
      <li><b>Right-click</b><span>Right-click a voice message (long-press on mobile) and open Apps, then VM-Text.</span></li>
      <li><b>Read it</b><span>Choose private or public. The transcript turns up in a few seconds.</span></li>
    </ol>
    <div class="diagram-wrap">{ctx_menu()}</div>
  </div>
</section>

<section class="part" id="privacy">
  <div class="wrap split">
    <div class="rail"><p class="tc">00:21</p><h2>Your data</h2></div>
    <div class="prose-lg">
      <p class="big">The audio stays on my own server and is thrown away the moment the text exists.</p>
      <p>Voice messages are transcribed with Whisper, an open-source model. Nothing is sent to an outside service.</p>
      <p>What is kept:</p>
      <ul>
        <li>the transcript text, so the same message isn't transcribed twice (it's deleted if the message is deleted);</li>
        <li>your settings: language, output style, and the automatic replies setting for a server.</li>
      </ul>
      <p>No ads, no tracking, no analytics. The full details are in the <a href="/pp">Privacy Policy</a> and the <a href="/tos">Terms</a>.</p>
    </div>
  </div>
</section>

<section class="part" id="faq">
  <div class="wrap split">
    <div class="rail"><p class="tc">00:28</p><h2>Questions</h2></div>
    <div>
      <details>
        <summary>Is it free?</summary>
        <p>Yes. It's a personal project with no ads and nothing to pay for.</p>
      </details>
      <details>
        <summary>Does it keep my voice messages?</summary>
        <p>No. The audio is held in memory while it's transcribed and then discarded. The transcript text is saved so each message is only done once, and it's deleted if the message is deleted.</p>
      </details>
      <details>
        <summary>Why does it ask for the Message Content permission?</summary>
        <p>So it can tell that a message in a server is a voice message and fetch the audio. It doesn't read or store ordinary text messages.</p>
      </details>
      <details>
        <summary>Account or server, which should I pick?</summary>
        <p>On your account you can use the Transcribe commands in any DM, group chat or server, but only when you ask. Added to a server, the bot can also reply to every voice message there automatically. You can have both.</p>
      </details>
      <details>
        <summary>How do I turn off the automatic replies?</summary>
        <p>Someone with the Manage Server permission can run <code>/config</code> and switch automatic transcription off.</p>
      </details>
      <details>
        <summary>The transcript is wrong.</summary>
        <p>Background noise, strong accents, names and people talking over each other all cause mistakes. Setting the right language in <code>/config</code> usually helps.</p>
      </details>
      <details>
        <summary>Who runs this?</summary>
        <p>Lavery.Jonez, in Scotland. You can reach me at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </details>
    </div>
  </div>
</section>

<section class="closing">
  <div class="wrap">
    <h2>Try it on your own account first.</h2>
    <p>A couple of clicks to add, and just as easy to remove.</p>
    <div class="btns">
      <a class="btn dark" href="{USER_LINK}">Add to my account</a>
      <a class="btn line" href="{SERVER_LINK}">Add to a server</a>
    </div>
  </div>
</section>
</main>
"""
    page += FOOTER
    (DIST / "index.html").write_text(page, encoding="utf-8")


def legal(name, title, desc):
    body = (ROOT / "content" / f"{name}.html").read_text(encoding="utf-8")
    toc = []

    def add_id(m):
        text = m.group(1)
        key = f"s{len(toc) + 1}"
        toc.append((key, re.sub(r"^\d+\.\s*", "", text)))
        return f'<h2 id="{key}">{text}</h2>'

    body = re.sub(r"<h2>(.*?)</h2>", add_id, body)
    toc_html = "".join(f'<a href="#{k}">{t}</a>' for k, t in toc)

    page = head(f"{title} - VM-Text", desc, f"/{name}")
    page += header(name)
    page += f"""<main id="main">
<div class="wrap doc-head">
  <h1>{title}</h1>
  <p>Last updated {UPDATED}</p>
</div>
<div class="wrap legal">
  <aside class="toc" aria-label="On this page"><b>On this page</b>{toc_html}</aside>
  <article class="prose">
{body}
  </article>
</div>
</main>
"""
    page += FOOTER
    (DIST / f"{name}.html").write_text(page, encoding="utf-8")


def not_found():
    page = head("Page not found - VM-Text", "That page doesn't exist.", "/404", robots="noindex")
    page += header()
    page += f"""<main id="main">
<div class="wrap lost">
  <h1><span class="cap">That page isn't here.</span></h1>
  <p>The link may be old or mistyped. <a href="/">Go back to the start</a>.</p>
</div>
</main>
"""
    page += FOOTER
    (DIST / "404.html").write_text(page, encoding="utf-8")


def sitemap():
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>2026-10-30</lastmod></url>" for p in ("/", "/tos", "/pp"))
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>',
        encoding="utf-8",
    )
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


if DIST.exists():
    shutil.rmtree(DIST)
shutil.copytree(SRC / "static", DIST)
shutil.copy(SRC / "style.css", DIST / "style.css")
shutil.copy(SRC / "k.js", DIST / "k.js")

index()
legal("tos", "Terms of Service", "The terms for using the VM-Text Discord app.")
legal("pp", "Privacy Policy", "How the VM-Text Discord app handles your data.")
not_found()
sitemap()
