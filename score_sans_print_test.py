import numpy as np
import matplotlib.pyplot as plt
import constantes
import equations_test
from classes import partie
from classes.boule import Boule
from classes.partie_test import Partie_test
from classes.vecteur import Vecteur
from classes.partie import Partie


def position_boule(b: Boule, t):
    return (b.vitesse.norme * np.cos(b.vitesse.angle) * 0.001 + b.position[0],
            b.vitesse.norme * np.sin(b.vitesse.angle) * 0.001 + b.position[1])


def score(part: Partie_test):
    alpha = part.vitesse_initiale.angle * (np.pi / 180)
    coordonnees_quilles_copy = constantes.COORDONNEES_QUILLES.copy()
    quillestombees = []
    y, x, t = part.y0, part.x0, 0
    """for k in range(1, 11):
        plt.plot(constantes.COORDONNEES_QUILLES[k][0], constantes.COORDONNEES_QUILLES[k][1],
                 marker='o', color='blue', markersize=10)"""

    while part.liste_boule:
        for boule in part.liste_boule:
            quille_a_supp = []
            xi, yi = boule.position
            boule.position = position_boule(boule, t)
            if np.abs(yi) > constantes.D_PISTE_Y or xi > constantes.D_PISTE_X:
                part.liste_boule.remove(boule)
            elif xi > 18:
                #plt.plot(xi, yi, marker='.', markersize=20)
                for quille in coordonnees_quilles_copy:
                    if coordonnees_quilles_copy[quille][0] > xi and equations_test.toucher_quille(boule, quille, t):
                        (x2, y2) = coordonnees_quilles_copy[quille]
                        beta = np.arctan((y2 - yi) / (x2 - xi))
                        (v0, alpha, vqi) = equations_test.nouveau_traj(boule, beta)
                        boule.vitesse.angle = alpha
                        #boule.x0 = xi
                        #part.y0 = yi
                        quille_en_boule = Boule(0, Vecteur(vqi, beta), (xi, yi))
                        quillestombees.append(quille)
                        part.liste_boule.append(quille_en_boule)
                        quille_a_supp.append(quille)
                for i in quille_a_supp:
                    del coordonnees_quilles_copy[i]
        t = t + 0.001
    #plt.show()
    return quillestombees
