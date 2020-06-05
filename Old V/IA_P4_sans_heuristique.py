# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:17:38 2020

@author: laith
"""

# _____________________________________________________________ Heuristique


def valeur_matrice(s):
    dimI = len(s)
    dimJ = len(s[0])

    somme = 0

    for j in range(dimJ):
        somme += colonne(s, j, dimI)
    somme += ligne1_1(s, dimI, dimJ) + ligne1_2(s, dimI, dimJ)
    somme += diagonale1_1(s, dimI, dimJ) + diagonale1_2(s, dimI, dimJ) + diagonale2_1(s, dimI, dimJ) + diagonale2_2(s, dimI, dimJ)
    return somme


def colonne(s, j, dimI):
    i = dimI-1
    max3 = dimI-4
    max2 = dimI-3   #
    if s[0][j] == 'X' or s[0][j] == 'O':
        return 0

    while(s[i][j] != ' '):
        if i == 0:
            break
        i -= 1
    compteur = 0
    compteurO = 0
    if i <= max3:  # verif que la profondeur permet d avoir 3 X d affilé
        for ii in range(1, 4):  # on cherche a partir de cette hauteur combien de fois d'affilé on a X en dessous
            if s[i+ii][j] == 'X':
                compteur += 1
            if s[i+ii][j] == 'O':
                compteurO += 1
            if compteur == 3:
                return 100000  # ici on ne met pas compteur =2 pr simplifier car il peut y avoir 2 X en dessous mais pas forcement d'affilé
            if compteurO == 3:
                return -100000

    compteur = 0
    compteurO = 0
    if i >= 1 and i <= max2:  # !=dim-1 parce que si on est sur la ligne tout en haut ca ne sert a rien qu il y ait que 2 O d 'affilé en dessous il en faut 3 pour faire 4
        for ii in range(1, 3):
            if s[i+ii][j] == 'X':
                compteur += 1
            if s[i+ii][j] == 'O':
                compteurO += 1
            if compteur == 2:
                return 1000
            if compteurO == 2:
                return -1000
    return 0


def ligne1_1(s, dimI, dimj):
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
        if compteurO == 2 and compteurX == 0:
            somme -= 1000
        if compteurO == 0 and compteurX == 3:
            somme += 100000
        if compteurO == 0 and compteurX == 2:
            somme += 1000

    return somme


def ligne1_2(m, dimI, dimJ):
    somme = 0
    for i in range(dimI-1):
        for j in range(dimJ-3):
            tab = []
            tabinf = []
            for jj in range(4):
                tab.append(m[i][j+jj])  # tab rempli
                tabinf.append(m[i+1][j+jj])  # tab inferieur rempli

            if tab.count(' ') != 4:  # si tab pas vide

                if tab.count('O') == 3 and tab.count('X') == 0:  # tab contient que 3 O
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        somme -= 100000
                    if tabinf.count(' ') == 1:  # tab inf pas rempli (3/4)
                        for jj in range(4):
                            if m[i+1][j+jj] == ' ':  # boucle pr trouver colonne ou il manque jeton
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+ii+1][j+jj] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+ii+1 == dimI:
                                        break
                        somme -= 10000-(compteurinf*20)

                if tab.count('X') == 3 and tab.count('O') == 0:  # tab contient que 3 X
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        somme += 100000
                    if tabinf.count(' ') == 1:  # tab inf pas rempli (3/4)
                        for jj in range(4):
                            if m[i+1][j+jj] == ' ':  # boucle pr trouver colonne ou il manque jeton
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+ii+1][j+jj] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+ii+1 == dimI:
                                        break
                        somme += 10000-(compteurinf*20)

                if tab.count('O') == 2 and tab.count('X') == 0:  # tab contient que 2 O
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        somme -= 1000
                    if tabinf.count(' ') == 1:  # tab inf pas rempli (3/4)
                        for jj in range(4):
                            if m[i+1][j+jj] == ' ':  # boucle pr trouver colonne ou il manque jeton
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+ii+1][j+jj] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+ii+1 == dimI:
                                        break
                        somme -= 1000-(compteurinf*20)
                    if tabinf.count(' ') == 2:  # si tab inferieur pas assez rempli(2/4)
                        somme -= 100

                if tab.count('X') == 2 and tab.count('O') == 0:  # tab contient que 2 X
                    if tabinf.count(' ') == 0:  # tab inferieur rempli
                        somme += 1000
                    if tabinf.count(' ') == 1:  # tab inf pas rempli (3/4)
                        for jj in range(4):
                            if m[i+1][j+jj] == ' ':  # boucle pr trouver colonne ou il manque jeton
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+ii+1][j+jj] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+ii+1 == dimI:
                                        break
                        somme += 1000-(compteurinf*20)
                    if tabinf.count(' ') == 2:  # si tab inferieur pas assez rempli(2/4)
                        somme += 100
    return somme


def diagonale1_1(m, dimI, dimJ):
    somme = 0
    i = dimI-1
    for j in range(dimJ-3):
        tab = []
        tabinf = []
        for jj in range(4):
            tab.append(m[i-jj][j+jj])
        for jj in range(3):
            tabinf.append(m[i-jj][j+jj+1])

        if tab.count('O') == 3:
            if tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 100000
                else:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i-x+ii == dimI:
                                    break

                    somme -= 10000-(compteurinf)*20

        if tab.count('X') == 3:
            if tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 100000
                else:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i-x+ii == dimI:
                                    break

                    somme += 10000-(compteurinf)*20

        if tab.count('O') == 2:
            if tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 1000
                if tabinf.count(' ') == 1:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i-x+ii == dimI:
                                    break

                    somme -= 1000-(compteurinf)*20
                if tabinf.count(' ') == 2:
                    somme -= 100

        if tab.count('X') == 2:
            if tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 1000
                if tabinf.count(' ') == 1:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i-x+ii][j+x+1] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i-x+ii == dimI:
                                    break

                    somme += 1000-(compteurinf)*20
                if tabinf.count(' ') == 2:
                    somme += 100
    return somme


def diagonale1_2(m, dimI, dimJ):
    somme = 0
    i = dimI-4
    for j in range(dimJ-3):
        tab = []
        tabinf = []
        for jj in range(4):
            tab.append(m[i+jj][j+jj])
        for jj in range(3):
            tabinf.append(m[i+jj+1][j+jj])

        if tab.count('O') == 3:
            if tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 100000
                else:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i+x+ii+1 == dimI:
                                    break

                    somme -= 10000-(compteurinf)*20

        if tab.count('X') == 3:
            if tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 100000
                else:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i+x+ii+1 == dimI:
                                    break

                    somme += 10000-(compteurinf)*20

        if tab.count('O') == 2:
            if tab.count('X') == 0:
                if tabinf.count(' ') == 0:
                    somme -= 1000
                if tabinf.count(' ') == 1:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i+x+ii+1 == dimI:
                                    break

                    somme -= 1000-(compteurinf)*20
                if tabinf.count(' ') == 2:
                    somme -= 100

        if tab.count('X') == 2:
            if tab.count('O') == 0:
                if tabinf.count(' ') == 0:
                    somme += 1000
                if tabinf.count(' ') == 1:
                    for x in range(3):
                        if tabinf[x] == ' ':

                            compteurinf = 0  # compteur profondeur
                            ii = 0  # index descente profondeur
                            while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                compteurinf += 1
                                ii += 1
                                if i+x+ii+1 == dimI:
                                    break

                    somme += 1000-(compteurinf)*20
                if tabinf.count(' ') == 2:
                    somme += 100
    return somme


def diagonale2_1(m, dimI, dimJ):
    somme = 0
    compteurinf = 0
    for i in range(dimI-2, 2, -1):
        for j in range(dimJ-3):
            tab = []
            tabinf = []
            for jj in range(4):
                tab.append(m[i-jj][j+jj])
                tabinf.append(m[i-jj+1][j+jj])

            if tab.count('O') == 3:
                if tab.count('X') == 0:
                    if tabinf.count(' ') == 0:
                        somme -= 100000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i-x+ii+1 == dimI:
                                        break
                        somme -= 10000-(compteurinf)*20

            if tab.count('X') == 3:
                if tab.count('O') == 0:
                    if tabinf.count(' ') == 0:
                        somme += 100000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i-x+ii+1 == dimI:
                                        break
                        somme += 10000-(compteurinf)*20

            if tab.count('O') == 2:
                if tab.count('X') == 0:
                    if tabinf.count(' ') == 0:
                        somme -= 1000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i-x+ii+1 == dimI:
                                        break
                        somme -= 1000-(compteurinf)*20
                    if tabinf.count(' ') == 2:
                        somme -= 100

            if tab.count('X') == 2:
                if tab.count('O') == 0:
                    if tabinf.count(' ') == 0:
                        somme += 1000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i-x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i-x+ii+1 == dimI:
                                        break
                        somme += 1000-(compteurinf)*20
                    if tabinf.count(' ') == 2:
                        somme += 100
    return somme


def diagonale2_2(m, dimI, dimJ):
    somme = 0
    for i in range(dimI-4):
        for j in range(dimJ-3):
            tab = []
            tabinf = []
            for jj in range(4):
                tab.append(m[i+jj][j+jj])
                tabinf.append(m[i+jj+1][j+jj])

            if tab.count('O') == 3:
                if tab.count('X') == 0:
                    if tabinf.count(' ') == 0:
                        somme -= 100000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+x+ii+1 == dimI:
                                        break
                        somme -= 10000-(compteurinf)*20

            if tab.count('X') == 3:
                if tab.count('O') == 0:
                    if tabinf.count(' ') == 0:
                        somme += 100000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+x+ii+1 == dimI:
                                        break
                        somme += 10000-(compteurinf)*20

            if tab.count('O') == 2:
                if tab.count('X') == 0:
                    if tabinf.count(' ') == 0:
                        somme -= 1000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+x+ii+1 == dimI:
                                        break
                        somme -= 1000-(compteurinf)*20
                    if tabinf.count(' ') == 2:
                        somme -= 100

            if tab.count('X') == 2:
                if tab.count('O') == 0:
                    if tabinf.count(' ') == 0:
                        somme += 1000
                    if tabinf.count(' ') == 1:
                        for x in range(4):
                            if tabinf[x] == ' ':
                                compteurinf = 0  # compteur profondeur
                                ii = 0  # index descente profondeur
                                while(m[i+x+ii+1][j+x] == ' '):  # boucle pr descendre en prof
                                    compteurinf += 1
                                    ii += 1
                                    if i+x+ii+1 == dimI:
                                        break
                        somme += 1000-(compteurinf)*20
                    if tabinf.count(' ') == 2:
                        somme += 100
    return somme


# _____________________________________________________________ Fin heuristique


def Actions(s):  # Retourner positions libres
    action = []
    dimJ = len(s[0])
    for j in range(dimJ):
        if PlaceLibre(s, j):
            i = DernierJeton(s, j)
            action.append([i, j])
    return action


def PlaceLibre(s, j):
    if s[0][j] == " ":  # Regarde si la première ligne (tout en haut est vide ou non)
        return True
    return False


def DernierJeton(s, j):
    for i in range(len(s)):
        if s[i][j] != " ":
            return i-1  # ligne où l'on doit insérer le jeton selon la colonne entrée (-1 permet de le mettre au dessus)
    return len(s)-1


def TerminalTest_Ut(s, lastplayed, jetons):  # Retourne vrai ou faux selon si la partie est finie ou non

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
                return True, 1000000
            else:
                return True, -1000000

    # sur la ligne
    countligne = 1
    xo = s[lpi][lpj]

    for jdroite in range(1, puissance, 1):
        if lpj+jdroite == DJ or s[lpi][lpj+jdroite] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 1000000
        elif countligne == puissance and xo == 'O':
            return True, -1000000

    for jgauche in range(1, puissance, 1):
        if lpj-jgauche == -1 or s[lpi][lpj-jgauche] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 1000000
        elif countligne == puissance and xo == 'O':
            return True, -1000000

    # diagonale ascendante
    countligne = 1
    xo = s[lpi][lpj]

    for diagup in range(1, puissance, 1):
        if lpi-diagup == -1 or lpj+diagup == DJ or s[lpi-diagup][lpj+diagup] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 1000000
        elif countligne == puissance and xo == 'O':
            return True, -1000000

    for diagdown in range(1, puissance, 1):
        if lpi+diagdown == DI or lpj-diagdown == -1 or s[lpi+diagdown][lpj-diagdown] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 1000000
        elif countligne == puissance and xo == 'O':
            return True, -1000000

    # diagonale descendante
    countligne = 1
    xo = s[lpi][lpj]

    for diagdown in range(1, puissance, 1):
        if lpi+diagdown == DI or lpj+diagdown == DJ or s[lpi+diagdown][lpj+diagdown] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 1000000
        elif countligne == puissance and xo == 'O':
            return True, -1000000

    for diagup in range(1, puissance, 1):
        if lpi-diagup == -1 or lpj-diagup == -1 or s[lpi-diagup][lpj-diagup] != xo:
            break
        countligne += 1
        if countligne == puissance and xo == 'X':
            return True, 1000000
        elif countligne == puissance and xo == 'O':
            return True, -1000000

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
    print("    ", end="")
    for numCol in range(len(mat[0])):
        if numCol+1 < 10:
            print(numCol+1, end="   ")
        else:
            print(numCol+1, end="  ")
    print()

    for i in range(len(mat)):
        print("  |", end=" ")
        for j in range(len(mat[0])):
            print(mat[i][j], end=" | ")
        print()
    print()


# ____________________________________________________________ MAIN

if __name__ == '__main__':

    print("\n\n---------- JEU DES PUISSANCES ----------\n\n")

    joueur = 1  # à 1 l'IA commence

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

    jetons = 42
    p = 4  # profondeur
    i = -1
    j = -1
    while TerminalTest_Ut(mat, [i, j], jetons)[0] == False:

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
            print()

        showMat(mat)

        joueur += 1

    print()

    resultat = TerminalTest_Ut(mat, [i, j], jetons)[1]

    if resultat == 1000000:
        print(" . . . . . .  Vous avez perdu :(")

    elif resultat == -1000000:
        print(" ! ! ! ! ! !  Félicitations champion !")

    else:
        print(" - - - - - -  Wow it's a tie !!")
