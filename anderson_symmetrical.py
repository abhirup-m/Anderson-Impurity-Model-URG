#!/bin/python
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import os

colors = ['r', 'b', 'g', 'y']
mng = plt.get_current_fig_manager()
mpl.rcParams["savefig.directory"] = os.chdir(os.path.dirname(__file__))

for U in range(1,22,5):
    V = 0.1
    V2 = 0.1
    D_o = 100000
    b = 0.999999999999
    w = (D_o - U)/4
    D = D_o
    col = colors[0]
    colors = colors[-1:] + colors[0:-1]
    for i in range(100):
        den = U**2 - (4*w - 2*D)**2
        U += 32*U*D*V**2/den
        V += -D*V*V2/(U + 4*w - 2*D)
        plt.scatter(U, V, marker='.', color=col)
        D *= b
        if den * (U**2 - (4*w - 2*D)**2) <=0 or U <=0:
            break
    print (i)
    print (U,V)
plt.xlabel("U")
plt.ylabel("V")
plt.show()
