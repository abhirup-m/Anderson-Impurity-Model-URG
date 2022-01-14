#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
#plt.style.use('ggplot')

def rg2(w,D,U):
    d = 10
    delta = -2 * d * U /((w - D/2)*(w - D/2 + U))  # rg equation for |e_D|, with Delta (:= V^2  rho)=1
    if U * (U + delta) <= 0:
        return 0
    else:
        return U+delta

for w in np.arange(-20,20,0.1):
    for U0 in np.arange(0, 20, 0.1):
        U = U0
        D0 = 10
        N = 100
        #plt.title(r'$\omega = {}, U = {}, D = {}$'.format(w, U, D0))
        #plt.tight_layout()
        X = []
        Y = []
        den = w - D0/2 + U
        for D in np.linspace(D0, 0, N):
            X.append(N)
            Y.append(U)
            if den * (w - D0/2 + U) <= 0 or U == 0:
                if U > U0:
                    print (w, U0, U)
#            plt.plot(X, Y)
#            plt.scatter(X[0], Y[0], color='r', marker='o', label="start point")
#            plt.scatter(X[-1], Y[-1], color='g', marker='o', label="fixed point")
#            plt.show()
                break
            den = w - D0/2 + U
            U = rg2(w, D, U)
            N -= 1

#plt.legend()
#plt.xlabel(r'RG step')
#plt.ylabel(r'$|\epsilon_d|$')
##plt.show()
#plt.savefig("irr.png")
