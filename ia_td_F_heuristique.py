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