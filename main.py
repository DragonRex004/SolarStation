import tkinter as tk

# === Basisfarben und Schriftarten ===
BG_COLOR = "#202020"
BTN_COLOR = "#333333"
TEXT_COLOR = "#FFFFFF"
GREEN = "#00CC00"
RED = "#CC0000"
FONT = ("Arial", 16)
FONT_BIG = ("Arial", 20, "bold")

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-View UI")
        self.attributes("-fullscreen", True)
        self.config(cursor="none")
        self.configure(bg=BG_COLOR)

        # Container für Seiten
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(expand=True, fill="both")

        # Alle Seiten initialisieren
        self.frames = {}
        for F in (StartPage, HandbetriebPage, AutobetriebPage, InfopanelPage, TransportPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Erste Seite anzeigen
        self.show_frame("StartPage")

        # Menüleiste unten
        self.create_bottom_bar()

        # ESC zum Schließen
        self.bind("<Escape>", lambda e: self.destroy())

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_bottom_bar(self):
        bottom_frame = tk.Frame(self, bg=BG_COLOR)
        bottom_frame.pack(side="bottom", fill="x", pady=10)

        buttons = [
            ("🔄 Start", "StartPage"),
            ("🛠️ Handbetrieb", "HandbetriebPage"),
            ("⚙️ Auto-betrieb", "AutobetriebPage"),
            ("ℹ️ Infopanel", "InfopanelPage"),
            ("📦 Transport-modus", "TransportPage")
        ]

        for text, page in buttons:
            b = tk.Button(bottom_frame, text=text, font=FONT, width=15, height=2, bg=BTN_COLOR, fg=TEXT_COLOR,
                          command=lambda p=page: self.show_frame(p))
            b.pack(side="left", padx=5)

# === Jede Seite als eigene Frame-Klasse ===

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        tk.Label(self, text="Startseite", font=("Arial", 24), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=100)

class HandbetriebPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        tk.Label(self, text="Handbetrieb", font=("Arial", 24), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=100)

class AutobetriebPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        tk.Label(self, text="Autobetrieb", font=("Arial", 24), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=100)

class InfopanelPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        tk.Label(self, text="Infopanel", font=("Arial", 24), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=100)

class TransportPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)

        tk.Label(self, text="Transportmodus", font=("Arial", 26, "bold"), fg="lightblue", bg=BG_COLOR).pack(pady=10)

        info_text = (
            "Im Transportmodus fährt das Solarpanel\n"
            "in seine Ausgangs- und Transportposition zurück.\n"
            "In diesem Modus werden keine Messungen durchgeführt!"
        )

        tk.Label(self, text=info_text, fg=TEXT_COLOR, bg=BG_COLOR, font=FONT, justify="center").pack(pady=10)

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="JA", bg=GREEN, fg="black", font=FONT_BIG, width=10, height=2,
                  command=lambda: print("Transportmodus gestartet")).pack(side="left", padx=20)

        tk.Button(btn_frame, text="NEIN", bg=RED, fg="black", font=FONT_BIG, width=10, height=2,
                  command=lambda: print("Transportmodus abgebrochen")).pack(side="right", padx=20)

# === App starten ===
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
