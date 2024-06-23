import numpy as np
import matplotlib.pyplot as plt
import constantes
import equations_test

from classes.boule_test import Boule_test
from classes.partie_test import Partie_test
from classes.vecteur import Vecteur
from score_sans_print_test import score


b = Boule_test(13, Vecteur(8, -0.62), (0, 15, 0))
p = Partie_test([b], Vecteur(8, -0.62), 0, 15)
print(score(p))


def position_boule(b: Boule_test, t):
    if b.position[0] == 0:
        return ((-b.position[1]+constantes.D_PISTE_Y ) / np.tan(b.vitesse.angle)),(constantes.D_PISTE_Y)
    if b.position[0] < 18:
        return 18, np.tan(b.vitesse.angle) * (18 - b.position[0]) + b.position[1]
    else:
        if b.numero == 0:
            v = (b.vitesse.norme - (constantes.F_FROTT / constantes.MASSE_QUILLE) * 0.001)
            if v <= 0:
                v = 0
            b.vitesse.norme = v
            return v * np.cos(b.vitesse.angle) * 0.001 / 2 + b.position[0], v * np.sin(b.vitesse.angle) * 0.001 / 2 + \
                   b.position[1]
        else:
            return (b.vitesse.norme * np.cos(b.vitesse.angle) * 0.001 + b.position[0],
                    b.vitesse.norme * np.sin(b.vitesse.angle) * 0.001 + b.position[1])


def score(part: Partie_test):
    coordonnees_quilles_copy = constantes.COORDONNEES_QUILLES.copy()
    quillestombees = []
    y, x, t = part.y0, part.x0, 0
    for k in range(1, 11):
        plt.plot(constantes.COORDONNEES_QUILLES[k][0], constantes.COORDONNEES_QUILLES[k][1],
                 marker='o', color='red', markersize=25)

    while part.liste_boule:
        boule_a_supp = []
        for boule in part.liste_boule:
            xi, yi = boule.position
            boule.position = position_boule(boule, t)
            if np.abs(yi) > constantes.D_PISTE_Y or xi > constantes.D_PISTE_X or boule.vitesse.norme <= 0:
                boule_a_supp.append(boule)
            elif xi >= 18:
                quille_a_supp = []
                plt.plot(xi, yi, marker='.', markersize=5, color='green')
                for quille in coordonnees_quilles_copy:
                    if coordonnees_quilles_copy[quille][0] > xi and equations_test.toucher_quille(boule, quille, t):
                        (x2, y2) = coordonnees_quilles_copy[quille]
                        beta = np.arctan((y2 - yi) / (x2 - xi))
                        (v0, alpha, vqi) = equations_test.nouveau_traj(boule, beta)
                        boule.vitesse.angle = alpha
                        boule.vitesse.norme = v0
                        # boule.x0 = xi
                        # part.y0 = yi
                        quille_en_boule = Boule(0, Vecteur(vqi, beta), (xi, yi))
                        quillestombees.append(quille)
                        part.liste_boule.append(quille_en_boule)
                        quille_a_supp.append(quille)
                for i in quille_a_supp:
                    del coordonnees_quilles_copy[i]
        for i in boule_a_supp:
            part.liste_boule.remove(i)
        t = t + 0.001
        plt.show()
        print(quillestombees)
    return quillestombees


