import constantes
from classes.vecteur import Vecteur


class Boule:
    def __init__(self, numero, vitesse:Vecteur, position):
        self.numero = numero
        self.vitesse = vitesse
        self.position = position

    def poids(self):
        return constantes.BOULE_NOMB_MASSE[self.numero]
