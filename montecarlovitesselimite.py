import numpy as np




hg=0.14
delta_hg=5*10**-3
rqb=5.7*10**-2
g=9.81
N=10000
def f() :
    tab_h=np.random.uniform(hg-delta_hg,hg+delta_hg,N)
    tab_R=np.sqrt(rqb**2+tab_h**2)
    tab_teta=np.arccos(rqb/tab_R)
    tab_v=(np.sqrt(2*g*tab_R*(1-np.sin(tab_teta))))/np.sin(tab_teta)
    v_lim=np.mean(tab_v)
    u_v=np.std(tab_v,ddof=1)
    print('v_lim = ',v_lim,' et u(v_lim) = ',u_v)
    return v_lim+u_v
