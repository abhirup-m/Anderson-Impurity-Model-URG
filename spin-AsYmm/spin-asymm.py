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


def den(w, D, ed, U, J):
    ''' Defines and evaluates all the
    denominators in the problem.'''

    d1 = w - 0.5 * D - ed - U + J/4
    d2 = w - 0.5 * D + ed + J/2
    d3 = w - 0.5 * D - ed + J/2
    d4 = w - 0.5 * D + J/4
    d5 = w - 0.5 * D + ed + U + J

    return d1, d2, d3, d4, d5


def rg(w, D, ed, U, V1, V0, J):
    '''Evaluates the change in each coupling 
    at a particular RG step.'''

    dens = den(w, D, ed, U, J)

    deltaed = V1**2 / dens[0] + V0**2 * (1/dens[1] - 1/dens[2]) + (3 * J**2 / 8) * D / dens[3]
    deltaU = V1**2 * (1/dens[4] - 1/dens[2]) + V0**2 * (1/dens[2] - 1/dens[1]) - (3 * J**2 / 4) * D / dens[3]
    deltaV1 = (-3/4) * J * V1 * (1/dens[3] + 1/dens[4])
    deltaV0 = (-3/4) * J * V0 * (1/dens[3] + 1/dens[2])
    deltaJ = -J**2 * 1/dens[3]

    ed = 0 if (ed + deltaed) * ed <= 0 else ed + deltaed
    U = 0 if (U + deltaU) * U <= 0 else U + deltaU
    V1 = 0 if (V1 + deltaV1) * V1 <= 0 else V1 + deltaV1
    V0 = 0 if (V0 + deltaV0) * V0 <= 0 else V0 + deltaV0
    J = 0 if (J + deltaJ) * J <= 0 else J + deltaJ

    return ed, U, V1, V0, J


def all_flow():
    '''master function to call other functions'''
    for Dmax in [2]:
        w = 4
        N = 100
        V1, V0 = 2.5, 2.5
        J = 0.5
        ed = 6
        U = 4
        title = r'$D = {}, V_1 = {}, V_0 = {}, J = {}, \epsilon_d = {}, U = {}, \omega = {}$'.format(Dmax, V1, V0, J, ed, U , w)
        old_den = den(w, Dmax, ed, U, J)[3]
        X = []
        Y = []
        Z = []
        step = N
        for D in np.linspace(Dmax, 0, N):
            X.append(step)
            Y.append(ed)
            Z.append(V0)
            new_den = den(w, D, ed, U, J)[3]
            if old_den * new_den <= 0: 
                break
            else:
                old_den = new_den

            ed, U, V1, V0, J = rg(w, D, ed, U, V1, V0, J)
            step -= 1

        print ("J*={:.1g}, V1*={:.1g}, V0*={:.1g}, ed* = {:.1g}, U* = {:.1g}".format(J, V1, V0, ed, U))
        plt.title(title+"\n"+r"$V_1^*={:.3g}, V_0^*={:.3g},J^*={:.3g}, \epsilon_d^* = {:.3g}, U^* = {:.3g}$".format( V1, V0,J, ed, U))
        ax.plot(X, Y, color="red")
        ax.set_ylabel(r'$\epsilon_d$', color="red")
        ax.scatter(X[0], Y[0], color="green", label="start")
        ax.scatter(X[-1], Y[-1], color="blue", label="end")
        ax2.plot(X, Z, color="orange")
        ax2.scatter(X[0], Z[0], color="green")
        ax2.scatter(X[-1], Z[-1], color="blue")
        ax2.set_ylabel(r'$V_0$', color="orange")
        ax.legend()
        plt.show()

fig,ax = plt.subplots()
ax2 = ax.twinx()
all_flow()
