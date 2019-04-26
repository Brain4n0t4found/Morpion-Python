from random import *

def NewTabVisu():  # création du visuel de la grille
    print('\n' * 60)
    tabVisu = [[' -', '-', '---', '-', '---', '-', '---', '-', '---', '-', '---', '-', '- '],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               [' -', '-', '---', '-', '---', '-', '---', '-', '---', '-', '---', '-', '- '],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               [' -', '-', '---', '-', '---', '-', '---', '-', '---', '-', '---', '-', '- '],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               ['| ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' | ', ' ', '   ', ' ', ' |'],
               [' -', '-', '---', '-', '---', '-', '---', '-', '---', '-', '---', '-', '- ']]
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


def SetInTable(tabVisu, tabCalc, symbPlayer):
    tabSaisies = ['', '']

    for compt in range(2):
        strAdapt = ['ligne', 'colonne']
        saisie = 0  # initialisation de saisie pour rentrer dans le while

        while saisie < 1 or saisie > 3:
            saisie = str(input('Veuillez entrez le numéro de la ' + strAdapt[compt] + ' où placer votre marqueur (1 à 3): '))  # récupération de la saisie de l'utilisateur

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
                    print('La saisie n\'est pas un nombre!')  # si même la conversion en float n'a pas réussi
                saisie = 0

        tabSaisies[compt] = saisie  # sauvegarde de la saisie

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
    #  Test

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
    verifSigneDiagBasGauche = tabCalc[2][0]

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
    else:  # Le joueur n'aura pu placer qu'un symbole auparavant, pas besoin de prendre en comptre son premier symbole dans les vérifs.

        listSymbX = []  # Listes contenant toutes les coordonnées où les symboles apparaissent
        listSymbO = []
        for line in range(0, 3):
            for col in range(0, 3):
                if tabCalc[line][col] == 'X':
                    listSymbX.append([line, col])
                elif tabCalc[line][col] == 'O':
                    listSymbO.append([line, col])

        CheckSymb('O', listSymbO)
        CheckSymb('X', listSymbX)

    return tabVisu, tabCalc

def CheckSymb(symb, listSymb):

    for elementToCompare in range(0, listSymb.length):
        for comparison in range(0, listSymb.length):
            if listSymb[elementToCompare][0] == listSymb[comparison][0] and elementToCompare != comparison:  # Si les deux éléments sont sur la même ligne
                LookForMissingSymbPlace([listSymb[elementToCompare][1], listSymb[comparison][1]])  # Envoi de la colonne des éléments
            elif listSymb[elementToCompare][1] == listSymb[comparison][1] and elementToCompare != comparison:  # Sinon si sur la même colonne
                LookForMissingSymbPlace([listSymb[elementToCompare][0], listSymb[comparison][0]])  # Envoi de la ligne des éléments

    return

def LookForMissingSymbPlace(tabCoords):

    """
    Cette fonction a pour but de renvoyer la valeur non comprise dans tabCoords, afin que l'IA sache ou essayer de
    placer le symbole afin d'effectuer une victoire ou un blocage
    """

    if 0 not in tabCoords:
        return 0
    elif 1 not in tabCoords:
        return 1
    else:
        return 2

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


jouer = 'oui'
while jouer == 'oui':
    # Initialisation des variables nécessaires à chaque parties
    compteur = 0
    symbJoueur = 'O'
    numJoueur = 2
    victoire = False
    tabVisu = NewTabVisu()
    tabCalc = NewTabCalc()

    while victoire != True and compteur <= 9:

        # Initialisation des variables nécessaires à chaque tours
        compteur += 1
        if symbJoueur == 'O':
            symbJoueur = 'X'
            numJoueur -= 1
        else:
            symbJoueur = 'O'
            numJoueur += 1

        PrintTabVisu(tabVisu)

        if symbJoueur == 'X':
            # Saisie des coordonnées où placer le symbole du joueur (avec vérifications)
            verif = False
            while verif == False:
                tabVisu, tabCalc, verif = SetInTable(tabVisu, tabCalc, symbJoueur)
                if verif == False:
                    print('Cette case est déjà prise!')
        else:
            tabVisu, tabCalc = TourIA(tabVisu, tabCalc, symbJoueur)

        victoire = CalcVictoire(tabCalc)

    PrintTabVisu(tabVisu)

    # En cas de victoire d'un joueur
    if victoire == True:
        print('Le joueur ' + str(numJoueur) + ' remporte la partie!')
    # En cas d'égalité
    else:
        print('Égalité entre les deux joueurs')

    # Demande si le(s) joueurs souhaitent rejouer
    rep = ''
    while rep.lower() != "oui" and rep.lower() != "non":
        rep = input('Désirez-vous continuer à jouer ? (oui/non) : ')
        if rep.lower() != "oui" and rep.lower() != "non":
            print('Veuillez entrer oui ou non!')
    jouer = rep.lower()