import tkinter as tk

vitesse = "9600"
port = "COM3"
requete = "01 03 00 00 00 05 85 C9"
temperature = "21.4°C"
HUmidite = "54%"
Pression = "998hPa"

def envoyer():
    reponse = "01 03 0A 00 F5 03 E8 00 31 00 02 00 62 6A 3C"
    sous_frame_reponse.config(text=reponse)
def RAS():
    label_etat.config(text="RAS", bg="mediumspringgreen")
def alerte():
    label_etat.config(text="Alerte", bg="orange")
def critique():
    label_etat.config(text="Critique", bg="red")

fenetre = tk.Tk()
fenetre.title("Supervision de la salle T/H/P")
fenetre.geometry("800x650")
fenetre.config(bg="oldlace")

font = ("arial", 18)
monTexte_titre = tk.Label(fenetre, text="Supervision de la salle T/H/P", font=font, fg="black",bg="oldlace")
monTexte_titre.pack(side="top",padx=10, pady=10, fill="x")
frame_message = tk.LabelFrame(fenetre, text="")

frame_message.pack(padx=10, pady=10, fill="x")
label_etat = tk.Label(frame_message, text="RAS", bg="mediumspringgreen", width=10)
label_etat.pack(side="left",padx=10, pady=10, fill="x")

tk.Label(frame_message, text="Message a afficher a l'utilisateur").pack(side="top",padx=10, pady=10, fill="x")
entry_vitesse = tk.Entry(frame_message)

frame_config = tk.LabelFrame(fenetre, text="Configuration")
frame_config.pack(padx=10, pady=10, fill="x")

tk.Label(frame_config, text="Vitesse de transmission").pack(side="left",padx=10, pady=10, fill="x")
entry_vitesse = tk.Entry(frame_config)
entry_vitesse.insert(0, vitesse)
entry_vitesse.pack(side="left",padx=10, pady=10, fill="x")

tk.Label(frame_config, text="Port").pack(side="left",padx=10, pady=10, fill="x")
entry_port = tk.Entry(frame_config)
entry_port.insert(0, port)
entry_port.pack(side="left",padx=10, pady=10, fill="x")

frame_modbus = tk.LabelFrame(fenetre, text="Requête Modbus")
frame_modbus.pack(padx=10, pady=10, fill="x")

tk.Label(frame_modbus, text="Requete").pack(side="left",padx=10, pady=10, fill="x")
entry_vitesse = tk.Entry(frame_modbus)

entry_requete = tk.Entry(frame_modbus, width=30)
entry_requete.insert(0, requete)
entry_requete.pack(side="left",pady=10, padx=10)

tk.Button(frame_modbus, text="Envoyer", command=envoyer).pack(side="left",pady=5,padx=10, fill="x")

frame_donnees = tk.LabelFrame(fenetre, text="Données")
frame_donnees.pack(padx=10, pady=10, fill="x")

tk.Label(frame_donnees, text="Réponse").pack(side="top",padx=10, pady=10, fill="x")
entry_reponse = tk.Entry(frame_donnees)

sous_frame_reponse = tk.Label(frame_donnees, text="", fg="blue")
sous_frame_reponse.pack(pady=5)

frame_donnees = tk.Frame(frame_donnees)
frame_donnees.pack(fill="x", pady=10)

sous_frame_temperature = tk.Frame(frame_donnees, bd=1, relief="solid")
sous_frame_temperature.pack(side="left", fill="both", padx=90)

tk.Label(sous_frame_temperature, text="21.4°C").pack(pady=5)

sous_frame_humidite = tk.Frame(frame_donnees, bd=1, relief="solid")
sous_frame_humidite.pack(side="left", fill="both", padx=150)

tk.Label(sous_frame_humidite, text="54%").pack(pady=15)

sous_frame_pression = tk.Frame(frame_donnees, bd=1, relief="solid")
sous_frame_pression.pack(side="right", fill="both", padx=50)

tk.Label(sous_frame_pression, text="998 hPa").pack(pady=5)


fenetre.mainloop()
