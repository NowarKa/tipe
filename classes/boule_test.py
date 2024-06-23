import constantes
from classes.vecteur import Vecteur


class Boule_test:
    def __init__(self, numero, vitesse:Vecteur, position, t0: float):
        self.numero = numero
        self.vitesse = vitesse
        self.position = position

    def poids(self):
        return constantes.BOULE_NOMB_MASSE[self.numero]
