from random import *

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

tabCalc = [['', '', ''],
            ['', '', ''],
            ['', '', '']]

# ==================================================================================================
# ==================================================================================================
def NewTabVisu():  # création du visuel de la grille
    print('\n' * 60)
    return tabVisu
# ==================================================================================================
# ==================================================================================================


def NewTabCalc():  # création de la grille de calcul
    return tabCalc
# ==================================================================================================
# ==================================================================================================

def PrintTabVisu():
    for row in tabVisu:
        lineStr = ""  # preparation d'une chaine de caracteres retournant une ligne entière du tableau
        for e in row:  # pour chaque colonne dans la ligne
            lineStr += e  # Ajouter le contenu de la colonne suivante a la chaine de caracteres
        print(lineStr)
print(PrintTabVisu())
# ==================================================================================================
# ==================================================================================================
def SetInTable(symbPlayer):
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
