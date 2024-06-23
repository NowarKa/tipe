import numpy as np
from matplotlib import pyplot as plt

from classes.boule_test import Boule_test
from classes.partie_test import Partie_test
from classes.vecteur import Vecteur
from test_sans_print import score


def statistique_angle(tab_alpha, tab_v0, tab_x0, tab_y0, k, m):
    n = len(tab_alpha)
    numstrike = 0
    liste_quille = []
    for i in range(n):
        b = Boule_test(16, Vecteur(tab_v0[0], tab_alpha[i]), (tab_x0[i], tab_y0[i]), 0)
        p = Partie_test([b], Vecteur(tab_v0[0], tab_alpha[i]), tab_x0[i], tab_y0[i])
        quille_tombees = score(p)
        if len(quille_tombees) == 10:
            numstrike = numstrike + 1
    # plt.savefig("graph"+str(j))
    print(str(k)+"/"+str(m))
    return numstrike


def meilleur_lancer(tab_alpha, tab_v0, tab_x0, tab_y0):
    n = len(tab_alpha)
    tab_num = n * [0]
    plt.figure()
    for i in range(n):
        tab_num[i] = statistique_angle(tab_alpha, tab_v0, tab_x0, n * [tab_y0[i]], i, n)
        #print(tab_y0[i], tab_num[i])
    plt.plot(tab_y0, tab_num, 'r:o', color='black')
    plt.xlabel("y0 en m")
    plt.ylabel("nombre de strikes")
    plt.title("v0 = 8 m/s")
    plt.grid()
    plt.show()
    plt.savefig("v0_8_500_lancers.png")
    return tab_num, tab_y0

