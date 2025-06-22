import tkinter as tk

# === Farben & Fonts ===
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
        self.title("Touch UI")
        self.geometry("800x480")  # Feste Größe für das Display
        self.configure(bg=BG_COLOR)

        # Container für Inhalte
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(side="left", fill="both", expand=True)

        # Seiten initialisieren
        self.frames = {}
        for F in (StartPage, HandbetriebPage, AutobetriebPage, InfopanelPage, TransportPage):
            page = F(parent=self.container, controller=self)
            self.frames[F.__name__] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.create_right_menu()

        self.bind("<Escape>", lambda e: self.destroy())

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def create_right_menu(self):
        right_frame = tk.Frame(self, bg=BG_COLOR, width=200)
        right_frame.pack(side="right", fill="y", padx=5, pady=5)

        buttons = [
            ("🔄 Start", "StartPage"),
            ("🛠️ Handbetrieb", "HandbetriebPage"),
            ("⚙️ Auto-betrieb", "AutobetriebPage"),
            ("ℹ️ Infopanel", "InfopanelPage"),
            ("📦 Transport-modus", "TransportPage")
        ]

        for text, page in buttons:
            btn = tk.Button(
                right_frame,
                text=text,
                font=FONT,
                width=20,
                height=2,
                bg=BTN_COLOR,
                fg=TEXT_COLOR,
                anchor="w",
                command=lambda p=page: self.show_frame(p)
            )
            btn.pack(side="top", fill="x", pady=5)

# === Seiten ===

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

        info = (
            "Im Transportmodus fährt das Solarpanel\n"
            "in seine Ausgangs- und Transportposition zurück.\n"
            "In diesem Modus werden keine Messungen durchgeführt!"
        )

        tk.Label(self, text=info, fg=TEXT_COLOR, bg=BG_COLOR, font=FONT, justify="center").pack(pady=10)

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="JA", bg=GREEN, fg="black", font=FONT_BIG, width=10, height=2).pack(side="left", padx=20)
        tk.Button(btn_frame, text="NEIN", bg=RED, fg="black", font=FONT_BIG, width=10, height=2).pack(side="right", padx=20)

# === Start ===
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
