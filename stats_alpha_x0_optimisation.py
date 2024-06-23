from classes.boule_test import Boule_test
from classes.partie_test import Partie_test
from classes.vecteur import Vecteur
from test_sans_print import score


def statistique_angle(x):
    y0, tab_alpha = x
    n = len(tab_alpha)
    numstrike = 0
    v0 = 13
    x0 = 0
    for i in range(n):
        b = Boule_test(13, Vecteur(v0, tab_alpha[i]), (x0, y0), 0)
        p = Partie_test([b], Vecteur(v0, tab_alpha[i]), x0, y0)
        quille_tombees = score(p)
        if len(quille_tombees) == 10:
            numstrike = numstrike + 1
    return numstrike


