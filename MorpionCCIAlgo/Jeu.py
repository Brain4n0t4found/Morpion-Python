from joueurVSia import JvsIA
from joueurVSjoueur import JvsJ
import Visu
intro = True

print('''
    ┌────────────────────────────────────────────────=Présentation=───────────────────────────────────────────────────┐
    │Bonjour et bienvenue dans le jeu du morpion réalisé par le meilleur groupe du BTS SIO 2018 de la CCI Strasbourg. │
    │Vous allez être projeté dans une expérience unique du jeu du morpion.                                            │
    └────────────────────────────────────────────────=XOXOXOXOXOXO=───────────────────────────────────────────────────┘
    ''')
input("Appuyez sur 'Entrer' pour continuer ...")
Visu.clearPrompt()

while intro:
    q1 = input("Connaissez-vous les règles du morpion? (oui/non) : ")
    if q1 == "oui":
        Visu.clearPrompt()
        print('''Très bien ! Avant de commencer à jouer vous allez devoir choisir votre mode de jeu.

                                -=XOXOXOXOXOXOXO=- Choisissez -=XOXOXOXOXOXOXO=-
        ''')
        while intro:
            try:
                q2 = int(input('''Vous voulez jouer en:
                      (1) - Joueur Contre Joueur ?
                      (2) - Joueur Contre IA ?
                      (3) - Quitter le jeu ?

-------------------------------------------> '''))
                if q2 == 1:
                    print('''Très bon choix, vous allez maintenant pouvoir choisir vos noms !
                        -=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-
                        ''')
                    j1 = input("Joueur 1, comment vous appelez-vous ?: ")
                    print('''
                    -=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-
                    ''')

                    j2 = input("Joueur 2 comment vous appelez-vous ?: ")
                    print('''
                    - {} vous jouez les X !
                    - {} vous jouez les O !
                    Bonne chance à vous deux et que le meilleur gagne !'''.format(j1, j2))
                    ########### Début partie Joueur VS Joueur ##############
                    JvsJ()
                elif q2 == 2:
                    print('''Choix intéressant, allez vous faire le poids ?

                            -=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-
                    ''')
                    j1 = input("Comment vous appelez-vous ? ")
                    Visu.clearPrompt()
                    print('''
                    - {}, vous jouez les X
                    - L'IA joue les O
                    -=XOXOXOXOXO=- Bonne chance {} ! -=XOXOXOXOXO=-'''.format(j1, j1))
    ########### Début partie contre l'IA ##############
                    JvsIA()
                elif q2 == 3:
                    print("Merci d'avoir joué")
                    quit()
            except ValueError:
                print("Entrez une valeur correcte !!")
                pass
        break
    elif q1 == "non":
        Visu.clearPrompt()
        print('''
        ┌───────────────────────────────────────────────=Règles=─────────────────────────────────────────────────┐
        │Les règles sont simples, vous allez devoir gagner en alignant votre symbole dans une grille de 3 par 3, │
        │tout cela en moins de 10 tours. Avant de commencer à jouer vous allez devoir choisir votre mode de jeu. │
        └───────────────────────────────────────────────=XOXOXO=─────────────────────────────────────────────────┘
                                -=XOXOXOXOXOXOXO=- Choisissez -=XOXOXOXOXOXOXO=-
            ''')
        input("Appuyez sur 'Entrer' pour continuer ...")
        continue
