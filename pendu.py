# coding: utf-8

"""
Ceci est un jeu de pendu,
auteur : Ronhan
merci de respecter le travail fait

Copyright 2020 Ronhan inc, tous droit réservé
"""
from tkinter import*
from random import choice
import tkinter.messagebox as tkMessagebox

user_letter = ""
root_window = Tk()
root_window.attributes('-fullscreen', True)
root_window.title("jeu du pendu")
root_window.config(background="grey")
writing_space = Canvas(root_window, width=500, height=500, bg="white")

Mots = [
    "tele",
    "escalier",
    "balcon",
    "climatisation",
    "chauffage",
    "mobilier",
    "jardin",
    "chambre",
    "cuisine",
    "toilette",
    "maison"

]
password = choice(Mots)
nb_lettres_password = len(password)
liste_visible = [""] * nb_lettres_password
essais_actuel = 1
essais_total = 10
essais_restant = 0

# Composants de l'échafaud

#dimension

dim_socle1 = (85, 395, 400, 430)
dim_barre = (85, 50, 130, 395)
dim_barre2 = (130, 50, 320, 70)
dim_corde = (300, 70, 320, 110)
dim_visage = (270, 110, 350, 200)
dim_oeil_1 = (280, 140, 298, 150)
dim_oeil_2 = (317, 140, 335, 150)
dim_bouche = (289, 165, 326, 190)
dim_vertebre_column = (310, 200, 310, 300)
dim_bras_gauche = (290, 270, 310, 230)
dim_bras_droit = (310, 230, 330, 270)
dim_pied_gauche = (310, 300, 285, 345)
dim_pied_droit = (310, 300, 335, 345)

socle = writing_space.create_rectangle(dim_socle1, fill="brown", state="hidden")
barre1 = writing_space.create_rectangle(dim_barre, state="hidden", fill="brown")
barre2 = writing_space.create_rectangle(dim_barre2, fill="brown", state="hidden")
corde = writing_space.create_rectangle(dim_corde, fill="#565661", state="hidden")
visage = writing_space.create_arc(dim_visage, extent=359, style=ARC, state="hidden")
oeil1 = writing_space.create_arc(dim_oeil_1,  extent=359, style=ARC, state="hidden")
oeil2 = writing_space.create_arc(dim_oeil_2,  extent=359, style=ARC, state="hidden")
bouche = writing_space.create_arc(dim_bouche,  extent=359, style=ARC, state="hidden")
colonne_vertebre = writing_space.create_line(dim_vertebre_column, state="hidden")
bras_gauche = writing_space.create_line(dim_bras_gauche, state="hidden")
bras_droit = writing_space.create_line(dim_bras_droit, state="hidden")
pied_gauche = writing_space.create_line(dim_pied_gauche, state="hidden")
pied_droit = writing_space.create_line(dim_pied_droit, state="hidden")


Intro_Pendu = Label(root_window, text="""Ceci est un jeu de pendu, vous devez deviner un mot avec les lettres qui le
composent, vous avez 10 essais""", font=("Courrier", 15), bg="grey")
frame1 = Frame(root_window, bg="grey")
Choix_letter = Label(frame1, text="veuillez entrer une lettre", font=("Arial", 35), bg="grey")

Entry_letter = Entry(frame1, font=("Arial", 35))
quit_button = Button(root_window, text="quitter", font=("Courrier", 25), command=root_window.destroy)

affiche_jeu_visible = Label(frame1, text=liste_visible, font=("Hervetica", 35))


def remise_zero():
    Mots = [
        "tele",
        "escalier",
        "balcon",
        "climatisation",
        "chauffage",
        "mobilier",
        "jardin",
        "chambre",
        "cuisine",
        "toilette",
        "maison"
    ]
    password = choice(Mots)
    nb_lettres_password = len(password)
    liste_visible = [""]*nb_lettres_password
    liste_non_visible = []
    writing_space.itemconfig(socle, state="hidden")
    writing_space.itemconfig(barre1, state="hidden")
    writing_space.itemconfig(barre2, state="hidden")
    writing_space.itemconfig(corde, state="hidden")
    writing_space.itemconfig(visage, state="hidden")
    writing_space.itemconfig(oeil1, state="hidden")
    writing_space.itemconfig(oeil2, state="hidden")
    writing_space.itemconfig(bouche, state="hidden")
    writing_space.itemconfig(colonne_vertebre, state="hidden")
    writing_space.itemconfig(bras_gauche, state="hidden")
    writing_space.itemconfig(bras_droit, state="hidden")
    writing_space.itemconfig(pied_gauche, state="hidden")
    writing_space.itemconfig(pied_droit, state="hidden")
    essais_total = 10
    essais_actuel = 1
    i = 0
    while i < nb_lettres_password:
        liste_non_visible.append(password[i])
        i += 1
    affiche_jeu_visible.config(text=liste_visible)



def traitement_letter():
    global password
    global nb_lettres_password
    global liste_visible
    global Mots
    global liste_non_visible
    global essais_total
    global essais_restant
    global essais_actuel
    compteur = 0

    if user_letter in liste_non_visible:
        if user_letter in liste_visible:
            tkMessagebox.showerror("Lettre déjà entré", "Vous avez déjà entré cette lettre, veuillez réessayer")
        else:
            for letter in liste_non_visible:
                if letter == user_letter:
                    index = compteur
                    liste_visible[index] = user_letter
                    tkMessagebox.showinfo("lettre trouvé", "Vous avez trouvé cette lettre, Félicitation ! ")
                    affiche_jeu_visible.configure(text=liste_visible)

                if liste_visible == liste_non_visible:
                    choix = tkMessagebox.askquestion("retry", "Voulez-vous recommencer", icon='info')
                    if choix == "yes":
                        remise_zero()
                    elif choix == "no":
                        root_window.destroy()

                compteur += 1

    elif user_letter not in liste_non_visible:
        essais_restant = essais_total - essais_actuel
        tkMessagebox.showwarning("mauvaise lettre", "Ce n\'est pas la bonne lettre, il vous reste {} essais"
                                 .format(essais_restant))
        essais_actuel += 1
        if essais_restant == 0:
            tkMessagebox.showinfo("essais épuisé", "Vous avez perdu, le mot à trouver était {} ".format(password))
            choix = tkMessagebox.askquestion("retry", "Voulez-vous recommencer", icon='info')
            if choix == "yes":
                remise_zero()
            else:
                root_window.destroy()
        elif essais_restant == 9:
            writing_space.itemconfig(socle, state="normal")
            writing_space.itemconfig(barre1, state="normal")
        elif essais_restant == 8: writing_space.itemconfig(barre2, state="normal")
        elif essais_restant == 7: writing_space.itemconfig(corde, state="normal")
        elif essais_restant == 6: writing_space.itemconfig(visage, state="normal")
        elif essais_restant == 5:
            writing_space.itemconfig(oeil1, state="normal")
            writing_space.itemconfig(oeil2, state="normal")
        elif essais_restant == 4: writing_space.itemconfig(bouche, state="normal")
        elif essais_restant == 3: writing_space.itemconfig(colonne_vertebre, state="normal")
        elif essais_restant == 2:
            writing_space.itemconfig(bras_gauche, state="normal")
            writing_space.itemconfig(bras_droit, state="normal")
        elif essais_restant == 1:
            writing_space.itemconfig(pied_gauche, state="normal")
            writing_space.itemconfig(pied_droit, state="normal")


def gather_letter():
    global user_letter
    user_letter = Entry_letter.get()
    traitement_letter()


valid_letter = Button(frame1, text="Valider", font=("Arial", 20), command=gather_letter)


liste_non_visible = []
i = 0
while i < nb_lettres_password:
    liste_non_visible.append(password[i])
    i += 1

Intro_Pendu.pack(side=TOP)
Choix_letter.pack()
Entry_letter.pack()
valid_letter.pack(fill=X)
frame1.pack(side=RIGHT)
affiche_jeu_visible.pack(side=BOTTOM)
writing_space.pack(side=LEFT)
quit_button.pack(side=BOTTOM)
root_window.mainloop()




