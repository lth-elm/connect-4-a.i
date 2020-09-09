# -*- coding: utf-8 -*-
"""
Puissance 4 matrice 6x12.

xoxo C'est la puissance xoxo
"""


# _____________________________________________________________ Heuristique


def valeur_matrice(s):
    """Méthode appellant d'autre méthodes de calcul pour générer un score associé à une grille en particulier."""
    dimI = len(s)
    dimJ = len(s[0])
    somme = 0

    for j in range(dimJ):
        somme += colonne(s, j, dimI)
    somme += ligne1_1(s, dimI, dimJ) + ligne1_2(s, dimI, dimJ)
    somme += diagonale1_1(s, dimI, dimJ) + diagonale1_2(s, dimI, dimJ) + diagonale2_1(s, dimI, dimJ) + diagonale2_2(s, dimI, dimJ)

    return somme


def colonne(s, j, dimI):
    """Score sur une colonne."""
    i = dimI-1
    if s[0][j] != ' ' or s[i][j] == ' ':  # = X ou Y
        return 0

    while(s[i][j] != ' '):  # garder une position libre (première ligne de la grille) au dessus d'un alignement de 3
        if i == 0:
            return 0
        i -= 1

    compteur = 1
    xo = s[i+1][j]  # point de départ du comptage

    for ii in range(2, 4):  # on cherche a partir de cette hauteur (après la précédente) combien de fois d'affilé on a X en dessous
        if i+ii < dimI:
            if s[i+ii][j] == xo:
                compteur += 1
        else:  # xo ne correspond pas au précédent donc la suite est cassé, pas besoin d'aller plus loin en profondeur
            break
        if compteur == 3 and xo == 'X':
            return 100000
        elif compteur == 3:  # xo == 'O'
            return -100000

    if compteur == 2 and s[1][j] == ' ':  # garder deux position libre (deux première ligne de la grille) au dessus d'un alignement de 2
        return 1000 if xo == 'X' else -1000

    return 0


def ligne1_1(s, dimI, dimj):
    """Première ligne."""
    somme = 0
    dimJ = dimj-3
    i = dimI-1
    for j in range(dimJ):
        liste4 = []
        compteurO = 0
        compteurX = 0
        for jj in range(4):
            liste4.append(s[i][j+jj])
        compteurO = liste4.count('O')
        compteurX = liste4.count('X')
        if compteurO == 3 and compteurX == 0:
            somme -= 100000
        elif compteurO == 2 and compteurX == 0:
            if liste4[0] == ' ' and j+4 != dimj:
                if s[i][j+4] == ' ':
                    somme -= 5000000
            else:
                somme -= 1000
        elif compteurO == 0 and compteurX == 3:
            somme += 100000
        elif compteurO == 0 and compteurX == 2:
            if liste4[0] == ' ' and j+4 != dimj:
                if s[i][j+4] == ' ':
                    somme += 5000000
            else:
                somme += 1000

    return somme


def ligne1_2(s, dimI, dimJ):
    """Autre lignes (1ere exclue) et test profondeur."""
    somme = 0
    for i in range(dimI-1):  # deuxième lignes (d'en bas)
        for j in range(dimJ-3):
            tab = []
            tabinf = []
            for jj in range(4):
                tab.append(s[i][j+jj])  # tab rempli
                tabinf.append(s[i+1][j+jj])  # tab inferieur rempli

            if tab.count(' ') != 4:  # si tab pas vide
                if tab.count('O') == 3 and tab.count('X') == 0:  # tab contient que 3 O
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        somme -= 100000
                    else:  # tab inf pas rempli (3/4)
                        x = tabinf.index(' ')
                        compteurinf = 0  # compteur profondeur
                        ii = 0  # index descente profondeur
                        while(s[i+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                            compteurinf += 1
                            ii += 1
                            if i+ii+1 == dimI:
                                break
                        somme -= 100000 - (compteurinf*20)

                elif tab.count('X') == 3 and tab.count('O') == 0:  # tab contient que 3 X
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        somme += 100000
                    else:  # tab inf pas rempli (3/4)
                        x = tabinf.index(' ')
                        compteurinf = 0  # compteur profondeur
                        ii = 0  # index descente profondeur
                        while(s[i+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                            compteurinf += 1
                            ii += 1
                            if i+ii+1 == dimI:
                                break
                        somme += 100000 - (compteurinf*20)

                elif tab.count('O') == 2 and tab.count('X') == 0:  # tab contient que 2 O
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        if tab[0] == ' ' and j+4 != dimJ:
                            if s[i][j+4] == ' ' and s[i+1][j+4] != ' ':
                                somme -= 5000000
                        else:
                            somme -= 1000
                    elif tabinf.count(' ') == 1:  # tab inf pas rempli (3/4)
                        x = tabinf.index(' ')
                        compteurinf = 0  # compteur profondeur
                        ii = 0  # index descente profondeur
                        while(s[i+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                            compteurinf += 1
                            ii += 1
                            if i+ii+1 == dimI:
                                break
                        somme -= 1000 - (compteurinf*20)
                    elif tabinf.count(' ') == 2:  # si tab inferieur pas assez rempli(2/4)
                        somme -= 100

                elif tab.count('X') == 2 and tab.count('O') == 0:  # tab contient que 2 X
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        if tab[0] == ' ' and j+4 != dimJ:
                            if s[i][j+4] == ' ' and s[i+1][j+4] != ' ':
                                somme += 5000000
                        else:
                            somme += 1000
                    elif tabinf.count(' ') == 1:  # tab inf pas rempli (3/4)
                        x = tabinf.index(' ')
                        compteurinf = 0  # compteur profondeur
                        ii = 0  # index descente profondeur
                        while(s[i+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                            compteurinf += 1
                            ii += 1
                            if i+ii+1 == dimI:
                                break
                        somme += 1000 - (compteurinf*20)
                    elif tabinf.count(' ') == 2:  # si tab inferieur pas assez rempli(2/4)
                        somme += 100
    return somme


def diagonale1_1(s, dimI, dimJ):
    """Bas gauche, haut droit à la première ligne."""
    somme = 0
    i = dimI-1
    for j in range(dimJ-3):
        tab = []
        tabinf = []
        for jj in range(4):
            tab.append(s[i-jj][j+jj])
        for jj in range(3):
            tabinf.append(s[i-jj][j+jj+1])

        if tab.count('O') == 3 and tab.count('X') == 0:
            if tabinf.count(' ') == 0:
                somme -= 100000
            else:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i-x+ii == dimI:
                        break
                somme -= 100000 - (compteurinf)*20

        elif tab.count('X') == 3 and tab.count('O') == 0:
            if tabinf.count(' ') == 0:
                somme += 100000
            else:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i-x+ii == dimI:
                        break
                somme += 100000 - (compteurinf)*20

        elif tab.count('O') == 2 and tab.count('X') == 0:
            if tabinf.count(' ') == 0:
                somme -= 1000
            elif tabinf.count(' ') == 1:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i-x+ii == dimI:
                        break
                somme -= 1000 - (compteurinf)*20
            elif tabinf.count(' ') == 2:
                somme -= 100

        elif tab.count('X') == 2 and tab.count('O') == 0:
            if tabinf.count(' ') == 0:
                somme += 1000
            elif tabinf.count(' ') == 1:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i-x+ii == dimI:
                        break
                somme += 1000 - (compteurinf)*20
            elif tabinf.count(' ') == 2:
                somme += 100
    return somme


def diagonale1_2(s, dimI, dimJ):
    """Haut gauche, bas droit à la première ligne."""
    somme = 0
    i = dimI-4
    for j in range(dimJ-3):
        tab = []
        tabinf = []
        for jj in range(4):
            tab.append(s[i+jj][j+jj])
        for jj in range(3):
            tabinf.append(s[i+jj+1][j+jj])

        if tab.count('O') == 3 and tab.count('X') == 0:
            if tabinf.count(' ') == 0:
                somme -= 100000
            else:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i+x+ii+1 == dimI:
                        break
                somme -= 100000 - (compteurinf)*20

        if tab.count('X') == 3 and tab.count('O') == 0:
            if tabinf.count(' ') == 0:
                somme += 100000
            else:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i+x+ii+1 == dimI:
                        break
                somme += 100000 - (compteurinf)*20

        if tab.count('O') == 2 and tab.count('X') == 0:
            if tabinf.count(' ') == 0:
                somme -= 1000
            elif tabinf.count(' ') == 1:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i+x+ii+1 == dimI:
                        break
                somme -= 1000 - (compteurinf)*20
            elif tabinf.count(' ') == 2:
                somme -= 100

        if tab.count('X') == 2 and tab.count('O') == 0:
            if tabinf.count(' ') == 0:
                somme += 1000
            elif tabinf.count(' ') == 1:
                x = tabinf.index(' ')
                compteurinf = 0  # compteur profondeur
                ii = 0  # index descente profondeur
                while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                    compteurinf += 1
                    ii += 1
                    if i+x+ii+1 == dimI:
                        break
                somme += 1000 - (compteurinf)*20
            elif tabinf.count(' ') == 2:
                somme += 100
    return somme


def diagonale2_1(s, dimI, dimJ):
    """Bas gauche, haut droit à partir de la seconde ligne."""
    somme = 0
    for i in range(dimI-2, 2, -1):
        for j in range(dimJ-3):
            tab = []
            tabinf = []
            for jj in range(4):
                tab.append(s[i-jj][j+jj])
                tabinf.append(s[i-jj+1][j+jj])

            if tab.count('O') == 3 and tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 100000
                else:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i-x+ii+1 == dimI:
                            break
                    somme -= 100000 - (compteurinf)*20

            elif tab.count('X') == 3 and tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 100000
                else:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i-x+ii+1 == dimI:
                            break
                    somme += 100000 - (compteurinf)*20

            elif tab.count('O') == 2 and tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 1000
                elif tabinf.count(' ') == 1:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i-x+ii+1 == dimI:
                            break
                    somme -= 1000 - (compteurinf)*20
                elif tabinf.count(' ') == 2:
                    somme -= 100

            elif tab.count('X') == 2 and tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 1000
                elif tabinf.count(' ') == 1:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i-x+ii+1 == dimI:
                            break
                    somme += 1000 - (compteurinf)*20
                elif tabinf.count(' ') == 2:
                    somme += 100
    return somme


def diagonale2_2(s, dimI, dimJ):
    """Haut gauche, bas droit jusqu'à la seconde ligne."""
    somme = 0
    for i in range(dimI-4):
        for j in range(dimJ-3):
            tab = []
            tabinf = []
            for jj in range(4):
                tab.append(s[i+jj][j+jj])
                tabinf.append(s[i+jj+1][j+jj])

            if tab.count('O') == 3 and tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 100000
                else:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i+x+ii+1 == dimI:
                            break
                    somme -= 100000 - (compteurinf)*20

            if tab.count('X') == 3 and tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 100000
                else:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i+x+ii+1 == dimI:
                            break
                    somme += 100000 - (compteurinf)*20

            if tab.count('O') == 2 and tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 1000
                elif tabinf.count(' ') == 1:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i+x+ii+1 == dimI:
                            break
                    somme -= 1000 - (compteurinf)*20
                elif tabinf.count(' ') == 2:
                    somme -= 100

            if tab.count('X') == 2 and tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 1000
                elif tabinf.count(' ') == 1:
                    x = tabinf.index(' ')
                    compteurinf = 0  # compteur profondeur
                    ii = 0  # index descente profondeur
                    while(s[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                        compteurinf += 1
                        ii += 1
                        if i+x+ii+1 == dimI:
                            break
                    somme += 1000 - (compteurinf)*20
                elif tabinf.count(' ') == 2:
                    somme += 100
    return somme


# _____________________________________________________________ Fin heuristique


def Actions(s):
    """Retourner les positions libres."""
    action = []
    dimJ = len(s[0])
    for j in range(dimJ):
        if PlaceLibre(s, j):
            i = DernierJeton(s, j)
            action.append([i, j])
    return action


def PlaceLibre(s, j):
    """Observe si la colonne est jouable à partir de la première ligne."""
    if s[0][j] == " ":
        return True
    return False


def DernierJeton(s, j):
    """Renvoie la position jouable pour un jeton à une colonne donnée."""
    for i in range(len(s)):
        if s[i][j] != " ":
            return i-1  # ligne où l'on doit insérer le jeton selon la colonne entrée (-1 permet de le mettre au dessus)
    return len(s)-1


def TerminalTest_Ut(s, lastplayed, jetons):
    """Retourne vrai ou faux avec un score selon si la partie est finie ou non."""
    lpi, lpj = lastplayed[0], lastplayed[1]
    if lpi == -1:
        return False, None  # 1er jeton

    DI, DJ = len(s), len(s[0])

    puissance = 4  # --> puissance "4"

    # sur la colonne
    if lpi+puissance <= DI:
        xo = s[lpi][lpj]
        if all(s[lpi+a][lpj] == xo for a in range(1, puissance, 1)):
            if xo == 'X':
                return True, 5000000
            else:
                return True, -5000000

    # sur la ligne
    countligne = 1
    xo = s[lpi][lpj]

    for jdroite in range(1, puissance, 1):
        if lpj+jdroite == DJ or s[lpi][lpj+jdroite] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 5000000
        elif countligne == puissance and xo == 'O':
            return True, -5000000

    for jgauche in range(1, puissance, 1):
        if lpj-jgauche == -1 or s[lpi][lpj-jgauche] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 5000000
        elif countligne == puissance and xo == 'O':
            return True, -5000000

    # diagonale ascendante
    countligne = 1
    xo = s[lpi][lpj]

    for diagup in range(1, puissance, 1):
        if lpi-diagup == -1 or lpj+diagup == DJ or s[lpi-diagup][lpj+diagup] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 5000000
        elif countligne == puissance and xo == 'O':
            return True, -5000000

    for diagdown in range(1, puissance, 1):
        if lpi+diagdown == DI or lpj-diagdown == -1 or s[lpi+diagdown][lpj-diagdown] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 5000000
        elif countligne == puissance and xo == 'O':
            return True, -5000000

    # diagonale descendante
    countligne = 1
    xo = s[lpi][lpj]

    for diagdown in range(1, puissance, 1):
        if lpi+diagdown == DI or lpj+diagdown == DJ or s[lpi+diagdown][lpj+diagdown] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 5000000
        elif countligne == puissance and xo == 'O':
            return True, -5000000

    for diagup in range(1, puissance, 1):
        if lpi-diagup == -1 or lpj-diagup == -1 or s[lpi-diagup][lpj-diagup] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 5000000
        elif countligne == puissance and xo == 'O':
            return True, -5000000

    # toujours des jetons jouable
    if jetons != 0:
        return False, None

    return True, 0


# _______________________ MINIMAX

def removeCoup(s, a):  # Permet d'éviter les copies en ajoutant un coup dans une matrice, l'envoyer dans une fonction, puis retirer ce coup
    s[a[0]][a[1]] = " "
    return s


def MinimaxAlphaBeta(s, i, j, p, jetons):
    v = MaxValueAlphaBeta(s, float('-inf'), float('inf'), i, j, p, jetons)  # Max car c'est à son tour de jouer
    a = []           # v[0] est associé au score, les autres indexes, la position
    a.append(v[1])  # i
    a.append(v[2])  # j
    return a


def MaxValueAlphaBeta(s, alpha, beta, i, j, p, jetons):

    end, sc = TerminalTest_Ut(s, [i, j], jetons)
    if end:  # impossibilité de continuer
        return [sc, None, None]  # -1, 0 ou 1

    if p == 0:
        return [valeur_matrice(s), None, None]
    p -= 1

    v = [float('-inf'), None, None]  # initialiser v au "minimum" possible : il prendra une vrai valeur à la prochaine comparaison

    # position correspond à ce score
    for a in Actions(s):
        i, j = a[0], a[1]
        s[i][j] = 'X'
        jetons -= 1
        min_value = MinValueAlphaBeta(s, alpha, beta, i, j, p, jetons)[0]  # on récupère la première valeur qui correspond au score
        s = removeCoup(s, a)

        # Si le nouveau score est meilleur que le précédent on actualise la nouvel position, sinon on garde l'ancienne
        v = [max(v[0], min_value), i if min_value > v[0] else v[1], j if min_value > v[0] else v[2]]

        if v[0] >= beta:
            return v
        alpha = max(alpha, v[0])

    return v  # Retourne [-1, 0 ou 1 ; Position]


def MinValueAlphaBeta(s, alpha, beta, i, j, p, jetons):

    end, sc = TerminalTest_Ut(s, [i, j], jetons)
    if end:
        return [sc, None, None]  # -1, 0 ou 1

    if p == 0:
        return [valeur_matrice(s), None, None]
    p -= 1

    v = [float('inf'), None, None]

    for a in Actions(s):
        i, j = a[0], a[1]
        s[i][j] = 'O'
        jetons -= 1
        max_value = MaxValueAlphaBeta(s, alpha, beta, i, j, p, jetons)[0]
        s = removeCoup(s, a)

        v = [min(v[0], max_value), i if max_value < v[0] else v[1], j if max_value < v[0] else v[2]]

        if v[0] <= alpha:
            return v
        beta = min(beta, v[0])

    return v

# _______________________


def showMat(s):
    """Affiche la grille de jeu."""
    print("    ", end="")
    for numCol in range(len(s[0])):
        if numCol+1 < 10:
            print(numCol+1, end="   ")
        else:
            print(numCol+1, end="  ")
    print()

    for i in range(len(s)):
        print("  |", end=" ")
        for j in range(len(s[0])):
            print(s[i][j], end=" | ")
        print()
    print()


# ____________________________________________________________ MAIN

if __name__ == '__main__':

    print("\n\n---------- JEU DES PUISSANCES ----------\n\n")

    joueur = 0  # à 1 l'IA commence

    print("Vous jouez 'O'.", end=" ")
    if joueur == 0:
        print("A vous de commencer !\n")
    else:
        print("\n")

    mat = []
    for i in range(6):  # nb lignes
        mat.append([" " for j in range(12)])  # nb colonnes
    dimI, dimJ = len(mat), len(mat[0])

    showMat(mat)

    jetons = 42  # nombre de jetons à disposition
    p = 5  # profondeur
    i = -1
    j = -1
    while TerminalTest_Ut(mat, [i, j], jetons)[0] == False:  # index 0 de Terminal_Ut -> Vrai ou faux selon si la partie est finie

        if joueur % 2 == 0:
            j = -1
            while not (j in range(dimJ)):
                j = input("Poser dans la colonne : ")
                j = int(j)-1
            i = DernierJeton(mat, j)
            assert mat[i][j] == ' ', "Vous devez jouer une position libre"
            mat[i][j] = 'O'
            jetons -= 1
            print("\n")

        else:
            a = MinimaxAlphaBeta(mat, i, j, p, jetons)
            i = a[0]
            j = a[1]
            mat[i][j] = 'X'
            jetons -= 1
            print("\nColonne jouée : ", j+1, end="\n\n")

        showMat(mat)

        joueur += 1

    print()

    resultat = TerminalTest_Ut(mat, [i, j], jetons)[1]  # index 1 de Terminal_Ut -> Score final (victoire, défaite, nul)

    if resultat == 5000000:
        print(" . . . . . .  Vous avez perdu :(")

    elif resultat == -5000000:
        print(" ! ! ! ! ! !  Félicitations champion !")

    else:
        print(" - - - - - -  Wow it's a tie !!")
