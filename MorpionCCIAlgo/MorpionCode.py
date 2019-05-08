from random import *
from Visu import *

'''
Modifications que j'ai effectué:
- tabVisu et tabCalc deviennent des variables globales pour alléger la taille des fonctions.
- Supressions des arguments tabVisu, tabCalc dans les arguments des fonctions pour ne garder que le nécessaire.
- Ajout du module "os" pour clean l'écran avant chaque apparition de tabVisu
- Mise à la norme PEP8

'''


def SetInTable(symbPlayer):  # Permet d'enregistrer et vérifier la saisie du joueur puis de placer le marqueur selon les coordonnées
    global j1
    global j2
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
            except Exception:
                # essai de conversion de saisie en float
                try:
                    float(saisie)
                    print(saisie + ' est un nombre décimal, la saisie doit être un entier!')  # si la conversion en float a réussi
                except Exception:
                    print('La saisie n\'est pas un nombre!')  # si même la conversion en float n'a pas réussi
                saisie = 0

        tabSaisies[compt] = saisie  # sauvegarde de la saisie

    return PlaceInputs(tabSaisies, symbPlayer)  # placement du marqueur selon les deux saisies récupérées


def GetTabVisuCase(saisie):
    """
    Cette fonction a pour but de renvoyer la valeur de l'emplacement demandé dans tabVisu selon différents cas possibles
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


def PlaceInputs(tabSaisies, symbPlayer):

    if tabCalc[tabSaisies[0] - 1][tabSaisies[1] - 1] == '':
        tabVisu[GetTabVisuCase(tabSaisies[0])][GetTabVisuCase(tabSaisies[1])] = '  ' + symbPlayer + '  '  # placement du symbole du joueur dans le tableau visuel
        tabCalc[tabSaisies[0] - 1][tabSaisies[1] - 1] = symbPlayer  # placement du symbole du joueur dans le tableau de calcul
        verif = True
    else:
        verif = False

    return tabVisu, tabCalc, verif


def CalcVictoire():
    global tabCalc
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


def TourIA(symbIA):
    symbIAexist = False
    global tabCalc
    global tabVisu
    # Analyse de s'il y a déjà un symbole de l'IA dans la grille
    for line in tabCalc:
        for case in line:
            if case == symbIA:
                if symbIAexist is False:
                    symbIAexist = True

    if symbIAexist is False:  # Si ucun symbole de l'IA n'a été trouvé
        randPos = [1, 3, 5, 7, 9]
        verif = False
        while (verif is False):
            tabVisu, tabCalc, verif = PlaceInputs(DefCoordsIASymb(choice(randPos)), symbIA)

    else:
        listSymbX = []  # Listes contenant toutes les coordonnées où les symboles apparaissent
        listSymbO = []
        for line in range(0, 3):
            for col in range(0, 3):
                if tabCalc[line][col] == 'X':
                    listSymbX.append([line, col])  # Ajout des coordonnées dans la List
                elif tabCalc[line][col] == 'O':
                    listSymbO.append([line, col])  # Idem

        if not CheckSymb('O', listSymbO, tabVisu, tabCalc, symbIA):
            if not CheckSymb('X', listSymbX, tabVisu, tabCalc, symbIA):  # Si l'IA n'a pas pu placer un symbole de manière définie
                randPos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                verif = False
                while (verif is False):
                    tabVisu, tabCalc, verif = PlaceInputs(DefCoordsIASymb(choice(randPos)), symbIA)

    return tabVisu, tabCalc


def CheckSymb(symb, listSymb, tabVisu, tabCalc, symbIA):
    placementDef = False

    for elementToCompare in range(0, len(listSymb)):
        for comparison in range(0, len(listSymb)):
            if placementDef is False:
                if listSymb[elementToCompare][0] == listSymb[comparison][0] and elementToCompare != comparison:  # Si les deux éléments sont sur la même ligne

                    coordToAim = LookForMissingSymbPlace([listSymb[elementToCompare][1], listSymb[comparison][1]])
                    tabVisu, tabCalc, placementDef = PlaceInputs([listSymb[elementToCompare][0] + 1, coordToAim + 1], symbIA)  # Tentative de placement dans la grille

                elif listSymb[elementToCompare][1] == listSymb[comparison][1] and elementToCompare != comparison:  # Sinon si sur la même colonne

                    coordToAim = LookForMissingSymbPlace([listSymb[elementToCompare][0], listSymb[comparison][0]])
                    tabVisu, tabCalc, placementDef = PlaceInputs([coordToAim + 1, listSymb[elementToCompare][1] + 1], symbIA)  # Tentative de placement dans la grille

    return placementDef


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
