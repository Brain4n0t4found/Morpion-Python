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


def PrintTabVisu():
    global tabVisu
    for row in tabVisu:
        lineStr = ""  # preparation d'une chaine de caracteres retournant une ligne entière du tableau
        for e in row:  # pour chaque colonne dans la ligne
            lineStr += e  # Ajouter le contenu de la colonne suivante a la chaine de caracteres
        print(lineStr)


if __name__ == "__main__": # Permet de lancer uniquement ce fichier si c'est celui-ci qui est explicitement exécuté (Afin de tester).
    print(PrintTabVisu())