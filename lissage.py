import numpy as np
import matplotlib.pyplot as plt


def lissage(tab_x, tab_y, pas):
    n = len(tab_y)
    lissage_y = []
    lissage_x = []
    for i in range(0, n-pas, pas):
        s = 0
        for k in range(i, min(i + pas, n - 1)):
            s = s + tab_y[k]
        s = s / pas
        lissage_y.append(s)
        lissage_x.append(tab_x[i + int(pas / 2)])
    plt.figure()
    plt.plot(lissage_x, lissage_y, 'b:o')
    plt.xlabel("y0 en m")
    plt.ylabel("nombre de strikes sur 500 lancers")
    plt.title('vo = 13 m/s')
    plt.grid()
    plt.savefig('lissage10_v0=13_n_16.png')
    plt.show()
