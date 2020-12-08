#!/bin/python

#   import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import os

colors = ['r', 'b', 'g', 'y']
mng = plt.get_current_fig_manager()
mpl.rcParams["savefig.directory"] = os.chdir(os.path.dirname(__file__))

#    for U in range(10,20,50):
#        V = 0.1
#        V2 = 0.1
#        D_o = 100000
#        b = 0.999999999999
#    for w in np.linspace(-300,300,20):
#        U = 1000
#        V = 0.1
#        V2 = 0.1
#        b = 0.999999999999
#        D = 10
#        col = colors[0]
#        colors = colors[-1:] + colors[0:-1]
#        for i in range(100):
#            den = U**2 - (4*w - 2*D)**2
#            U += 32*U*D*V**2/den
#            V += -D*V*V2/(U + 4*w - 2*D)
#            plt.scatter(V, U, marker='.', color=col)
#            D *= b
#            if den * (U**2 - (4*w - 2*D)**2) <=0 or U <=0:
#                break
#        print (w)
#        plt.show()
#        plt.clf()

#   U = 1000
#   V2 = 0.01
#   b = 0.9999
#   Do = 100
#   D = Do
# for i in range(10000):
#    den = D**2 - U**2/4
#    print (den)
#    U += 2*U*D*V2*Do/den
#    D *= b
#    if den * (D**2 - U**2/4) <=0:
#        print (D,U)
#        break


U = 100
V = 0.01
V2 = V
b = 0.9999
Do = 50
D = Do
for i in range(10):
    denU = D**2/4 - D*U + 15*U**2/16
    denV = D - 3*U/2
    print(U, V)
    U += 2*U*D*V/denU
    V += -V*V2*D/denV
    D *= b

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
