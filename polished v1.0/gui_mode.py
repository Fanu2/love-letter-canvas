import tkinter as tk
from tkinter import colorchooser, filedialog
from color_core import emotion_from_color
from palette import extract_palette

def run_gui():
    root = tk.Tk()
    root.title("Unified Color App")

    label = tk.Label(root, text="Pick a color", width=30)
    label.pack(pady=10)

    def pick_color():
        color = colorchooser.askcolor()
        if color[0]:
            rgb = tuple(map(int, color[0]))
            label.config(text=f"{rgb}\n{emotion_from_color(rgb)}", bg=color[1])

    def load_image():
        path = filedialog.askopenfilename()
        if path:
            palette = extract_palette(path)
            label.config(text=f"Palette:\n{palette}")

    tk.Button(root, text="Pick Color", command=pick_color).pack()
    tk.Button(root, text="Load Image Palette", command=load_image).pack()

    root.mainloop()
