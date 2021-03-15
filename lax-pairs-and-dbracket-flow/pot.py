#!/bin/python

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 25}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True

def rg2(w,D,J):
    delta = -J**2 /(w + D/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

fig, ax = plt.subplots(1,2)
for Dmax in [10]:
    J = 0.01
    N = 1000
    w = 10
    ax[0].set_title(r'Bare: $J = {}, N = {}, D = {}, \omega={}$'.format(J, N, Dmax, w))
    ax[1].set_title(r'Bare: $J = {}, N = {}, D = {}, \omega={}$'.format(J, N, Dmax, w))
    count = N
    X = []
    Y = []
    Z = []
    for D in np.linspace(Dmax,0,N):
        trace = J**2 * count
        X.append(count)
        Y.append(trace)
        Z.append(J)
        #plt.scatter(count, trace)
        den = w + D/2
        J = rg2(w, D, J)
        count -= 1
        if J == 0 or den * (w + D/2) <= 0:
            X.append(count)
            Y.append(trace)
            Z.append(J)
            break

print (J)
ax[0].plot(X, Y)
ax[0].set_xlabel(r'RG step')
ax[0].set_ylabel(r'Tr$[(\mathcal{H}_j^I)^2]$')
ax[1].plot(X, Z)
ax[1].set_xlabel(r'RG step')
ax[1].set_ylabel(r'$J$')
plt.show()
