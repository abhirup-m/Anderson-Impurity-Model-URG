#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
#plt.style.use('ggplot')

def rg1(D,e):
    delta = - 4 * e /(D**2/4 - e**2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

def rg2(w,D,e):
    delta = -4 * e /((w - D/2)**2 - e**2)  # rg equation for |e_D|, with Delta (:= V^2  rho)=1
    if e * (e + delta) <= 0:
        return 0
    else:
        return e+delta

e = 1
D0 = 10
N = 100
w = 1
plt.title(r'bare values: $\omega = {}, |\epsilon_d| = {}, D = {}$'.format(w, e, D0))
plt.tight_layout()
X = []
Y = []
den = (w - D0/2)**2 - e**2
for D in np.linspace(D0,0.001,N):
    print (den)
    X.append(N)
    Y.append(e)
    if den * ((w - D/2)**2 - e**2) <= 0 or e == 0:
        print ("D=", D)
        plt.plot(X, Y)
        plt.scatter(X[0], Y[0], color='r', marker='o', label="start point")
        plt.scatter(X[-1], Y[-1], color='g', marker='o', label="fixed point")
        break
    den = (w - D/2)**2 - e**2
    e = rg2(w, D, e)
    N -= 1

plt.legend()
plt.xlabel(r'RG step')
plt.ylabel(r'$|\epsilon_d|$')
#plt.show()
plt.savefig("irr.png")
