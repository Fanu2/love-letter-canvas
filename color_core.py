def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def brightness(rgb):
    return sum(rgb) / 3

def emotion_from_color(rgb):
    r, g, b = rgb
    if b > r and b > g:
        return "Calm / Cool"
    if r > 200 and g < 100:
        return "Energetic / Passion"
    if brightness(rgb) < 80:
        return "Dark / Serious"
    if brightness(rgb) > 180:
        return "Light / Happy"
    return "Neutral"
