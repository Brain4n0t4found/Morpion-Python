import os

q1 = ''
q2 = ''

os.system('cls')
print(" ")
print("┌────────────────────────────────────────────────=Présentation=───────────────────────────────────────────────────┐")
print("│Bonjour et bienvenue dans le jeu du morpion réalisé par le meilleur groupe du BTS SIO 2018 de la CCI Strasbourg.│")
print("│Vous allez être projeté dans une expérience unique du jeu du morpion.                                           │")
print("└────────────────────────────────────────────────=XOXOXOXOXOXO=───────────────────────────────────────────────────┘")
print(" ")

while q1.lower() != "oui" and q1.lower() != "non":
	q1 = input("Connaissez-vous les règles du morpion? (oui/non) : ")
	if q1 == "oui":
		os.system('cls')
		print(" ")
		print("Très bien ! Avant de commencer à jouer vous allez devoir choisir votre mode de jeu.")
		print(" ")
		print("            -=XOXOXOXOXOXOXO=- Choisissez -=XOXOXOXOXOXOXO=-            ")
		print(" ")
		while q2 != 1 and q2 != 2:
			try:
				q2 = int(input("Vous voulez jouer en Joueur Contre Joueur (1) ou Joueur Contre IA (2) ? "))
				if q2 == 1:
					os.system('cls')
					print("Très bon choix, vous allez maintenant pouvoir choisir vos noms ! ")
					print(" ")
					print("-=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-")
					print(" ")
					j1 = input("Joueur 1 comment vous appeler vous ? ")
					os.system('cls')
					print(" ")
					print("-=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-")
					print(" ")
					j2 = input("Joueur 2 comment vous appeler vous ? ")
					os.system('cls')
					print(" ")
					print("{} vous jouez les X et {} vous jouez les O !".format(j1, j2))
					print("Bonne chance à vous deux et que le meilleur gagne !")
				elif q2 == 2:
					os.system('cls')
					print("Choix intéressant, allez vous faire le poids ? ")
					print(" ")
					print("-=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-")
					print(" ")
					j1 = input("Joueur 1 comment vous appeler vous ? ")
					os.system('cls')
					print("{} vous jouez les X et l'IA joue les O ! Bonne chance {} !".format(j1, j1))
			except ValueError:
				print("Entrez une valeur correcte !!")
				pass
		break
	elif q1 == "non":
		os.system('cls')
		print(" ")
		print("┌───────────────────────────────────────────────=Règles=─────────────────────────────────────────────────┐")
		print("│Les règles sont simples, vous allez devoir gagner en alignant votre symbole dans une grille de 3 par 3, │")
		print("│tout cela en moins de 10 tours. Avant de commancer à jouer vous allez devoir choisir votre mode de jeu.│")
		print("└───────────────────────────────────────────────=XOXOXO=─────────────────────────────────────────────────┘")
		print(" ")
		print("            -=XOXOXOXOXOXOXO=- Choisissez -=XOXOXOXOXOXOXO=-            ")
		print(" ")
		while q2 != 1 and q2 != 2:
			try:
				q2 = int(input("Vous voulez jouer en Joueur Contre Joueur (1) ou Joueur Contre IA (2) ? "))
				if q2 == 1:
					os.system('cls')
					print("Très bon choix, vous allez maintenant pouvoir choisir vos noms ! ")
					print(" ")
					print("-=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-")
					print(" ")
					j1 = input("Joueur 1 comment vous appeler vous ? ")
					os.system('cls')
					print(" ")
					print("-=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-")
					print(" ")
					j2 = input("Joueur 2 comment vous appeler vous ? ")
					os.system('cls')
					print(" ")
					print("{} vous jouez les X et {} vous jouez les O !".format(j1, j2))
					print("Bonne chance à vous deux et que le meilleur gagne !")
				elif q2 == 2:
					os.system('cls')
					print("Choix intéressant, allez vous faire le poids ? ")
					print(" ")
					print("-=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-")
					print(" ")
					j1 = input("Joueur 1 comment vous appeler vous ? ")
					os.system('cls')
					print("{} vous jouez les X et l'IA joue les O ! Bonne chance {} !".format(j1, j1))
			except ValueError:
				print("Entrez une valeur correcte !!")
				pass
		break