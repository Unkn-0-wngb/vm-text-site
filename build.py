import hashlib
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
SUPPORT = "https://discord.gg/wXhHBKNAQe"
EMAIL = "contact@laveryjonez.uk"
UPDATED = "30 October 2026"


def stamp(name):
    digest = hashlib.sha1((SRC / name).read_bytes()).hexdigest()[:8]
    stem, dot, ext = name.rpartition(".")
    return f"{stem}.{digest}.{ext}"


CSS = stamp("style.css")
JS = stamp("k.js")

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


DISCORD = '<svg class="dc" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.317 4.37a19.79 19.79 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.74 19.74 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.1 13.1 0 0 1-1.872-.892.077.077 0 0 1-.008-.128c.126-.094.252-.192.372-.292a.074.074 0 0 1 .078-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .079.009c.12.1.245.199.372.293a.077.077 0 0 1-.007.128 12.3 12.3 0 0 1-1.873.891.077.077 0 0 0-.04.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.029 19.84 19.84 0 0 0 6.002-3.03.077.077 0 0 0 .031-.055c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.095 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.095 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>'

ICONS = {
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "bolt": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "list": '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
    "check": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "sliders": '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 24 24" {STROKE}>{ICONS[name]}</svg>'


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
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#1e1f22">
{extra}
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/icon.png">
<link rel="preload" href="/fonts/body.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/{CSS}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="VM-Text">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<script src="/{JS}" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current=""):
    return f"""<header class="top">
  <div class="wrap">
    <a class="brand" href="/"><img src="/icon.png" alt="" width="32" height="32">VM-Text</a>
    <nav aria-label="Main">
      <a href="/#features">Features</a>
      <a href="/#how">How it works</a>
      <a href="/#commands">Commands</a>
      <a href="/#faq">FAQ</a>
      <a href="{SUPPORT}">Support</a>
    </nav>
    <details class="add">
      <summary class="btn blurple small-btn">{DISCORD}Add to Discord<svg class="chev" viewBox="0 0 24 24" {STROKE}><polyline points="6 9 12 15 18 9"/></svg></summary>
      <div class="menu">
        <a href="{USER_LINK}"><b>To my account</b><span>Use it in any DM, group chat or server</span></a>
        <a href="{SERVER_LINK}"><b>To a server</b><span>Also replies to voice messages automatically</span></a>
      </div>
    </details>
  </div>
</header>
"""


FOOTER = f"""<footer class="foot">
  <div class="wrap">
    <div class="about">
      <a class="brand" href="/"><img src="/icon.png" alt="" width="32" height="32">VM-Text</a>
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
        <h2>Help</h2>
        <ul>
          <li><a href="{SUPPORT}">Support server</a></li>
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


FEATURES = [
    ("lock", "Private transcripts", "Transcribe (private) shows the text only to you. Good for DMs, meetings, or anywhere you can't play audio."),
    ("users", "Public transcripts", "Transcribe (public) posts the transcript in the channel so everyone there can read it."),
    ("bolt", "Automatic replies", "In a server, VM-Text can reply to every voice message by itself. Anyone with Manage Server can switch it off."),
    ("list", "A fair queue", "Requests are handled one at a time, in order. If you have to wait, it tells you your place."),
    ("check", "Transcribed once", "Each voice message is done a single time. Ask again later and you get the saved text straight away."),
    ("globe", "21 languages", "It works out the language on its own. If it guesses wrong, pick one yourself in /config."),
]

COMMANDS = [
    ("Transcribe (private)", "Apps menu", "Right-click a voice message, then Apps, then VM-Text. Only you see the transcript."),
    ("Transcribe (public)", "Apps menu", "Same menu. The transcript is posted in the channel for everyone."),
    ("/config", "Slash command", "Choose your language and whether replies are embeds or plain text. Server admins can set a default language and turn automatic replies on or off."),
]

FAQ = [
    ("Is it free?", "Yes. It's a personal project with no ads and nothing to pay for."),
    ("Does it keep my voice messages?", "No. The audio is held in memory while it's transcribed and then discarded. The transcript text is saved so each message is only done once, and it's deleted if the message is deleted."),
    ("Why does it ask for the Message Content permission?", "So it can tell that a message in a server is a voice message and fetch the audio. It doesn't read or store ordinary text messages."),
    ("Account or server, which should I pick?", "On your account you can use the Transcribe commands in any DM, group chat or server, but only when you ask. Added to a server, the bot can also reply to every voice message there automatically. You can have both."),
    ("How do I turn off the automatic replies?", "Someone with the Manage Server permission can run /config and switch automatic transcription off."),
    ("The transcript is wrong.", "Background noise, strong accents, names and people talking over each other all cause mistakes. Setting the right language in /config usually helps."),
    ("Where do I get help?", f'Join the <a href="{SUPPORT}">support server</a> and open a ticket, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.'),
    ("Who runs this?", f"Lavery.Jonez, in Scotland. It's a one-person project and runs on a small server I look after myself."),
]


def index():
    page = head(
        "VM-Text: turn Discord voice messages into text",
        "VM-Text is a free Discord app that turns voice messages into text. Add it to your account or a server.",
        "/",
    )
    page += header()
    cards = "".join(
        f'<div class="card"><span class="ico">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in FEATURES
    )
    cmds = "".join(
        f'<div class="cmd"><div><code>{n}</code><span class="kind">{k}</span></div><p>{d}</p></div>' for n, k, d in COMMANDS
    )
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    page += f"""<main id="main">
<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p class="pill"><span></span>Free Discord app, no ads</p>
      <h1>Turn voice messages into <em>text.</em></h1>
      <p class="lede">Right-click a voice message, pick Apps, and a few seconds later you have the words. Works in DMs, group chats and servers. The audio is never saved.</p>
      <div class="btns">
        <a class="btn blurple" href="{USER_LINK}">{DISCORD}Add to my account</a>
        <a class="btn grey" href="{SERVER_LINK}">Add to a server</a>
      </div>
      <p class="small">Or <a href="{SUPPORT}">join the support server</a></p>
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
</section>

<section class="stats">
  <div class="wrap">
    <div><b>21</b><span>languages</span></div>
    <div><b>0</b><span>audio files saved</span></div>
    <div><b>Free</b><span>no ads, no tracking</span></div>
  </div>
</section>

<section class="part" id="features">
  <div class="wrap">
    <h2>Everything you need to read a voice message</h2>
    <p class="sub">Simple to use, and out of the way until you need it.</p>
    <div class="grid">{cards}</div>
  </div>
</section>

<section class="part alt" id="how">
  <div class="wrap">
    <h2>How it works</h2>
    <p class="sub">Three steps, no setup.</p>
    <ol class="steps">
      <li><span class="n">1</span><h3>Add it</h3><p>Add VM-Text to your Discord account, or to a server.</p></li>
      <li><span class="n">2</span><h3>Right-click</h3><p>Right-click a voice message (long-press on mobile) and open Apps, then VM-Text.</p></li>
      <li><span class="n">3</span><h3>Read it</h3><p>Choose private or public. The transcript turns up in a few seconds.</p></li>
    </ol>
    <div class="diagram-wrap">{ctx_menu()}</div>
  </div>
</section>

<section class="part" id="commands">
  <div class="wrap">
    <h2>Commands</h2>
    <p class="sub">Two entries in the Apps menu and one slash command.</p>
    <div class="cmds">{cmds}</div>
  </div>
</section>

<section class="part alt" id="privacy">
  <div class="wrap">
    <div class="privacy">
      <div>
        <h2>Your data stays yours</h2>
        <p class="sub left">Voice messages are transcribed on my own server with Whisper, an open-source model. Nothing is sent to an outside service, and the audio is thrown away the moment the text exists.</p>
        <p class="sub left">The full details are in the <a href="/pp">Privacy Policy</a> and the <a href="/tos">Terms</a>.</p>
      </div>
      <ul class="facts">
        <li><b>Audio</b><span>Never saved</span></li>
        <li><b>Transcripts</b><span>Kept as text, deleted with the message</span></li>
        <li><b>Settings</b><span>Your language and style</span></li>
        <li><b>Ads and tracking</b><span>None</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="part" id="faq">
  <div class="wrap narrow">
    <h2>Questions</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="cta-box">
      <div>
        <h2>Ready to read your voice messages?</h2>
        <p>Add it in a couple of clicks. Stuck? The support server is open.</p>
      </div>
      <div class="btns">
        <a class="btn white" href="{USER_LINK}">Add to my account</a>
        <a class="btn ghost" href="{SUPPORT}">Support server</a>
      </div>
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
  <h1>That page isn't here.</h1>
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
shutil.copy(SRC / "style.css", DIST / CSS)
shutil.copy(SRC / "k.js", DIST / JS)

index()
legal("tos", "Terms of Service", "The terms for using the VM-Text Discord app.")
legal("pp", "Privacy Policy", "How the VM-Text Discord app handles your data.")
not_found()
sitemap()
