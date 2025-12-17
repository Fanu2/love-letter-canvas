from flask import Flask, render_template, request
from message_engine import generate_message
import random

app = Flask(__name__)

LOVE_COLORS = {
    "romantic": [
        ["#ff758f", "#ffb3c6", "#ffc8dd"],
        ["#f72585", "#ff8fab", "#ffd6e0"]
    ],
    "sweet": [
        ["#ffd6e0", "#ffcad4", "#f4acb7"],
        ["#fbc4ab", "#ffdab9", "#fde2e4"]
    ],
    "passionate": [
        ["#9d0208", "#dc2f02", "#f48c06"]
    ],
    "calm": [
        ["#bde0fe", "#cdb4db", "#a2d2ff"]
    ],
    "warm": [
        ["#ffb703", "#fb8500", "#f77f00"]
    ],
    "night": [
        ["#240046", "#3c096c", "#5a189a"]
    ],
    "dreamy": [
        ["#e0aaff", "#cdb4db", "#ffc8dd"]
    ]
}

# Allowed font colors (safety)
FONT_COLORS = {
    "#ffffff",  # White
    "#fff1c1",  # Ivory
    "#ffcad4",  # Rose
    "#ffd166",  # Gold
    "#1d3557",  # Midnight
    "#343a40"   # Charcoal
}

@app.route("/", methods=["GET", "POST"])
def index():
    # Mood (safe fallback)
    mood = request.form.get("mood", "romantic")
    if mood not in LOVE_COLORS:
        mood = "romantic"

    # Mode: card or letter (safe fallback)
    mode = request.form.get("mode", "card")
    if mode not in ("card", "letter"):
        mode = "card"

    # Font color (safe fallback)
    font_color = request.form.get("font_color", "#ffffff")
    if font_color not in FONT_COLORS:
        font_color = "#ffffff"

    # Custom message (letter or pasted text)
    custom_message = request.form.get("custom_message", "").strip()
    if custom_message:
        message = custom_message
    else:
        message = generate_message(mood)

    # Pick ONE palette
    colors = random.choice(LOVE_COLORS[mood])

    return render_template(
        "index.html",
        message=message,
        colors=colors,
        mood=mood,
        mode=mode,
        font_color=font_color
    )

if __name__ == "__main__":
    print("Starting Love Card / Love Letter Server…")
    app.run(host="127.0.0.1", port=5000, debug=False)
