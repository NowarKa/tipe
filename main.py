import matplotlib.pyplot as plt
import time
from multiprocessing import Pool
import sys
import Score
import model_final
import test_sans_print
from Score import score
from classes.boule import Boule
from classes.partie import Partie
from classes.partie_test import Partie_test
from classes.vecteur import Vecteur
from lissage import lissage
import trajectoire_optimale_test
import numpy as np
from score_sans_print_test import score
import test
import stats_alpha_x0_optimisation



tab_alpha = np.linspace(-0.047, 0.047, 500)
tab_v0 = np.array([13])
tab_y0 = np.linspace(0, 0.525, 500)
tab_x0 = np.zeros(500)
tab_y0_alpha = np.empty(500, dtype=object)
for i in range(500):
    tab_y0_alpha[i] = (tab_y0[i], tab_alpha)
tab_num0 = [84, 85, 85, 84, 84, 85, 84, 84, 85, 85, 84, 85, 85, 84, 84, 85, 84,
            84, 84, 84, 84, 85, 85, 84, 84, 85, 84, 84, 84, 84, 84, 85, 85, 84,
            85, 85, 84, 84, 84, 84, 84, 84, 85, 84, 85, 85, 84, 84, 84, 84, 84,
            84, 84, 84, 85, 85, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 84, 85,
            84, 84, 84, 84, 84, 84, 84, 85, 84, 85, 84, 84, 84, 84, 84, 84, 84,
            84, 84, 85, 85, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 84, 85, 84,
            84, 84, 84, 84, 84, 84, 85, 84, 85, 84, 84, 84, 84, 84, 84, 84, 84,
            84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84,
            84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 83, 84,
            84, 84, 84, 84, 84, 84, 84, 84, 83, 84, 84, 84, 84, 83, 84, 84, 84,
            84, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84,
            84, 84, 83, 84, 84, 84, 84, 83, 84, 84, 84, 84, 83, 84, 84, 84, 84,
            83, 84, 84, 84, 84, 83, 84, 84, 83, 84, 83, 84, 84, 84, 84, 84, 84,
            84, 83, 84, 83, 84, 84, 83, 84, 84, 84, 84, 83, 84, 83, 84, 84, 83,
            84, 84, 84, 84, 83, 84, 83, 83, 84, 83, 84, 84, 84, 84, 84, 84, 83,
            83, 84, 83, 84, 84, 83, 84, 84, 84, 83, 83, 84, 83, 83, 84, 83, 84,
            84, 84, 83, 83, 84, 83, 83, 84, 83, 84, 84, 84, 84, 83, 84, 83, 83,
            84, 83, 83, 84, 83, 84, 84, 84, 83, 83, 84, 83, 83, 84, 83, 84, 84,
            84, 83, 83, 84, 83, 83, 84, 83, 83, 84, 84, 83, 83, 84, 83, 83, 84,
            83, 83, 84, 83, 83, 84, 84, 83, 83, 84, 83, 83, 84, 83, 82, 84, 84,
            83, 83, 84, 83, 83, 84, 83, 82, 84, 84, 83, 83, 84, 83, 83, 84, 83,
            82, 84, 84, 82, 83, 84, 83, 83, 84, 83, 82, 84, 83, 82, 84, 84, 83,
            83, 84, 83, 82, 84, 83, 82, 84, 84, 82, 83, 84, 83, 83, 84, 83, 82,
            84, 84, 82, 83, 84, 83, 83, 84, 83, 82, 84, 83, 82, 83, 84, 83, 83,
            84, 83, 82, 84, 83, 82, 84, 84, 82, 83, 84, 83, 82, 84, 83, 82, 84,
            84, 82, 83, 84, 83, 82, 84, 83, 82, 84, 83, 82, 83, 84, 82, 82, 84,
            83, 82, 84, 83, 82, 83, 84, 82, 82, 84, 83, 82, 84, 83, 82, 84, 84,
            82, 82, 84, 82, 82, 84, 83, 82, 84, 83, 82, 82, 84, 82, 82, 84, 83,
            82, 84, 83, 82, 82, 84, 82, 82, 84, 82, 82, 84, 83, 82, 83, 84, 82,
            82, 84, 82, 82, 84, 83, 82]

if __name__ == '__main__':
    # l1, l3 = trajectoire_optimale_test(tab_alpha, tab_v0, tab_x0, tab_y0)
    # l2, l4 = trajectoire_optimale(tab_alpha, tab_v0, tab_x0, tab_y0)
    # plt.figure()
    # f.write(f"{l4}\n")
    # part = Partie_test([Boule(9, Vecteur(12, 0.01), (0, 0.0689))], Vecteur(12, 0.01), 0, 0.0689)
    # test.score(part)
    # part2 = Partie(Boule(9, Vecteur(12, 0.01), (0, 0)), Vecteur(12, 0.01), 0, 0)
    # test_sans_print.score(part)
    # trajectoire_optimale_test.trajectoire_optimale(tab_alpha, tab_v0, tab_x0, tab_y0)
    # Score.score(part2)
    # tab_num, tab_y = model_final.meilleur_lancer(tab_alpha, tab_v0, tab_x0, tab_y0)
    # print(tab_num)
    lissage(tab_y0, tab_num0, 10)
    # stat_pour_les_pros
    """t1 = time.time()
    with Pool() as pool:
        result = pool.map(stats_alpha_x0_optimisation.statistique_angle, tab_y0_alpha)
    t2 = time.time()
    print(t2 - t1)
    print(result)"""

