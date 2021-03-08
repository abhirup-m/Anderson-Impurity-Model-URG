#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 15}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
plt.style.use('ggplot')

def rg(w, D, ed):
    Delta = 1
    delta = Delta * (w**2 + 3 * D**2/4 - 2*w*D - 2*ed**2)/(((w - D/2)**2 - ed**2) * (w + D/2)) 
    if ed * (ed + delta) <= 0:
        return 0
    else:
        return ed+delta

def rg2(w,E,j):
    deltaE = (j**2/4)*1/(w - E/2)
    if E * (E + deltaE) <= 0:
        return 0
    else:
        return E+deltaE

for w in np.linspace(-1000,1000,1000):
    ed = -0.01
    N = 1000
    D0 = 100
    flag = False
    Y = []
    X = []
    plt.title(r"$\omega={}$".format(ed))
    for D in np.linspace(D0, 0, N):
        Y.append(ed)
        X.append(D)
        den = ((w - D/2)**2 - ed**2) * (w + D/2)
        E = rg(w,D,ed)
        if ed == 0 or den * ((w - D/2)**2 - ed**2) * (w + D/2) <= 0:
            flag = True
            break
    if flag:
        print (ed)
        plt.plot(X,Y,label=r'$\tilde\omega={}$'.format(w))
        plt.xlabel(r'$D$')
        plt.ylabel(r'$\epsilon_d$')
        plt.legend()
        plt.show()
