from Score import score
from classes import partie_test, vecteur
from classes.boule_test import Boule_test
from classes.vecteur import Vecteur
from score_sans_print_test import score
import matplotlib.pyplot as plt
from rad_degre import rad_deg


def trajectoire_optimale(tab_alpha, tab_v0, tab_x0, tab_y0):
    n = len(tab_alpha)
    m = len(tab_v0)
    l = []
    liste_quille = []
    for j in range(m):
        for i in range(n):
            b = Boule_test(13, Vecteur(tab_v0[j], tab_alpha[i]), (tab_x0[i], tab_y0[i]), 0)
            p = partie_test.Partie_test([b], Vecteur(tab_v0[j], tab_alpha[i]), tab_x0[i], tab_y0[i])
            quille_tombees = score(p)
            #plt.plot(tab_alpha[i], len(quille_tombees), color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
            #         markersize=5)
            if j == 9:
                l1 = [len(quille_tombees), (tab_v0[j], tab_alpha[i])]
                l.append(l1)
            #quille_tombees.append((tab_v0[j], tab_alpha[i]))
            liste_quille.append(len(quille_tombees))
        plt.title("vitesse initiale = 8 m/s , position initiale = 7 cm")
        plt.xlabel("angle (en degré)")
        plt.ylabel("nombre de quilles tombées")
        plt.plot(rad_deg(tab_alpha), liste_quille, 'o:r', color='black', markersize=7)
        plt.grid()
        plt.savefig("position_698_vitesse_8_lancers_500.pdf")
        plt.show()
    return liste_quille

def un_seul_lancer(alpha):
    l = []
    v0 = 13
    x0 = 0
    y0 = 0.0689
    b = Boule_test(13, Vecteur(v0, alpha), (x0, y0), 0)
    p = partie_test.Partie_test([b], Vecteur(v0, alpha), x0, y0)
    quille_tombees = score(p)
    #plt.plot(tab_alpha[i], len(quille_tombees), color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
    #         markersize=5)
    #quille_tombees.append((tab_v0[j], tab_alpha[i]))
    """plt.title("vitesse initiale = 13 m/s , position initiale = 6.89 cm")
    plt.xlabel("angle (en rad)")
    plt.ylabel("nombre de quilles tombées")
    plt.plot(tab_alpha, liste_quille, 'o:r', color='black', markersize=7)
    plt.grid()
    plt.savefig("position_698_vitesse_13_lancers_500.png")
    plt.show()"""
    return len(quille_tombees)

