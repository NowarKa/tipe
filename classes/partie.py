from classes.boule import Boule
from classes.quille import Quille
from classes.vecteur import Vecteur


class Partie:
    def __init__(self, boule: Boule, vitesse_initiale: Vecteur, x0: float, y0: float):
        self.x0 = x0
        self.y0 = y0
        self.boule = boule
        self.vitesse_initiale = vitesse_initiale
