from PIL import Image

def extract_palette(image_path, size=5):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((100, 100))
    colors = img.getcolors(10000)
    colors.sort(reverse=True)
    return [c[1] for c in colors[:size]]
