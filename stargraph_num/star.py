#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np

def rg(w,e,j,E):
    deltaE = -(j**2/4)*1/(w - e/2 + E/2 + j/4)
    if E * (E + deltaE) <= 0:
        return 0
    else:
        return E+deltaE


for w in range(0,50,1):
    N = 1000
    j = 0.4
    e = 2
    E = -2
    flag = False
    Y = X = []
    for i in range(N,0,-1):
        den = w - e/2 + E/2 + j/4
        if E == 0:
            flag = True
            break
        Y.append(E)
        X.append(i)
        E = rg(w,e,j,E)
        if den * (w - e/2 + E/2 + j/4) <= 0:
            flag = True
            break
    if flag:
        print (w)
        print (E)
        plt.plot(X,Y)
        plt.title("w={},E={}".format(w,E))
        plt.show()
