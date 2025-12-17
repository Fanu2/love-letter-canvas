from terminal_mode import run_terminal
from gui_mode import run_gui
from web_mode import run_web

print("""
Unified Color App
1 - Terminal
2 - GUI
3 - Web
""")

choice = input("Choose mode: ")

if choice == "1":
    run_terminal()
elif choice == "2":
    run_gui()
elif choice == "3":
    run_web()
else:
    print("Invalid choice")
