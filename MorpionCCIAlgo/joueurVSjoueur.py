import MorpionCode
import Visu


def JvsJ():
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
    jouer = 'oui'
    while jouer == 'oui':
        # Initialisation des variables nécessaires à chaque parties
        compteur = 0
        symbJoueur = 'O'
        numJoueur = 2
        victoire = False
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
                currentPlayer = j2

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

            if symbJoueur == 'O':
                # Saisie des coordonnées où placer le symbole du joueur (avec vérifications)
                verif = False
                while verif is False:
                    print("-=XOXOXOXOXO=- {} -=XOXOXOXOXO=-".format(currentPlayer))
                    tabVisu, tabCalc, verif = MorpionCode.SetInTable(symbJoueur)
                    if verif is False:
                        print('Cette case est déjà prise!')

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
                rep = input('Désirez-vous continuer à jouer ? (oui/non) : ')
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
    JvsJ()
