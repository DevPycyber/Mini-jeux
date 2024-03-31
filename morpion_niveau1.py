from random import choice

class Joueur():
	def __init__(self):
		self.pion_joueur = 1
		self.position_pion_joueur = ''
		self.joueurs = [True, False]
		self.joueur_actuel = choice(self.joueurs)
		



class Morpion(Joueur):
	def __init__(self):
		self.morpion1 = [
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]
		]  
		self.morpion2 = [
			['','',''],
			['','',''],
			['','','']
		]
		self.ligne = 0
		self.colonne = 0
		self.cases_prises = []
		self.cases_libres = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C0', 'C1', 'C2']
		self.retry_choice = ''
		self.pos_in_list = 0
		self.j_gagnant = None
		self.somme_ligne_a = 0
		self.somme_ligne_b = 0
		self.somme_ligne_c = 0

		self.somme_colonne_a = 0
		self.somme_colonne_b = 0
		self.somme_colonne_c = 0

		self.somme_diagonale_a = 0
		self.somme_diagonale_b = 0

		self.sommel1 = 0
		self.sommel2 = 0
		self.sommel2 = 0
		self.sommecol1 = 0
		self.sommecol2 = 0
		self.sommecol3 = 0

		self.somme_diago1 = 0
		self.somme_diago2 = 0

	def afficher_morpion(self):
		print(' |   1 | 2 | 3')
		print(' --------------  ')
		print("A|",self.morpion2[0])
		print("B|",self.morpion2[1])
		print("C|",self.morpion2[2])

	
	def verifie_alignements(self):
		for lc in range(0, 3):
			if self.morpion1[lc][0] + self.morpion1[lc][1] + self.morpion1[lc][2] == 3:
				self.j_gagnant = True
				

			elif self.morpion1[lc][0] + self.morpion1[lc][1] + self.morpion1[lc][2] == 30:
				self.j_gagnant = False
				

			elif self.morpion1[0][lc] + self.morpion1[1][lc] + self.morpion1[2][lc] == 3:
				self.j_gagnant = True
				

			elif self.morpion1[0][lc] + self.morpion1[1][lc] + self.morpion1[2][lc] == 30:
				self.j_gagnant = False
				

		if self.morpion1[0][0] + self.morpion1[1][1] + self.morpion1[2][2] == 3:
			self.j_gagnant = True
			

		elif self.morpion1[0][0] + self.morpion1[1][1] + self.morpion1[2][2] == 30:
			self.j_gagnant = False
			
		elif self.morpion1[0][2] + self.morpion1[1][1] + self.morpion1[2][0] == 3:
			self.j_gagnant = True
			

		elif self.morpion1[0][2] + self.morpion1[1][1] + self.morpion1[2][0] == 30:
			self.j_gagnant = False
			
			
	def recommencer(self):
		self.joueur_actuel = choice(J1.joueurs)
		self.cases_libres = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C0', 'C1', 'C2']
		self.cases_prises = []
		self.morpion1 = [
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]
		]
		self.morpion2 = [
			['','',''],
			['','',''],
			['','','']
		]
		self.j_gagnant = None

	


class IA(Morpion):
	def __init__(self):
		self.pion_ia = 10
		self.position_pion_ia = ''
		
		

morpion = Morpion()
tic_tac_ia = IA()
J1 = Joueur()

while morpion.j_gagnant == None and len(morpion.cases_prises) < 9:
	if morpion.cases_prises == []:
		print('''Ceci est un jeu de morpion, vous devez aligner trois pions en ligne,  
		colonne et diagonale . Vous affronterez une intelligence artificielle. Bonne chance''')
	morpion.afficher_morpion()

	if J1.joueur_actuel != True and J1.joueur_actuel == False:
		print('Au tour de l\' intelligence artificielle')
		tic_tac_ia.position_pion_ia = choice(morpion.cases_libres)
		morpion.ligne = tic_tac_ia.position_pion_ia[0]
		morpion.colonne = tic_tac_ia.position_pion_ia[1]
		morpion.colonne = int(morpion.colonne)
		if morpion.ligne == 'A':
			morpion.ligne = 0
		elif morpion.ligne == 'B':
			morpion.ligne = 1
		elif morpion.ligne == 'C':
			morpion.ligne = 2
		morpion.morpion1[morpion.ligne][morpion.colonne] = tic_tac_ia.pion_ia
		morpion.morpion2[morpion.ligne][morpion.colonne] = 'O'
		morpion.cases_prises.append(tic_tac_ia.position_pion_ia)
		morpion.pos_in_list = morpion.cases_libres.index(tic_tac_ia.position_pion_ia)
		del morpion.cases_libres[morpion.pos_in_list]
		morpion.verifie_alignements()
		J1.joueur_actuel = True

	elif J1.joueur_actuel != False and J1.joueur_actuel == True:
		print('au tour du joueur')
		J1.position_pion_joueur = input('Où voulez vous placer votre pion ?             ')
		if len(J1.position_pion_joueur) == 2:
			J1.position_pion_joueur = J1.position_pion_joueur.upper()
			if J1.position_pion_joueur in morpion.cases_prises:
				print('case prise, veuillez réessayer')
			else:
				morpion.ligne = J1.position_pion_joueur[0]
				morpion.colonne = J1.position_pion_joueur[1]
				morpion.colonne = int(morpion.colonne)
				morpion.ligne = morpion.ligne.upper()
				if morpion.ligne == 'A':
					morpion.ligne = 0
				elif morpion.ligne == 'B':
					morpion.ligne = 1
				elif morpion.ligne == 'C':
					morpion.ligne = 2
				morpion.morpion1[morpion.ligne][morpion.colonne] = J1.pion_joueur
				morpion.morpion2[morpion.ligne][morpion.colonne] = 'X'
				morpion.verifie_alignements()
				morpion.cases_prises.append(J1.position_pion_joueur)
				morpion.pos_in_list = morpion.cases_libres.index(J1.position_pion_joueur)
				del morpion.cases_libres[morpion.pos_in_list]
				J1.joueur_actuel = False
	
	if  morpion.j_gagnant == True:
		morpion.afficher_morpion()
		print('le joueur a gagné, félicitation')
		morpion.retry_choice = input('voulez vous recommencer?     ')
		if morpion.retry_choice not in ['non', 'n', 'no']:
			morpion.recommencer()
		else:
			break

		

	elif morpion.j_gagnant == False:
		morpion.afficher_morpion()
		print('l\'intelligence artificielle a gagné , félicitation')
		morpion.retry_choice = input('voulez vous recommencer?     ')
		if morpion.retry_choice not in ['non', 'n', 'no']:
			morpion.recommencer()
		else:
			break
		

	elif len(morpion.cases_prises) == 9 and morpion.cases_libres == []:
		print('match nul')
		print('félicitation aux 2 joueurs')
		morpion.retry_choice = input('voulez vous recommencer?     ')
		if morpion.retry_choice not in ['non', 'n', 'no']:
			morpion.recommencer()
		else:
			break