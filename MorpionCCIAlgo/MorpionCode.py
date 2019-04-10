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

    verif = ''
    if tabCalc[tabSaisies[0] - 1][tabSaisies[1] - 1] == '':
        tabVisu[GetTabVisuCase(tabSaisies[0], 'line')][GetTabVisuCase(tabSaisies[1], 'col')] = ' ' + symbPlayer + ' '  # placement du symbole du joueur dans le tableau visuel
        tabCalc[tabSaisies[0] - 1][tabSaisies[1] - 1] = symbPlayer  # placement du symbole du joueur dans le tableau de calcul
        verif = 'true'
    else:
        verif = 'false'

    return tabVisu, tabCalc, verif


def GetTabVisuCase(saisie, strVerif):

    """
    Cette focntion a pour but de renvoyer la valeur de l'emplacement demandé dans tabVisu selon différents cas possibles
    Elle est aussi séparée en deux parties selon si c'est la valeur d'une ligne ou d'une colonne qui est demandée

    switcher est un dictionnaire, un tableau spécifique permettant de retrouver une valeur grâce à une "clé" (1 ou 2 par exemple)
    "switcher.get()" est la façon de récupérer la valeur en insérant la clé dans la parenthèse
    """

    if strVerif == 'line':  # si le numéro de la ligne est demandé
        switcher = {
            1: 2,
            2: 6,
            3: 10,
        }
    else:
        switcher = {
            1: 2,
            2: 6,
            3: 10,
        }

    return switcher.get(saisie)


def CalcVictoire(tabCalc):

    victoire = 'false'

    for x in range(0, 3):  # Boucle de vérification des lignes et des colonnes
        verifSigneCol = tabCalc[x][0]
        verifSigneLine = tabCalc[0][x]

        if (tabCalc[x][1] == verifSigneCol and tabCalc[x][2] == verifSigneCol and verifSigneCol != '' or tabCalc[1][x] == verifSigneLine and tabCalc[2][x] == verifSigneLine and verifSigneLine != ''):
            victoire = 'true'

    # Déclaration de variables nécessaires à la vérification des diagonales
    lineDiagBasDroite = [tabCalc[1][1], tabCalc[2][2]]
    lineDiagBasGauche = [tabCalc[1][1], tabCalc[2][0]]

    verifSigneDiagBasDroite = tabCalc[0][0]
    verifSigneDiagBasGauche = tabCalc[2][0]

    if (verifSigneDiagBasDroite == lineDiagBasDroite[0] and verifSigneDiagBasDroite == lineDiagBasDroite[1] and verifSigneDiagBasDroite != '' or verifSigneDiagBasGauche == lineDiagBasGauche[0] and verifSigneDiagBasGauche == lineDiagBasGauche[1] and verifSigneDiagBasGauche != ''):
        victoire = 'true'

    return victoire


jouer = 'oui'
compteur = 0
while jouer == 'oui':
    # Initialisation des variables nécessaires à chaque parties
    compteur = 0
    symbJoueur = 'O'
    numJoueur = 2
    victoire = 'false'
    tabVisu = NewTabVisu()
    tabCalc = NewTabCalc()

    while victoire != 'true' and compteur <= 9:

        # Initialisation des variables nécessaires à chaque tours
        compteur += 1
        if symbJoueur == 'O':
            symbJoueur = 'X'
            numJoueur -= 1
        else:
            symbJoueur = 'O'
            numJoueur += 1

        PrintTabVisu(tabVisu)

        # Saisie des coordonnées où placer le symbole du joueur (avec vérifications)
        verif = 'false'
        while verif == 'false':
            tabVisu, tabCalc, verif = SetInTable(tabVisu, tabCalc, symbJoueur)
            if verif == 'false':
                print('Cette case est déjà prise!')

        victoire = CalcVictoire(tabCalc)

    PrintTabVisu(tabVisu)

    # En cas de victoire d'un joueur
    if victoire == 'true':
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