from classes.boule import Boule
from classes.quille import Quille
from classes.vecteur import Vecteur
from classes import partie, partie_test, boule_test
import constantes
import numpy as np


def position_boule(b: Boule, t):
    return (b.vitesse.norme * np.cos(b.vitesse.angle) * 0.001 + b.position[0],
            b.vitesse.norme * np.sin(b.vitesse.angle) * 0.001 + b.position[1])


def toucher_quille(b: Boule, q, t):
    (x1, y1) = position_boule(b, t)
    (x2, y2) = constantes.COORDONNEES_QUILLES[q]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= (constantes.RAYON_BOULE + constantes.RAYON_QUILLE)


def nouveau_traj(b: boule_test.Boule_test, beta):
    a_delta = (b.poids() / constantes.MASSE_QUILLE) + 1

    b_delta = -2 * (b.poids() / constantes.MASSE_QUILLE) * b.vitesse.norme * np.cos(
        b.vitesse.angle) - 2 * \
              (np.sin(beta)) ** 2 * np.cos(b.vitesse.angle) * b.vitesse.norme + 2 * \
              b.vitesse.norme * np.sin(b.vitesse.angle) * np.sin(beta) * np.cos(beta)

    c_delta = (b.poids() / constantes.MASSE_QUILLE) * (
            b.vitesse.norme * np.cos(b.vitesse.angle)) ** 2 - \
              b.vitesse.norme ** 2 * (np.cos(beta)) ** 2 + b.vitesse.norme ** 2 * \
              (np.sin(b.vitesse.angle)) ** 2 * (np.cos(beta)) ** 2 + b.vitesse.norme ** 2 * \
              ((np.sin(beta) * np.cos(b.vitesse.angle)) ** 2) - 2 * b.vitesse.norme ** 2 * \
              np.sin(b.vitesse.angle) * np.cos(b.vitesse.angle) * np.sin(beta) * np.cos(beta)

    delta = b_delta ** 2 - 4 * a_delta * c_delta
    v0_x = (-b_delta - np.sqrt(delta)) / (2 * a_delta)
    v0_y = np.tan(beta) * (v0_x - b.vitesse.norme * np.cos(b.vitesse.angle)) + \
           b.vitesse.norme * np.sin(b.vitesse.angle)
    alpha = np.arctan(v0_y / v0_x)
    vq = np.sqrt((b.poids() / constantes.MASSE_QUILLE) * (b.vitesse.norme ** 2 - v0_x ** 2 - v0_y ** 2))
    v0 = np.sqrt(v0_x ** 2 + v0_y ** 2)
    return v0, alpha, vq
