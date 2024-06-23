from classes.boule import Boule
from classes.quille import Quille
from classes.vecteur import Vecteur
from classes import partie
import constantes
import numpy as np


def position(self: partie.Partie, t, t0):
    return (self.vitesse_initiale.norme * np.cos(self.vitesse_initiale.angle) * (t - t0) + self.x0,
            self.vitesse_initiale.norme * np.sin(self.vitesse_initiale.angle) * (t - t0) + self.y0)


def toucher_quille(self: partie.Partie, q, t, t0):
    (x1, y1) = position(self, t, t0)
    (x2, y2) = constantes.COORDONNEES_QUILLES[q]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= (constantes.RAYON_BOULE + constantes.RAYON_QUILLE)


def nouveau_traj(self: partie.Partie, beta):
    a = (self.boule.poids() / constantes.MASSE_QUILLE) + 1

    b = -2 * (self.boule.poids() / constantes.MASSE_QUILLE) * self.vitesse_initiale.norme * np.cos(
        self.vitesse_initiale.angle) - 2 * \
        (np.sin(beta)) ** 2 * np.cos(self.vitesse_initiale.angle) * self.vitesse_initiale.norme + 2 * \
        self.vitesse_initiale.norme * np.sin(self.vitesse_initiale.angle) * np.sin(beta) * np.cos(beta)

    c = (self.boule.poids() / constantes.MASSE_QUILLE) * (
            self.vitesse_initiale.norme * np.cos(self.vitesse_initiale.angle)) ** 2 - \
        self.vitesse_initiale.norme ** 2 * (np.cos(beta)) ** 2 + self.vitesse_initiale.norme ** 2 * \
        (np.sin(self.vitesse_initiale.angle)) ** 2 * (np.cos(beta)) ** 2 + self.vitesse_initiale.norme ** 2 * \
        ((np.sin(beta) * np.cos(self.vitesse_initiale.angle)) ** 2) - 2 * self.vitesse_initiale.norme ** 2 * \
        np.sin(self.vitesse_initiale.angle) * np.cos(self.vitesse_initiale.angle) * np.sin(beta) * np.cos(beta)

    #vq = np.sqrt((m_boule/m_quille)*(v0**2 - v0_x**2 - v0_y**2))
    delta = b ** 2 - 4 * a * c
    v0_x = (-b - np.sqrt(delta)) / (2 * a)
    v0_y = np.tan(beta) * (v0_x - self.vitesse_initiale.norme * np.cos(self.vitesse_initiale.angle)) + \
           self.vitesse_initiale.norme * np.sin(self.vitesse_initiale.angle)
    alpha = np.arctan(v0_y / v0_x)
    v0 = np.sqrt(v0_x ** 2 + v0_y ** 2)
    return v0, alpha
