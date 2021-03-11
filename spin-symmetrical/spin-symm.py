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


def rg(w, D, ed, V, J):
    '''Evaluates the change in each coupling 
    at a particular RG step.'''

    dens = den(w, D, ed, J)

    deltaed = V**2 * (1/dens[0] + 1/dens[1] - 2/dens[2]) + (3 * J**2 / 8) * D * (1 / dens[3])
    deltaV = (-3/4) * J * V * (1/dens[2] + 1/dens[3])
    deltaJ = -J**2 * 1/dens[3]

    ed = 0 if (ed + deltaed) * ed <= 0 else ed + deltaed
    V = 0 if (V + deltaV) * V <= 0 else V + deltaV
    J = 0 if (J + deltaJ) * J <= 0 else J + deltaJ

    return ed, V, J


def all_flow():
    '''master function to call other functions'''
    for Dmax in [10]:
        w = -0.1
        N = 100
        V = 0.1
        J = 0.1
        ed = 4
        plt.title(r'Bare values: $V = {}, J = {}, \epsilon_d = {}, \omega = {}$'.format(V, J, ed, w))
        old_den = den(w, Dmax, ed, J)[3]
        X = []
        Y = []
        Z = []
        step = N
        for D in np.linspace(Dmax, 0, N):
            X.append(step)
            Y.append(J)
            Z.append(ed)
            new_den = den(w, D, ed, J)[3]
            if old_den * new_den <= 0: 
                break
            else:
                old_den = new_den

            ed, V, J = rg(w, D, ed, V, J)
            step -= 1

        print ("End: D*={}, J*={}".format(Dmax, D, J))
        ax.plot(X, Y, color="red")
        ax.set_ylabel(r'$J$', color="red")
        ax.scatter(X[0], Y[0], color="green", label="start")
        ax.scatter(X[-1], Y[-1], color="blue", label="end")
        ax2.plot(X, Z, color="orange")
        ax2.scatter(X[0], Z[0], color="green")
        ax2.scatter(X[-1], Z[-1], color="blue")
        ax2.set_ylabel(r'$\epsilon_d$', color="orange")
        ax.legend()
        plt.show()

fig,ax = plt.subplots()
ax2 = ax.twinx()
all_flow()
