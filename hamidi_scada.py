import tkinter as tk

vitesse = "9600"
port = "COM3"
requete = "01 03 00 00 00 05 85 C9"

def envoyer():
    reponse = "01 03 0A 00 F5 03 E8 00 31 00 02 00 62 6A 3C"
    label_reponse.config(text=reponse)

def RAS():
    label_etat.config(text="RAS", bg="green")

def alerte():
    label_etat.config(text="Alerte", bg="orange")

def critique():
    label_etat.config(text="Critique", bg="red")

fenetre = tk.Tk()
fenetre.title("Supervision de la salle T/H/P")
fenetre.geometry("600x450")

font = ("arial", 18)
monTexte_titre = tk.Label(fenetre, text="Supervision de la salle T/H/P", font=font, fg="black", bg="mintcream")
monTexte_titre.pack(side="top", fill="x")

frame1 = tk.LabelFrame(fenetre, text="Configuration")
frame1.pack(padx=10, pady=10, fill="x")

label_etat = tk.Label(frame1, text="RAS", bg="green", width=10)
label_etat.grid(row=0, column=0, pady=5)

tk.Label(frame1, text="Vitesse de transmission").grid(row=0, column=1, sticky="w",)
entry_vitesse = tk.Entry(frame1)
entry_vitesse.insert(0, vitesse)
entry_vitesse.grid(row=0, column=2, pady=5)

tk.Label(frame1, text="Port").grid(row=0, column=3, sticky="w")
entry_port = tk.Entry(frame1)
entry_port.insert(0, port)
entry_port.grid(row=0, column=4, pady=5)

frame2 = tk.LabelFrame(fenetre, text="Requête Modbus")
frame2.pack(padx=10, pady=10, fill="x")

entry_requete = tk.Entry(frame2, width=30)
entry_requete.insert(0, requete)
entry_requete.pack(pady=5)

tk.Button(frame2, text="Envoyer", command=envoyer).pack(pady=10)


frame3 = tk.LabelFrame(fenetre, text="Réponse")
frame3.pack(padx=10, pady=10, fill="x")

label_reponse = tk.Label(frame3, text="", fg="blue")
label_reponse.pack(pady=5)


fenetre.mainloop()