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

def rg2(w,D,J):
    delta = -2 * J**2 /(w - D/2 + J/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

J = -0.1
flag = False
D0 = 10
plt.title(r'bare values: $\epsilon_q = \epsilon = {}, J = {}$'.format(D0, J))
N = 1000
X = [N]
Y = [J]
for D in np.linspace(D0,0,N):
    N -= 1
    den = D - J/2
    J = rg1(D, J)
    if J == 0 or den * (D - J/2) <= 0:
        flag = True
        break
    X.append(N)
    Y.append(J)
if flag:
    plt.plot(X, Y)
    plt.xlabel(r'RG step')
    plt.ylabel(r'$J$')
    plt.scatter(X[0], Y[0], color='r', marker='o', label="start point")
    plt.scatter(X[-1], Y[-1], color='g', marker='o', label="fixed point")
    plt.legend()
    plt.show()
    #plt.savefig('match2.png',bbox_inches='tight', transparent="True", pad_inches=0)
