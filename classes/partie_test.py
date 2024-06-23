from classes.boule import Boule
from classes.quille import Quille
from classes.vecteur import Vecteur


class Partie_test:
    def __init__(self, liste_boule: list, vitesse_initiale: Vecteur, x0: float, y0: float):
        self.x0 = x0
        self.y0 = y0
        self.liste_boule = liste_boule
        self.vitesse_initiale = vitesse_initiale
