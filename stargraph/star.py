#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
#plt.style.use('ggplot')


def rg(w,e,j,E):
    deltaE = -(j**2/4)*1/(w - e/2 + E/2 + j/4)
    if E * (E + deltaE) <= 0:
        return 0
    else:
        return E+deltaE


def rg2(w,E,j):
    deltaE = (j**2/4)*1/(w - E/2)
    if E * (E + deltaE) <= 0:
        return 0
    else:
        return E+deltaE


for w in [2,1]:
    N = 200
    j = 0.5
    #e = 2
    E = -3
    flag = False
    Y = []
    X = []
    den = w - E/2
    Y.append(E)
    X.append(N)
    plt.title(r"$\epsilon_0$ (bare value)$={}, N = {}, J = {}$".format(E, N, j))
    for i in range(N-1,0,-1):
        den = w - E/2
        E = rg2(w,E,j)
        if E == 0 or den * (w - E/2) <= 0:
            flag = True
            break
        Y.append(E)
        X.append(i)
    if flag:
        print (X)
        plt.plot(X,Y,label=r'$\tilde\omega={}$'.format(w))
        plt.xlabel(r" RG step")
        plt.ylabel(r'$\epsilon_0$')
plt.legend()
#plt.show()
plt.savefig('match.png',bbox_inches='tight', transparent="True", pad_inches=0)
