import MorpionCode
import Visu

def JvsIA():
    print('''Choix intéressant, allez vous faire le poids ?

            -=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-
    ''')
    j1 = input("Comment vous appelez-vous ? ")
    Visu.clearPrompt()
    print('''
    - {}, vous jouez les X
    - L'IA joue les O
    -=XOXOXOXOXO=- Bonne chance {} ! -=XOXOXOXOXO=-'''.format(j1, j1))
    jouer = 'oui'
    while jouer == 'oui':
        # Initialisation des variables nécessaires à chaque parties
        compteur = 0
        symbJoueur = 'O'
        numJoueur = 2
        victoire = False
        tabCalc = MorpionCode.tabCalcInit
        # tabVisu = tabVisuInit

        while victoire is not True and compteur <= 9:

            # Initialisation des variables nécessaires à chaque tours
            compteur += 1
            if symbJoueur == 'O':
                symbJoueur = 'X'
                numJoueur -= 1
                currentPlayer = j1
            else:
                symbJoueur = 'O'
                numJoueur += 1
                currentPlayer = "Ordinateur"
            MorpionCode.clearPrompt()  # Nettoie l'écran avant d'afficher la grille
            MorpionCode.PrintTabVisu()

            if symbJoueur == 'X':
                # Saisie des coordonnées où placer le symbole du joueur (avec vérifications)
                verif = False
                while verif is False:
                    print("-=XOXOXOXOXO=- {} -=XOXOXOXOXO=-".format(currentPlayer))
                    tabVisu, tabCalc, verif = MorpionCode.SetInTable(symbJoueur)
                    if verif is False:
                        print('Cette case est déjà prise!')
            else:
                tabVisu, tabCalc = MorpionCode.TourIA(symbJoueur)

            victoire = MorpionCode.CalcVictoire()
        MorpionCode.clearPrompt()
        MorpionCode.PrintTabVisu()

        # En cas de victoire d'un joueur
        if victoire is True:
            print('{} remporte la partie!'.format(currentPlayer))
        # En cas d'égalité
        else:
            print('Égalité entre les deux joueurs')

        # Demande si le(s) joueurs souhaitent rejouer
        continuer = True
        while continuer:
            try:
                rep = input('Désirez-vous continuer à jouer contre l\'ordinateur ? (oui/non) : ')
                if rep.lower() == "oui":
                    jouer = rep.lower()
                    break
                elif rep.lower() == "non":
                    MorpionCode.clearPrompt()
                    jouer = rep.lower()
                    break
                else:
                    print("Entrez une réponse valide ...")
            except Exception:
                print("Entrez une réponse valide ...")
                continue


if __name__ == "__main__":  # Permet de lancer uniquement ce fichier si c'est celui-ci qui est explicitement exécuté (Afin de tester).
    JvsIA()
