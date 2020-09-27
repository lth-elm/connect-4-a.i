# -*- coding: utf-8 -*-
"""
Puissance 4 matrice 6x12.

xoxo C'est la puissance xoxo
"""

from ia_td_F_heuristique import *


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
    p = 4  # profondeur
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
