#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
#plt.style.use('ggplot')

def rg1(D,J):
    delta = 2 * J**2 /(D - J/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

def rg2(w,D,e):
    delta = -4 * e /((w - D/2)**2 - e**2)
    if e * (e + delta) <= 0:
        return 0
    else:
        return e+delta

e = 10
flag = False
D0 = 10
N = 100
plt.title(r'bare values: $|\epsilon_d| = {}, D = {}, N={}$'.format(e, D0, N))
X = [N]
Y = [e]
w = 1
for D in np.linspace(D0,0,N):
    N -= 1
    den = (w - D/2)**2 - e**2
    e = rg2(w, D, e)
    if e == 0 or den * ((w - D/2)**2 - e**2) <= 0:
        print (e)
        flag = True
        break
    X.append(N)
    Y.append(e)
#if not flag:
#    quit()
plt.plot(X, Y)
plt.xlabel(r'RG step')
plt.ylabel(r'$|\epsilon_d|$')
plt.scatter(X[0], Y[0], color='r', marker='o', label="start point")
plt.scatter(X[-1], Y[-1], color='g', marker='o', label="fixed point")
plt.legend()
#plt.show()
plt.savefig('rel.png',bbox_inches='tight', transparent="True", pad_inches=0)
