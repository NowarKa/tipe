import numpy as np
import matplotlib.pyplot as plt
import constantes
import equations
from classes import partie


def score(part: partie.Partie):
    alpha = part.vitesse_initiale.angle * (np.pi / 180)
    coordonnees_quilles_copy = constantes.COORDONNEES_QUILLES.copy()
    quillestombees = []
    t0 = 0
    y, x, t = part.y0, part.x0, t0
    for k in range(1, 11):
        plt.plot(constantes.COORDONNEES_QUILLES[k][0], constantes.COORDONNEES_QUILLES[k][1],
                 marker='o', color='blue', markersize=20)

    while np.abs(y) < constantes.D_PISTE_Y and x < constantes.D_PISTE_X:
        (x, y) = equations.position(part, t, t0)
        if x > 18:
            plt.plot(x, y, marker='.', markersize=10)
            for quille in coordonnees_quilles_copy:
                if coordonnees_quilles_copy[quille][0] > x and equations.toucher_quille(part, quille, t, t0):
                    (x2, y2) = coordonnees_quilles_copy[quille]
                    beta = np.arctan((y2 - y) / (x2 - x))
                    (v0, alpha) = equations.nouveau_traj(part, beta)
                    part.vitesse_initiale.angle = alpha
                    part.vitesse_initiale.norme = v0
                    t0 = t
                    part.x0 = x
                    part.y0 = y
                    coordonnees_quilles_copy[quille] = (0, 0)
                    quillestombees.append(quille)
                    #plt.plot(x, y, marker='.', markersize=50)
        t = t + 0.001
    plt.savefig("ancienne_modelisation")
    plt.show()
    print(quillestombees, x, y)
