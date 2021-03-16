#!/bin/python


import itertools
from math import sqrt

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def den(w, D, ed, J):
    ''' Defines and evaluates all the
    denominators in the problem.'''

    d1 = w - 0.5 * D + ed + J/4
    d2 = w - 0.5 * D + ed + J/2
    d3 = w - 0.5 * D - ed + J/2
    d4 = w - 0.5 * D + J/4

    return d1, d2, d3, d4


def rg(w, D, ed, V, J, flags):
    '''Evaluates the change in each coupling 
    at a particular RG step.'''

    dens = den(w, D, ed, J)

    deltaed = V**2 * (flags[0]/dens[0] + flags[1]/dens[1] - 2*flags[2]/dens[2]) + (3 * J**2 / 8) * D * (flags[3] / dens[3])
    deltaV = (-3/4) * J * V * (flags[3]/dens[2] + flags[3]/dens[3])
    deltaJ = -J**2 * flags[3]/dens[3]

    ed = 0 if (ed + deltaed) * ed <= 0 else ed + deltaed
    V = 0 if (V + deltaV) * V <= 0 else V + deltaV
    J = 0 if (J + deltaJ) * J <= 0 else J + deltaJ

    return ed, V, J


def all_flow():
    '''master function to call other functions'''
    for Dmax in [10]:
        w = 1
        N = 10
        V = 1
        J = 1
        ed = -0.1
        plt.title(r'$D = {}, V = {}, J = {}, \epsilon_d = {}, \omega = {}$'.format(Dmax, V, J, ed, w))
        old_den = den(w, Dmax, ed, J)
        X = []
        Y = []
        Z = []
        step = N
        flags = [1, 1, 1, 1]
        for D in np.linspace(Dmax, 0, N):
            X.append(step)
            Y.append(J)
            Z.append(ed)
            new_den = den(w, D, ed, J)
            for i in range(len(old_den)):
                if old_den[i] * new_den[i] <= 0: 
                    flags[i] = 0
                if not 1 in flags:
                    break
            old_den = [den for den in new_den]
            ed, V, J = rg(w, D, ed, V, J, flags)
            step -= 1

        if 1 in flags:
            quit()
        
        print (sum(flags))
        print ("End: J*={}".format(J))
        ax.plot(X, Z, marker=".")
        ax.set_ylabel(r'$J$')
        ax.set_xlabel(r'$D$')
        ax.scatter(X[0], Z[0], color="green", label="start")
        ax.scatter(X[-1], Z[-1], color="red", label="end")
        #ax2.plot(X, Z, color="orange")
        #ax2.scatter(X[0], Z[0], color="green")
        #ax2.scatter(X[-1], Z[-1], color="blue")
        #ax2.set_ylabel(r'$\epsilon_d$', color="orange")
        ax.legend()
        plt.show()

fig,ax = plt.subplots()
#ax2 = ax.twinx()
all_flow()
plt.tight_layout()
#plt.savefig("af.png")
