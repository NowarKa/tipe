import numpy as np
from matplotlib import pyplot as plt

from classes.boule_test import Boule_test
from classes.partie_test import Partie_test
from classes.vecteur import Vecteur
from lancer_pro import score
import constantes


pas=(2*0.047/500)

def init_tab_alpha(y0,pas) :
    alphamin = -np.arctan( (y0 + constantes.D_PISTE_Y)/constantes.D_PISTE_X)
    alphamax = -np.arctan( (y0 - constantes.D_PISTE_Y)/constantes.D_PISTE_X)
    l=[]
    i=alphamin
    print (alphamin,alphamax)
    while i<= alphamax :
        l.append(i)
        i = i + pas
    return l



def statistique_angle(tab_alpha, tab_v0, tab_x0, tab_y0):
    n = len(tab_alpha)
    numstrike = 0
    for i in range(n):
        b = Boule_test(13, Vecteur(tab_v0[0], tab_alpha[i]), (tab_x0[i], tab_y0[i]), 0)
        p = Partie_test([b], Vecteur(tab_v0[0], tab_alpha[i]), tab_x0[i], tab_y0[i])
        quille_tombees = score(p)
        if len(quille_tombees) == 10:
            numstrike = numstrike + 1
    # plt.savefig("graph"+str(j))
    print("fini")
    return numstrike


def meilleur_lancer(tab_v0, tab_x0, tab_y0):
    n = len(tab_y0)
    tab_num = n * [0]
    plt.figure()
    for i in range(n):
        tab_alpha=np.array(init_tab_alpha(tab_y0[i],pas))
        tab_num[i] = statistique_angle(tab_alpha, tab_v0, tab_x0, len(tab_alpha)* [tab_y0[i]])
        print(len(tab_alpha))
        #print(tab_y0[i], tab_num[i])
    plt.plot(tab_y0, tab_num, 'r:o')
    plt.xlabel("y0 en m")
    plt.ylabel("nombre de strikes")
    plt.title("v0 = "+str(tab_v0[0])+" m/s")
    plt.grid()
    plt.show()
    plt.savefig("v0_"+str(tab_v0[0])+"_200_lancers.png")
    #return tab_num, tab_y0
    """plt.figure()
    plt.bar(tab_y0, tab_num, width=0.005)
    plt.xlabel("y0 en m")
    plt.ylabel("nombre de strikes")
    plt.title("v0 = "+str(tab_v0[0])+" m/s")
    plt.grid()
    plt.show()"""
