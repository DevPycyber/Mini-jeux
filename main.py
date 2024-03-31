#    MOTUS GAME

import random

#variables
liste_mot = ["ACTEUR", "AVIRON", "BOXEUR", "BRONZE", "BUDGET", "CHAQUE",
"CHEVAL", "CIMENT", "COMPTE", "CONTRE", "CONTRE", "CUPIDE", "DESIGN", "DICTER", "DOSAGE",
"DOUCHE", "DROITE", "EXPORT", "FLAQUE", "FORAGE", "GLAIVE", "GRAINE", "GROUPE",
"JARDIN", "JUNGLE", "LUCIDE", "MANCHE", "MARQUE", "MIRAGE", "MOUCHE",
"NIVEAU", "NOVICE", "OISEAU", "PAQUET", "PILOTE"]

mot_user = ""
mot = random.choice(liste_mot)

for x in range(8):
    mot_user = input("Proposer un mot de 6 lettres:  ")
    mot_user = mot_user.upper()
    if len(mot_user) != 6:
        while len(mot_user) != 6:
            mot_user = input("Proposer un mot de 6 lettres:  ")
            mot_user = mot_user.upper()
    if mot_user == mot:
        print("GAGNE")
    else:
        for i in range(0, 6):
            for letter in mot_user:
                if letter in mot:
                    if mot[i] == letter:
                        print(mot_user[i], "#", end="")
                    elif mot_user[i] != mot[i]:
                        print(mot_user[i], "?", end="")
                elif mot_user[i] not in mot:
                    print(mot_user[i].lower())
                i +=1

                


                
