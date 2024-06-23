import score_sans_print
from Score import score
from classes import partie, vecteur
from classes.boule import Boule
from classes.vecteur import Vecteur
from score_sans_print import score_sans_print
import matplotlib.pyplot as plt
from rad_degre import rad_deg

def trajectoire_optimale_test(tab_alpha, tab_v0, tab_x0, tab_y0):
    n = len(tab_alpha)
    m = len(tab_v0)
    liste_quille = []
    l = []
    for j in range(m):
        for i in range(n):
            b = Boule(8, Vecteur(tab_v0[j], tab_alpha[i]), (tab_x0[i], tab_y0[i]))
            p = partie.Partie(b, Vecteur(tab_v0[j], tab_alpha[i]), tab_x0[i], tab_y0[i])
            quille_tombees, x, y = score_sans_print(p)
            if j == 9:
                l1 = [len(quille_tombees), (tab_v0[j], tab_alpha[i])]
                l.append(l1)
            plt.plot(rad_deg(tab_alpha[i]), len(quille_tombees), color='black', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='black',
                     markersize=5)
            quille_tombees.append((tab_v0[j], tab_alpha[i]))
            liste_quille.append(len(quille_tombees))
            plt.title("vitesse initiale = " + str(tab_v0[j]))
            plt.xlabel("angle (en degré)")
            plt.ylabel("nombre de quilles tombées")
        plt.savefig("graph_meilleur_lancer")
        plt.show()
    return liste_quille, l
