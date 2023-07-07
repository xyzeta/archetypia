import tkinter as tk
import tkinter.font as tkfont
import random
import json
from PIL import ImageTk, Image

color_schemes = [
    {
        "name": "Blautöne",
        "bg_color_primary": "#2C3E50",
        "bg_color_secondary": "#34495E",
        "bg_color_button": "#2980B9",
        "text_color": "#FFFFFF",
        "accent_color": "#E74C3C",
        "bg_color_window": "#34495E"
    },
    {
        "name": "Rottöne",
        "bg_color_primary": "#8E353D",
        "bg_color_secondary": "#A93241",
        "bg_color_button": "#C0392B",
        "text_color": "#FFFFFF",
        "accent_color": "#F39C12",
        "bg_color_window": "#8E353D"
    },
    {
        "name": "Violetttöne",
        "bg_color_primary": "#6C3483",
        "bg_color_secondary": "#7D3C98",
        "bg_color_button": "#8E44AD",
        "text_color": "#FFFFFF",
        "accent_color": "#F1C40F",
        "bg_color_window": "#7D3C98"
    },
    {
        "name": "Grüntöne",
        "bg_color_primary": "#1E8449",
        "bg_color_secondary": "#27AE60",
        "bg_color_button": "#2ECC71",
        "text_color": "#FFFFFF",
        "accent_color": "#F39C12",
        "bg_color_window": "#27AE60"
    },
    {
        "name": "Grautöne",
        "bg_color_primary": "#555555",
        "bg_color_secondary": "#777777",
        "bg_color_button": "#999999",
        "text_color": "#FFFFFF",
        "accent_color": "#FF0000",
        "bg_color_window": "#333333"
    },
    {
        "name": "Pastellfarben",
        "bg_color_primary": "#F9E79F",
        "bg_color_secondary": "#AED6F1",
        "bg_color_button": "#F5B7B1",
        "text_color": "#333333",
        "accent_color": "#C39BD3",
        "bg_color_window": "#D7BDE2"
    },
    {
        "name": "Sonnenuntergang",
        "bg_color_primary": "#F4D03F",
        "bg_color_secondary": "#E59866",
        "bg_color_button": "#DC7633",
        "text_color": "#FFFFFF",
        "accent_color": "#1ABC9C",
        "bg_color_window": "#E67E22"
    },
    {
        "name": "Herbstlaub",
        "bg_color_primary": "#D35400",
        "bg_color_secondary": "#8E44AD",
        "bg_color_button": "#E74C3C",
        "text_color": "#FFFFFF",
        "accent_color": "#27AE60",
        "bg_color_window": "#E67E22"
    },
    {
        "name": "Pastellblüten",
        "bg_color_primary": "#FADBD8",
        "bg_color_secondary": "#85C1E9",
        "bg_color_button": "#F8C471",
        "text_color": "#333333",
        "accent_color": "#E67E22",
        "bg_color_window": "#F9E79F"
    }
]

class ArchetypiaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Archetypia")
        random.shuffle(color_schemes)  # Mischt die Reihenfolge der Farbschemata
        self.current_color_scheme = color_schemes[0]  # Wählt das erste Farbschema
        self.interpretations = self.load_interpretations()

        self.root.wm_attributes("-topmost", 1)
        self.root.wm_attributes("-topmost", 1)

        # Fenstergröße
        window_width = 800
        window_height = 900

        # Bildschirmgröße
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Fensterposition berechnen
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Fensterposition festlegen
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.create_widgets()
        self.apply_color_scheme()


    def load_interpretations(self):
        with open("interpretations.json", "r", encoding='utf-8') as file:
            interpretations = json.load(file)
        return interpretations

    def create_widgets(self):
        self.container_frame = tk.Frame(self.root)
        self.container_frame.pack(padx=5, pady=20)

        self.image_frame = tk.Frame(self.container_frame)
        self.image_frame.pack(side=tk.TOP, padx=20, pady=(10, 0))

        self.image = ImageTk.PhotoImage(file="Archetypia_Journey_662x142_Bild.gif")
        self.image_label1 = tk.Label(self.image_frame, image=self.image, anchor='w',
                                     pady=0, relief="solid", bd=0.5)
        self.image_label1.pack(side=tk.LEFT)

        #Beginn Startseite Text
        text = """Archetypia Journey

        Das Leben ist tatsächlich eine Reise, gefüllt mit Höhen und Tiefen, Herausforderungen und Triumphen sowie endlosen Möglichkeiten für Wachstum und Entdeckung. Es geht nicht darum, ein endgültiges Ziel der Perfektion zu erreichen, sondern vielmehr darum, die Erfahrungen anzunehmen, von ihnen zu lernen und sich auf dem Weg der Erkenntnis weiterzuentwickeln. Diese Reise formt uns und erlaubt uns, das reiche und vielfältige Leben in seiner ganzen Pracht zu erleben.

        Auf unserem Weg begegnen wir verschiedenen Archetypen, die verschiedene Aspekte unserer eigenen Persönlichkeit und der Welt um uns herum repräsentieren. Diese Archetypen dienen als Wegweiser, die unseren Pfad erhellen und uns bei der Navigation durch die Komplexitäten des Lebens unterstützen. Im Spiel 'Archetypia Journey' begibst du dich auf eine Reise der Selbstentdeckung. Du erforschst die Tiefen deiner eigenen Psyche und entdeckst die Weisheit der Archetypen. Jede Karte, der du begegnest, enthüllt einen einzigartigen Archetypen, der dich einlädt, zu reflektieren, zu lernen und zu wachsen."""

        word_count = len(text.split())
        padx = word_count // 3  # Anpassung des Wertes, um den gewünschten Abstand zu erhalten
        text_width = 70  # Neue Breite des text_widget

        self.text_widget = tk.Text(self.container_frame, width=text_width, height=20, relief="solid", bd=0.5, padx=padx, pady=30,
                                   wrap=tk.WORD)
        self.text_widget.pack(side=tk.TOP, padx=0, pady=50)
        self.text_widget.insert(tk.END, text)
        self.text_widget.configure(state=tk.DISABLED)
        #Ende Startseite Text

        self.image_label2 = tk.Label(self.image_frame, anchor='w', pady=0, relief="solid", bd=0.5)
        self.image_label2.pack(side=tk.LEFT)

        self.text_frame = tk.Frame(self.container_frame)
        self.text_frame.pack(side=tk.TOP, padx=10)

        # Erstellen einer benutzerdefinierten Schriftart mit Schriftgröße 8 und Schriftart "Arial"
        custom_font = tkfont.Font(family="Helvetica", size=8)

        self.text_label1 = tk.Label(
            self.text_frame,
            width=43,
            height=8,
            wraplength=1 * 300 + 0,
            justify='left',
            anchor='nw',
            padx=15,
            pady=5,
            relief="solid",
            bd=0,
            font=custom_font
        )
        self.text_label1.pack_forget()

        self.text_label2 = tk.Label(
            self.text_frame,
            width=43,
            height=8,
            wraplength=1 * 300 + 0,
            justify='left',
            anchor='nw',
            padx=15,
            pady=5,
            relief="solid",
            bd=0,
            font=custom_font
        )
        self.text_label2.pack_forget()

        #self.text_label1.configure(highlightthickness=1)
        #self.text_label2.configure(highlightthickness=1)

        self.interpretation_frame_outer = tk.LabelFrame(self.container_frame, bd=0, highlightthickness=0, padx=5)
        self.interpretation_frame_outer.pack_forget()  # Verstecke den interpretation_frame_outer im ersten Fenster

        self.interpretation_frame = tk.Frame(self.container_frame, padx=10)

        self.interpretation_label = tk.Label(
            self.interpretation_frame,
            width=92,
            height=7,
            wraplength=631,
            justify='left',
            anchor='nw',
            padx=8,
            pady=5,
            relief="solid",
            bd=0,
            font=custom_font
        )
        self.interpretation_label.pack()
        # Verstecke den interpretation_frame_outer im ersten Fenster
        self.interpretation_frame_outer.pack_forget()
        #self.interpretation_label.configure(highlightthickness=1)

        self.button_frame = tk.Frame(self.container_frame, bg=self.current_color_scheme["bg_color_primary"],
                                     highlightbackground="white", highlightthickness=2)
        self.button_frame.pack(fill=tk.X, padx=22, pady=10)

        self.start_button = tk.Button(
            self.button_frame,
            text="Kartenlegung",
            command=self.generate_cards,
            relief="raised",
            bg=self.current_color_scheme["bg_color_button"],
            fg=self.current_color_scheme["text_color"]
        )
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.change_color_button = tk.Button(
            self.button_frame,
            text="Farbschema ändern",
            command=self.change_color_scheme,
            relief="raised",
            bg=self.current_color_scheme["bg_color_button"],
            fg=self.current_color_scheme["text_color"]
        )
        self.change_color_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.quit_button = tk.Button(
            self.button_frame,
            text="Schließen",
            command=self.root.destroy,
            relief="raised",
            bg=self.current_color_scheme["bg_color_button"],
            fg=self.current_color_scheme["text_color"]
        )
        self.quit_button.pack(side=tk.LEFT, padx=10, pady=10)

    def show_interpretation_frame(self):
        self.interpretation_frame_outer = tk.LabelFrame(self.container_frame, bd=0, highlightthickness=0, padx=15)
        self.interpretation_frame_outer.pack(pady=0)

        self.interpretation_frame.pack(side=tk.TOP, padx=10, pady=0)
        self.interpretation_label.pack()
    # Aktualisiere das Fenster, um die Änderungen anzuzeigen

    def generate_cards(self):
        random_a_card = random.choice(self.interpretations['a_cards'])
        random_b_card = random.choice(self.interpretations['b_cards'])
        # Löschen text_widget aus Startseite
        self.text_widget.pack_forget()
        self.show_interpretation_frame()

        a_card_image = Image.open(random_a_card['image'])
        a_card_image = a_card_image.resize((330, 514), Image.LANCZOS)
        a_card_image = ImageTk.PhotoImage(a_card_image)
        self.image_label1.configure(image=a_card_image)
        self.image_label1.image = a_card_image

        b_card_image = Image.open(random_b_card['image'])
        b_card_image = b_card_image.resize((330, 514), Image.LANCZOS)
        b_card_image = ImageTk.PhotoImage(b_card_image)
        self.image_label2.configure(image=b_card_image)
        self.image_label2.image = b_card_image

        self.text_label1.configure(text=random_a_card['text'])
        self.text_label2.configure(text=random_b_card['text'])

        interpretation = self.get_interpretation(random_a_card['image'], random_b_card['image'])
        self.interpretation_label.configure(text=interpretation)

        # Entferne das text_widget aus dem zweiten Fenster
        self.text_widget.pack_forget()

        # Frame für a_cards und b_cards erstellen
        self.cards_frame = tk.Frame(self.container_frame, pady=10)
        self.cards_frame.pack(side=tk.TOP)

        self.text_label1.pack(side=tk.LEFT, padx=(0, 5), pady=(5, 5),
                              anchor=tk.NW)  # Text für a_cards, reduzierter Abstand oben
        self.text_label2.pack(side=tk.LEFT, padx=(0, 0), pady=(5, 5),
                              anchor=tk.NW)  # Text für b_cards, reduzierter Abstand oben

        self.interpretation_label.pack(side=tk.TOP, padx=5, pady=(0, 5), anchor=tk.NW,
                                       ipadx=4)  # Interpretation, reduzierter Abstand oben und unten, breiteres Label

        self.button_frame.pack(fill=tk.X, padx=5, pady=(5, 8),
                               after=self.interpretation_label)  # Buttons nach Interpretation-Label platzieren
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.change_color_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.quit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.image_label1.pack(side=tk.LEFT, padx=(0, 5))  # Bild a_card
        self.image_label2.pack(side=tk.LEFT, padx=(0, 0))  # Bild b_card

        self.button_frame.configure(highlightthickness=2)  # Breiterer Rahmen für das Button-Frame

    def get_interpretation(self, a_card_image, b_card_image):
        for interpretation in self.interpretations['interpretations']:
            if a_card_image in interpretation['image'] and b_card_image in interpretation['image']:
                return interpretation['text']

        return "Keine Interpretation gefunden."

    def change_color_scheme(self):
        new_color_scheme = random.choice(color_schemes)
        self.current_color_scheme = new_color_scheme
        self.apply_color_scheme()

    def apply_color_scheme(self):
        self.root.configure(bg=self.current_color_scheme["bg_color_window"])
        self.container_frame.configure(bg=self.current_color_scheme["bg_color_primary"])
        self.image_frame.configure(bg=self.current_color_scheme["bg_color_primary"])
        self.text_frame.configure(bg=self.current_color_scheme["bg_color_primary"])
        self.interpretation_frame_outer.configure(bg=self.current_color_scheme["bg_color_primary"])
        self.interpretation_frame.configure(bg=self.current_color_scheme["bg_color_primary"])
        self.interpretation_label.configure(bg=self.current_color_scheme["bg_color_secondary"], fg=self.current_color_scheme["text_color"])

        self.button_frame.configure(bg=self.current_color_scheme["bg_color_primary"])
        self.quit_button.configure(bg=self.current_color_scheme["bg_color_button"], fg=self.current_color_scheme["text_color"])
        self.change_color_button.configure(bg=self.current_color_scheme["bg_color_button"], fg=self.current_color_scheme["text_color"])
        self.start_button.configure(bg=self.current_color_scheme["bg_color_button"], fg=self.current_color_scheme["text_color"])

        self.text_label1.configure(bg=self.current_color_scheme["bg_color_secondary"], fg=self.current_color_scheme["text_color"])
        self.text_label2.configure(bg=self.current_color_scheme["bg_color_secondary"], fg=self.current_color_scheme["text_color"])

    def center_image(self, label):
        label.update()
        label_width = label.winfo_width()
        label_height = label.winfo_height()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - label_width) // 2
        y = (screen_height - label_height) // 2

        self.root.geometry(f"{label_width + 0}x{label_height + 0}+{x}+{y}")

root = tk.Tk()
game = ArchetypiaGame(root)
root.mainloop()
