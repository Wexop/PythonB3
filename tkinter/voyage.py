from tkinter import *

from tkcalendar import DateEntry


class InterfaceVoyage(Tk):
    def __init__(self, voyage):
        super().__init__()

        self.title("Détails du Voyage")

        # Titre centré en haut et en gras
        titre_label = Label(self, text=voyage.nom, font=("Helvetica", 16, "bold"), pady=10)
        titre_label.pack()

        # Description centrée
        description_label = Label(self, text=voyage.description, justify="center", padx=20)
        description_label.pack()

        # Image
        image_label = Label(self)
        image_label.img = PhotoImage(file=voyage.image)
        image_label.config(image=image_label.img, height=400, width=1080)
        image_label.pack()

        # Pays et Ville
        pays_ville_label = Label(self, text=f"Pays: {voyage.pays}   Ville: {voyage.ville}", pady=10)
        pays_ville_label.pack()

        # Calendrier pour les dates de début et de fin
        date_debut_label = Label(self, text="Date de début:")
        date_debut_label.pack()
        date_debut_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_debut_entry.set_date(voyage.dateDebut)
        date_debut_entry.pack()

        date_fin_label = Label(self, text="Date de fin:")
        date_fin_label.pack()
        date_fin_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_fin_entry.set_date(voyage.dateFin)
        date_fin_entry.pack()

        # Prix en énorme, gras et jaune
        prix_label = Label(self, text=f"Prix: {voyage.prix} €", font=("Helvetica", 24, "bold"), fg="orange")
        prix_label.pack()


class Voyage:
    def __init__(self, nom, pays, ville, description, image, dateDebut, dateFin, prix):
        self.nom = nom
        self.pays = pays
        self.ville = ville
        self.description = description
        self.image = image
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.prix = prix

    def afficher(self):
        print(f"Nom: {self.nom}\n" \
              f"Pays: {self.pays}\n" \
              f"Ville: {self.ville}\n" \
              f"Description: {self.description}\n" \
              f"Image: {self.image}\n" \
              f"Date de début: {self.dateDebut}\n" \
              f"Date de fin: {self.dateFin}\n" \
              f"Prix: {self.prix}")


voyage = Voyage("Voyage au Quebec", "Quebec", "Montreal",
                "Super voyage en plein coeur des tabernacles de gens qui parle le canadien leu",
                "img.png",
                "1/01/2024", "15/01/2024", 1200)

app = InterfaceVoyage(voyage)
app.mainloop()
