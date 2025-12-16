import random
from datetime import datetime

# Fixed identities
BELOVED = "Rosa"
RELATION = "my own blood"
SENDER = "Papa"

# Language pools (base moods only)
OPENINGS = {
    "romantic": [
        "My heart smiles every time I think of you",
        "Every thought of you feels like a gentle embrace",
        "You live quietly in the deepest part of my heart",
        "Loving you comes as naturally as breathing",
        "My soul softens whenever your name crosses my mind"
    ],
    "sweet": [
        "You make everything feel lighter and kinder",
        "Your presence fills my days with warmth",
        "Thinking of you brings a soft smile to my face",
        "You add sweetness to even the simplest moments",
        "You make my heart feel at home"
    ],
    "calm": [
        "With you in my thoughts, everything feels peaceful",
        "Your memory brings stillness to my heart",
        "You are my quiet comfort in a noisy world",
        "Thinking of you steadies my soul",
        "You remind me to breathe slowly and gently"
    ],
    "passionate": [
        "My love for you burns strong and steady",
        "You awaken something powerful in my heart",
        "Every part of me recognizes you",
        "You are the fire that keeps my spirit alive",
        "My devotion to you runs deep and fierce"
    ]
}

FEELINGS = [
    "you are deeply cherished",
    "you are endlessly loved",
    "you are my greatest blessing",
    "you mean more to me than words can hold",
    "you are carried in my heart always"
]

CLOSINGS = [
    "Always remember how precious you are to me",
    "Never forget how loved you are",
    "May this love stay with you always",
    "Hold this love close whenever you need strength",
    "Let this remind you that you are never alone"
]

# NEW: map extended moods to base language tones
MOOD_ALIAS = {
    "warm": "sweet",
    "night": "romantic",
    "dreamy": "calm"
}

def generate_message(mood: str) -> str:
    # Resolve mood safely
    base_mood = MOOD_ALIAS.get(mood, mood)
    if base_mood not in OPENINGS:
        base_mood = "romantic"

    # Time-aware opening
    hour = datetime.now().hour
    time_phrase = ""
    if hour < 12:
        time_phrase = "As this day begins, "
    elif hour >= 20:
        time_phrase = "As the night wraps the world in quiet, "

    opening = random.choice(OPENINGS[base_mood])
    feeling = random.choice(FEELINGS)
    closing = random.choice(CLOSINGS)

    return (
        f"{time_phrase}{opening}, {BELOVED}, {RELATION}. "
        f"{feeling}. {closing}.\n\n— {SENDER}"
    )
