from color_core import emotion_from_color
from gradients import generate_gradient
from palette import extract_palette

def run_terminal():
    print("Terminal Color Mode")
    print("1 - RGB Emotion")
    print("2 - Gradient")
    print("3 - Image Palette")

    choice = input("Choose: ")

    if choice == "1":
        rgb = tuple(int(input(f"{x}: ")) for x in "RGB")
        print("Emotion:", emotion_from_color(rgb))

    elif choice == "2":
        c1 = tuple(int(input(f"C1 {x}: ")) for x in "RGB")
        c2 = tuple(int(input(f"C2 {x}: ")) for x in "RGB")
        print("Gradient:", generate_gradient(c1, c2))

    elif choice == "3":
        path = input("Image path: ")
        print("Palette:", extract_palette(path))
