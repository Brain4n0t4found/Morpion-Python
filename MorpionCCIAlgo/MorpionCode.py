from random import *
import os

def NewTabVisu():  # création du visuel de la grille
    print('\n' * 60)
    tabVisu = [['┌', '─', '─────', '─', '┬', '─', '─────', '─', '┬', '─', '─────', '─', '┐'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['├', '─', '─────', '─', '┼', '─', '─────', '─', '┼', '─', '─────', '─', '┤'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['├', '─', '─────', '─', '┼', '─', '─────', '─', '┼', '─', '─────', '─', '┤'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│', ' ', '     ', ' ', '│'],
               ['└', '─', '─────', '─', '┴', '─', '─────', '─', '┴', '─', '─────', '─', '┘']]
    return tabVisu

def NewTabCalc():  # création de la grille de calcul
    tabCalc = [['', '', ''],
               ['', '', ''],
               ['', '', '']]
    return tabCalc

def PrintTabVisu(tabVisu):
    for row in tabVisu:
        lineStr = ""  # preparation d'une chaine de caracteres retournant une ligne entière du tableau
        for e in row:  # pour chaque colonne dans la ligne
            lineStr += e  # Ajouter le contenu de la colonne suivante a la chaine de caracteres
        print(lineStr)

def SetInTable(tabVisu, tabCalc, symbPlayer, nomJoueur):
    tabSaisies = ['', '']
    compt = 0

    while compt < 2:
        strAdapt = ['ligne', 'colonne']
        saisie = 0  # initialisation de saisie pour rentrer dans le while

        while saisie < 1 or saisie > 3:
            saisie = str(input(nomJoueur + ', veuillez entrez le numéro de la ' + strAdapt[compt] + ' où placer votre marqueur (1 à 3) (tapez "cancel" pour annuler une saisie précédente): '))  # récupération de la saisie de l'utilisateur
            if saisie.lower() == 'cancel':
                tabSaisies = ['', '']
                compt = 0
                saisie = 0  # réinitialisation de saisie pour rentrer dans le while
            else:
                # essai de conversion de saisie en int
                try:
                    saisie = int(saisie)
                    if saisie < 1 or saisie > 3:  # si la conversion a réussi et que saisie n'est pas entre 1 et 3
                        print('Veuillez saisir un nombre entre 1 et 3!')

                # si la conversion a échoué
                except:
                    # essai de converison de saisie en float
                    try:
                        float(saisie)
                        print(saisie + ' est un nombre décimal, la saisie doit être un entier!')  # si la conversion en float a réussi
                    except:
                        print('La saisie n\'est pas valide!')  # si même la conversion en float n'a pas réussi
                    saisie = 0

        tabSaisies[compt] = saisie  # sauvegarde de la saisie
        compt += 1

    return PlaceInputs(tabSaisies, tabVisu, tabCalc, symbPlayer)  # placement du marqueur selon les deux saisies récupérées

def PlaceInputs(tabSaisies, tabVisu, tabCalc, symbPlayer):

    if tabCalc[tabSaisies[0] - 1][tabSaisies[1] - 1] == '':
        tabVisu[GetTabVisuCase(tabSaisies[0])][GetTabVisuCase(tabSaisies[1])] = ' ' + symbPlayer + ' '  # placement du symbole du joueur dans le tableau visuel
        tabCalc[tabSaisies[0] - 1][tabSaisies[1] - 1] = symbPlayer  # placement du symbole du joueur dans le tableau de calcul
        verif = True
    else:
        verif = False

    return tabVisu, tabCalc, verif

def GetTabVisuCase(saisie):

    """
    Cette focntion a pour but de renvoyer la valeur de l'emplacement demandé dans tabVisu selon différents cas possibles
    Elle est aussi séparée en deux parties selon si c'est la valeur d'une ligne ou d'une colonne qui est demandée

    switcher est un dictionnaire, un tableau spécifique permettant de retrouver une valeur grâce à une "clé" (1 ou 2 par exemple)
    "switcher.get()" est la façon de récupérer la valeur en insérant la clé dans la parenthèse
    """


    switcher = {
        1: 2,
        2: 6,
        3: 10
    }
    return switcher.get(saisie)

def CalcVictoire(tabCalc):

    victoire = False

    for x in range(0, 3):  # Boucle de vérification des lignes et des colonnes
        verifSigneCol = tabCalc[x][0]
        verifSigneLine = tabCalc[0][x]

        if (tabCalc[x][1] == verifSigneCol and tabCalc[x][2] == verifSigneCol and verifSigneCol != '' or tabCalc[1][x] == verifSigneLine and tabCalc[2][x] == verifSigneLine and verifSigneLine != ''):
            victoire = True

    # Déclaration de variables nécessaires à la vérification des diagonales
    lineDiagBasDroite = [tabCalc[1][1], tabCalc[2][2]]
    lineDiagBasGauche = [tabCalc[1][1], tabCalc[2][0]]

    verifSigneDiagBasDroite = tabCalc[0][0]
    verifSigneDiagBasGauche = tabCalc[0][2]

    # Vérification des diagonales
    if (verifSigneDiagBasDroite == lineDiagBasDroite[0] and verifSigneDiagBasDroite == lineDiagBasDroite[1] and verifSigneDiagBasDroite != '' or verifSigneDiagBasGauche == lineDiagBasGauche[0] and verifSigneDiagBasGauche == lineDiagBasGauche[1] and verifSigneDiagBasGauche != ''):
        victoire = True

    return victoire

def TourIA(tabVisu, tabCalc, symbIA):
    symbIAexist = False

    # Analyse de s'il y a déjà un symbole de l'IA dans la grille
    for line in tabCalc:
        for case in line:
            if case == symbIA:
                if symbIAexist == False:
                    symbIAexist = True


    if symbIAexist == False:  # Si ucun symbole de l'IA n'a été trouvé
        randPos = [1, 3, 5, 7, 9]
        verif = False
        while (verif == False):
            tabVisu, tabCalc, verif = PlaceInputs(DefCoordsIASymb(choice(randPos)), tabVisu, tabCalc, symbIA)

    else:
        listDiagHautGaucheCoord = [[0, 0], [1, 1], [2, 2]]  # Listes des emplacements des diagonales
        listDiagHautDroiteCoord = [[0, 2], [1, 1], [2, 0]]

        listSymbX = []  # Listes contenant toutes les coordonnées où les symboles apparaissent
        listSymbO = []
        listDiagHautGauche = []
        listDiagHautDroite = []

        for line in range(0, 3):
            for col in range(0, 3):
                if tabCalc[line][col] == 'X':
                    listSymbX.append([line, col])  # Ajout des coordonnées dans la List
                elif tabCalc[line][col] == 'O':
                    listSymbO.append([line, col])  # Idem

        FillListDiag(listDiagHautGaucheCoord, listDiagHautGauche, tabCalc)  # remplissage des listes de symboles en diagonale
        FillListDiag(listDiagHautDroiteCoord, listDiagHautDroite, tabCalc)

        if not CheckSymb('O', listSymbO, tabVisu, tabCalc, symbIA, listDiagHautDroite, listDiagHautGauche):
            if not CheckSymb('X', listSymbX, tabVisu, tabCalc, symbIA, listDiagHautDroite, listDiagHautGauche):  # Si l'IA n'a pas pu placer un symbole de manière définie
                randPos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                verif = False
                while (verif == False):
                    tabVisu, tabCalc, verif = PlaceInputs(DefCoordsIASymb(choice(randPos)), tabVisu, tabCalc, symbIA)

    return tabVisu, tabCalc

def FillListDiag(Coords, list, tabCalc):
    for element in Coords:
        if tabCalc[element[0]][element[1]] != '':
            list.append(element)

def CheckSymb(symb, listSymb, tabVisu, tabCalc, symbIA, listDiagHautDroite, listDiagHautGauche):
    placementDef = False

    for elementToCompare in range(0, len(listSymb)):
        for comparison in range(0, len(listSymb)):
            if placementDef == False:
                if listSymb[elementToCompare][0] == listSymb[comparison][0] and elementToCompare != comparison:  # Si les deux éléments sont sur la même ligne

                    coordToAim = LookForMissingSymbPlace('', [listSymb[elementToCompare][1], listSymb[comparison][1]])
                    tabVisu, tabCalc, placementDef = PlaceInputs([listSymb[elementToCompare][0] + 1, coordToAim + 1], tabVisu, tabCalc, symbIA)  # Tentative de placement dans la grille

                elif listSymb[elementToCompare][1] == listSymb[comparison][1] and elementToCompare != comparison:  # Sinon si sur la même colonne

                    coordToAim = LookForMissingSymbPlace('', [listSymb[elementToCompare][0], listSymb[comparison][0]])
                    tabVisu, tabCalc, placementDef = PlaceInputs([coordToAim + 1, listSymb[elementToCompare][1] + 1], tabVisu, tabCalc, symbIA)  # Tentative de placement dans la grille

    if len(listDiagHautDroite) == 2 and placementDef == False:
        if tabCalc[listDiagHautDroite[0][0]][listDiagHautDroite[0][1]] == tabCalc[listDiagHautDroite[1][0]][listDiagHautDroite[1][1]] and tabCalc[listDiagHautDroite[0][0]][listDiagHautDroite[0][1]] == symb:  # S'il s'agit du même symbole
            coordToAimLine, coordToAimCol = LookForMissingSymbPlace('right', [listDiagHautDroite[0][0], listDiagHautDroite[1][0]])
            tabVisu, tabCalc, placementDef = PlaceInputs([coordToAimLine + 1, coordToAimCol + 1], tabVisu, tabCalc, symbIA)  # Tentative de placement dans la grille

    if len(listDiagHautGauche) == 2 and placementDef == False:
        if tabCalc[listDiagHautGauche[0][0]][listDiagHautGauche[0][1]] == tabCalc[listDiagHautGauche[1][0]][listDiagHautGauche[1][1]] and tabCalc[listDiagHautGauche[0][0]][listDiagHautGauche[0][1]] == symb:  # S'il s'agit du même symbole
            coordToAimLine, coordToAimCol = LookForMissingSymbPlace('left', [listDiagHautGauche[0][0], listDiagHautGauche[1][0]])
            tabVisu, tabCalc, placementDef = PlaceInputs([coordToAimLine + 1, coordToAimCol + 1], tabVisu, tabCalc, symbIA)  # Tentative de placement dans la grille

    return placementDef

def DefCoordsIASymb(coord):

    # EMPLACEMENT DES COORDONNEES DANS LA GRILLE
    # |1|2|3|
    # |4|5|6|
    # |7|8|9|

    switcher = {
        1: [1, 1],  # Ici, les valeurs ont +1 car def PlaceInputs réduit de 1 les données qu'elle reçoit
        2: [1, 2],
        3: [1, 3],
        4: [2, 1],
        5: [2, 2],
        6: [2, 3],
        7: [3, 1],
        8: [3, 2],
        9: [3, 3]
    }
    return switcher.get(coord)

def LookForMissingSymbPlace(lineStartingPos, tabCoords):
    """
    Cette fonction a pour but de renvoyer la valeur non comprise dans tabCoords, afin que l'IA sache ou essayer de
    placer le symbole afin d'effectuer une victoire ou un blocage
    """
    if lineStartingPos == 'right':      # S'l s'agit de la diagonale partant de la droite
        if 0 not in tabCoords:
            return 2, 0
        elif 1 not in tabCoords:
            return 1, 1
        else:
            return 0, 2
    elif lineStartingPos == 'left':     # S'il s'agit de la diagonale partant de la gauche
        if 0 not in tabCoords:
            return 0, 0
        elif 1 not in tabCoords:
            return 1, 1
        else:
            return 2, 2
    else:                               # S'il s'agit d'une ligne ou d'une colonne
        if 0 not in tabCoords:
            return 0
        elif 1 not in tabCoords:
            return 1
        else:
            return 2

def GamePlayMenu():
    os.system('cls')
    print(" ")
    print("┌────────────────────────────────────────────────=Présentation=───────────────────────────────────────────────────┐")
    print("│Bonjour et bienvenue dans le jeu du morpion réalisé par le meilleur groupe du BTS SIO 2019 de la CCI Strasbourg. │")
    print("│Vous allez être projeté dans une expérience unique du jeu du morpion.                                            │")
    print("└────────────────────────────────────────────────=XOXOXOXOXOXO=───────────────────────────────────────────────────┘")
    print(" ")
    rep = ''
    while rep.lower() != 'oui' and rep.lower() != 'non':
        rep = input("Connaissez-vous les règles du morpion? (oui/non) : ")
        if rep.lower() != 'oui' and rep.lower() != 'non':
            print("N'allez pas cherche une réponse compliquée! Répondez juste par oui ou non!")
    if rep == 'oui':
        os.system('cls')
        print(" ")
        print("Très bien ! Avant de commencer à jouer vous allez devoir choisir votre mode de jeu.")
        print(" ")
        print("            -=XOXOXOXOXOXOXO=- Choisissez -=XOXOXOXOXOXOXO=-            ")
        print(" ")
        j1, j2, numModeJeu = ChoixModeJeuEtNoms()
    else:
        os.system('cls')
        print(" ")
        print("┌───────────────────────────────────────────────=Règles=─────────────────────────────────────────────────┐")
        print("│Les règles sont simples, vous allez devoir gagner en alignant votre symbole dans une grille de 3 par 3, │")
        print("│tout cela en moins de 10 tours. Avant de commancer à jouer vous allez devoir choisir votre mode de jeu. │")
        print("└───────────────────────────────────────────────=XOXOXO=─────────────────────────────────────────────────┘")
        print(" ")
        print("            -=XOXOXOXOXOXOXO=- Choisissez -=XOXOXOXOXOXOXO=-            ")
        print(" ")
        j1, j2, numModeJeu = ChoixModeJeuEtNoms()

    return j1, j2, numModeJeu

def ChoixModeJeuEtNoms():
    rep = 0
    while rep != 1 and rep != 2:
        print("Voulez-vous jouer en Joueur Contre Joueur (1) ou Joueur Contre IA (2) ? ")
        try:
            rep = int(input("Votre choix : "))
            if rep == 1:
                os.system('cls')
                print("Très bon choix, vous allez maintenant pouvoir choisir vos noms !")
                print(" ")
                print("-=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-")
                print(" ")
                j1 = input("Joueur 1 comment vous appelez vous ? ")
                os.system('cls')
                print(" ")
                print("-=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-")
                print(" ")
                j2 = input("Joueur 2 comment vous appelez vous ? ")
                os.system('cls')
                print(" ")
                print("{} vous jouez les X et {} vous jouez les O !".format(j1, j2))
                print("Bonne chance à vous deux et que le meilleur gagne !")
            elif rep == 2:
                os.system('cls')
                print("Choix intéressant, allez vous faire le poids ?")
                print(" ")
                print("-=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-")
                print(" ")
                j1 = input("Joueur 1 comment vous appelez vous ? ")
                j2 = 'L\'IA'  # afin de pouvoir renvoyer un j2 correspondant à l'ia
                os.system('cls')
                print("{} vous jouez les X et l'IA joue les O ! Bonne chance {} !".format(j1, j1))
            else:
                print("Veuillez entrer un numéro compris entre 1 et 2 s'il vous plaît!")
        except:
            print("Entrez un numéro entier je vous prie.")

    return j1, j2, rep

def QuestionsFin(j1, j2):
    # Demande si le(s) joueurs souhaitent rejouer
    repJouer = ''
    while repJouer.lower() != "oui" and repJouer.lower() != "non":
        repJouer = input('Désirez-vous continuer à jouer ? (oui/non) : ')
        if repJouer.lower() != "oui" and repJouer.lower() != "non":
            print('Veuillez entrer oui ou non!')

    if repJouer == 'oui':
        # Demande du mode de jeu à appliquer
        repNumModeJeu = 0
        while repNumModeJeu != 1 and repNumModeJeu != 2:
            print("Voulez-vous jouer en Joueur Contre Joueur (1) ou Joueur Contre IA (2) ? ")
            try:
                repNumModeJeu = int(input("Votre choix : "))
                if repNumModeJeu < 1 or repNumModeJeu > 2:
                    print("Veuillez entrer 1 ou 2 uniquement!")
            except:
                print("Veuillez entrer un numéro!")

        # Demande s'il faut changer les noms
        repNom = ''
        while repNom.lower() != "oui" and repNom.lower() != "non":
            repNom = input('Faut-il changer les noms des joueurs ? (oui/non) : ')
            if repNom.lower() != "oui" and repNom.lower() != "non":
                print('Veuillez entrer oui ou non!')
        if repNom.lower() == 'oui':
            j1, j2 = ChangerNoms(repNumModeJeu)
    else:
        repNumModeJeu = 0

    return repJouer, repNumModeJeu, j1, j2

def ChangerNoms(numModeJeu):
    if numModeJeu == 1:
        print("-=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-")
        print(" ")
        j1 = input("Joueur 1 comment vous appelez vous ? ")
        os.system('cls')
        print(" ")
        print("-=XOXOXOXOXO=- Joueur 2 -=XOXOXOXOXO=-")
        print(" ")
        j2 = input("Joueur 2 comment vous appelez vous ? ")
        os.system('cls')
        print(" ")
        print("{} vous jouez les X et {} vous jouez les O !".format(j1, j2))
        print("Bonne chance à vous deux et que le meilleur gagne !")
    else:
        print("-=XOXOXOXOXO=- Joueur 1 -=XOXOXOXOXO=-")
        print(" ")
        j1 = input("Joueur 1 comment vous appelez vous ? ")
        j2 = 'L\'IA'  # afin de pouvoir renvoyer un j2 correspondant à l'ia
        os.system('cls')
        print("{} vous jouez les X et l'IA joue les O ! Bonne chance {} !".format(j1, j1))

    return j1, j2


j1, j2, numModeJeu = GamePlayMenu()
jouer = 'oui'
while jouer == 'oui':
    # Initialisation des variables nécessaires à chaque parties
    compteur = 1
    symbJoueur = ' O '
    numJoueur = 2
    victoire = False
    tabVisu = NewTabVisu()
    tabCalc = NewTabCalc()

    while victoire != True and compteur <= 9:

        # Initialisation des variables nécessaires à chaque tours
        if symbJoueur == ' O ':
            symbJoueur = ' X '
            numJoueur -= 1
        else:
            symbJoueur = ' O '
            numJoueur += 1

        os.system('cls')
        PrintTabVisu(tabVisu)

        if symbJoueur == ' X ':
            # Saisie des coordonnées où placer le symbole du joueur (avec vérifications)
            verif = False
            while verif == False:
                tabVisu, tabCalc, verif = SetInTable(tabVisu, tabCalc, symbJoueur, j1)
                if verif == False:
                    print('Cette case est déjà prise!')
        else:
            if numModeJeu == 2:  # Si c'est une partie contre l'IA
                tabVisu, tabCalc = TourIA(tabVisu, tabCalc, symbJoueur)
            else:  # Si c'est une partie contre le joueur
                verif = False
                while verif == False:
                    tabVisu, tabCalc, verif = SetInTable(tabVisu, tabCalc, symbJoueur, j2)
                    if verif == False:
                        print('Cette case est déjà prise!')

        victoire = CalcVictoire(tabCalc)
        compteur += 1

    os.system('cls')
    PrintTabVisu(tabVisu)

    # En cas de victoire d'un joueur#
    if victoire == True:
        if numJoueur == 1:
            print(j1 + ' remporte la partie!')
        else:
            print(j2 + ' remporte la partie!')
    # En cas d'égalité
    else:
        print('Égalité entre ' + j1 + ' et ' + j2)

    jouer, numModeJeu, j1, j2 = QuestionsFin(j1, j2)
