import tkinter as tk
from tkinter import messagebox

# === Hauptfenster ===
root = tk.Tk()
root.title("Transportmodus")
root.attributes("-fullscreen", True)  # Vollbild
root.config(cursor="none")

# === Farben ===
BG_COLOR = "#202020"
BTN_COLOR = "#333333"
TEXT_COLOR = "#FFFFFF"
GREEN = "#00CC00"
RED = "#CC0000"
FONT = ("Arial", 16)
FONT_BIG = ("Arial", 20, "bold")

root.configure(bg=BG_COLOR)

# === Container für Inhalt ===
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(expand=True, fill="both", padx=20, pady=20)

# === Titel ===
title = tk.Label(content_frame, text="Transportmodus", fg="lightblue", bg=BG_COLOR, font=("Arial", 26, "bold"))
title.pack(pady=10)

# === Infotext ===
info_text = (
    "Im Transportmodus fährt das Solarpanel\n"
    "in seine Ausgangs- und Transportposition zurück.\n"
    "In diesem Modus werden keine Messungen durchgeführt!"
)
info = tk.Label(content_frame, text=info_text, fg=TEXT_COLOR, bg=BG_COLOR, font=FONT, justify="center")
info.pack(pady=10)

# === JA / NEIN Buttons ===
button_frame = tk.Frame(content_frame, bg=BG_COLOR)
button_frame.pack(pady=20)

def on_yes():
    messagebox.showinfo("JA", "Transportmodus gestartet.")

def on_no():
    messagebox.showinfo("NEIN", "Transportmodus abgebrochen.")

btn_yes = tk.Button(button_frame, text="JA", bg=GREEN, fg="black", font=FONT_BIG, width=10, height=2, command=on_yes)
btn_yes.pack(side="left", padx=20)

btn_no = tk.Button(button_frame, text="NEIN", bg=RED, fg="black", font=FONT_BIG, width=10, height=2, command=on_no)
btn_no.pack(side="right", padx=20)

# === Unteres Menü ===
bottom_frame = tk.Frame(root, bg=BG_COLOR)
bottom_frame.pack(side="bottom", fill="x", pady=10)

def dummy_action(name):
    messagebox.showinfo(name, f"{name} gedrückt")

menu_buttons = [
    ("🔄 Start", "Start"),
    ("🛠️ Handbetrieb", "Handbetrieb"),
    ("⚙️ Auto-betrieb", "Autobetrieb"),
    ("ℹ️ Infopanel", "Infopanel"),
    ("📦 Transport-modus", "Transportmodus")
]

for text, name in menu_buttons:
    b = tk.Button(bottom_frame, text=text, font=FONT, width=15, height=2, bg=BTN_COLOR, fg=TEXT_COLOR,
                  command=lambda n=name: dummy_action(n))
    b.pack(side="left", padx=5)

# === ESC schließt Vollbild ===
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()

