#coding: utf-8

class Morpion():
	def __init__(self):
		self.morpion1 = [
			[0, 0, 0],
			[10, 10, 10],
			[0, 0, 0]
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


	def verifie_alignements(self):
		for l in range(0, 3):
			if self.morpion1[l][0] + self.morpion1[l][1] + self.morpion1[l][2] == 3:
				self.j_gagnant = True
			elif self.morpion1[l][0] + self.morpion1[l][1] + self.morpion1[l][2] == 30:
				self.j_gagnant = False

		for c in range(0, 3):
			if self.morpion1[c][0] + self.morpion1[c][0] + self.morpion1[c][0] == 3:
				self.j_gagnant = True
			elif self.morpion1[c][0] + self.morpion1[c][0] + self.morpion1[c][0] == 30:
				self.j_gagnant = False


		if self.morpion1[0][0] + self.morpion1[1][1] + self.morpion1[2][2] == 3:
			self.j_gagnant = True
		elif self.morpion1[0][2] + self.morpion1[1][1] + self.morpion1[2][0] == 30:
			self.j_gagnant = False

morp = Morpion()
morp.verifie_alignements()