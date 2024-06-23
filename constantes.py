D_PISTE_X = 20  # m
D_PISTE_Y = 0.525  # m
RAYON_BOULE = 0.218 / 2  # m
RAYON_QUILLE = 0.1143 / 2  # m
MASSE_QUILLE = 1.5  # kg
"""MU_FROTT=0
g=9.81  #N/kg
POIDS_QUILLE=g*MASSE_QUILLE
F_FROTT=MU_FROTT*POIDS_QUILLE"""
F_FROTT = 3.4

BOULE_NOMB_MASSE = {0: MASSE_QUILLE,
                    6: 2.72,
                    7: 3.18,
                    8: 3.63,
                    9: 4.08,
                    10: 4.54,
                    11: 4.99,
                    12: 5.44,
                    13: 5.90,
                    14: 6.35,
                    15: 6.80,
                    16: 7.26, }
COORDONNEES_QUILLES = {1: (18.52, 0),
                       2: (18.78, -0.135),
                       3: (18.78, 0.135),
                       4: (19.04, -0.3),
                       5: (19.04, 0),
                       6: (19.04, 0.3),
                       7: (19.3, -0.475),
                       8: (19.3, -0.19),
                       9: (19.3, 0.19),
                       10: (19.3, 0.475)}
