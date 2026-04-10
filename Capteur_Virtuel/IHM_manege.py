import tkinter as tk
from tkinter import messagebox

print("test")

def dire_bonjour():
    age = entry_age.get()
    messagebox.showinfo("Message", "Bonjour !")

fenetre = tk.Tk()
fenetre.title("TP Manège Parc d'attraction - BTS CIEL")
fenetre.geometry("450x300")

font = ("arial", 18)
monTexte_titre = tk.Label(fenetre, text="Manège du parc - Force1 / Force 2", font=font, fg="navy", bg="grey")
monTexte_titre.pack(side="top", fill="x")

font = ("arial", 16)
monTexte_info = tk.Label(
    fenetre,
    text="Entrez votre âge et votre taille pour savoir à quelle force vous pouvez faire le manège.",
    font=font,
    fg="black",
    wraplength=500)
monTexte_info.pack()

monTexte_age = tk.Label(fenetre, text="Entrez votre age :", font=font, fg="black")
monTexte_age.pack()

entry_age = tk.Entry(fenetre, width=40)
entry_age.pack()

monTexte_taille = tk.Label(fenetre, text="Entrez votre taille (en m, exemple : 1.73) :", font=font, fg="black")
monTexte_taille.pack()

entry_taille = tk.Entry(fenetre, width=40)
entry_taille.pack()

def affiche_message():
    age_str = entry_age.get()
    taille_str = entry_taille.get()

    if age_str.isdigit() and taille_str.replace(".", "").isdigit():
        age = int(age_str)
        taille = float(taille_str) * 100

        ageMin = 14
        tailleMinF1 = 110
        tailleMinF2 = 130

        if age < ageMin:
            message = "Désolé, il faut avoir au moins 14 ans."
        else:
            if taille >= tailleMinF2:
                message = "Manège autorisé en Force 2."
            elif taille >= tailleMinF1:
                message = "Manège autorisé en Force 1."
            else:
                message = "Désolé, il faut mesurer au moins 110 cm."

        label_resultat.config(text=message)
    else:
        label_resultat.config(text="Veuillez entrer un âge et une taille valides.")

bouton_envoyer = tk.Button(fenetre, text="Envoyer", command=affiche_message)
bouton_envoyer.pack()

label_resultat = tk.Label(fenetre, text="", font=("arial", 14), fg="green")
label_resultat.pack(pady=10)

fenetre.mainloop()