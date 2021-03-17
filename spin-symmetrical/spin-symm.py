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

    w1, w2 = w

    d1 = w1 + 0.5 * D + 2*ed - J/4
    d2 = w2 - 0.5 * D - ed + J/4

    return d1, d2


def rg(w, D, ed, V, J):
    '''Evaluates the change in each coupling 
    at a particular RG step.'''


    dens = den(w, D, ed, J)

    deltaed = 2 * V**2 * (J/4 - ed) / ((w[0] + D/2) * dens[0]) + (3 * J**2 / 8) * D / dens[1]
    deltaV = (3/4) * J * V * (1/dens[0] - 1/dens[1])
    deltaJ = -J**2 * 1/dens[1]

    ed = 0 if (ed + deltaed) * ed <= 0 else ed + deltaed
    V = 0 if (V + deltaV) * V <= 0 else V + deltaV
    J = 0 if (J + deltaJ) * J <= 0 else J + deltaJ

    return ed, V, J


def all_flow():
    '''master function to call other functions'''
    fig, ax = plt.subplots(2)
    for w1, w2 in itertools.product(np.arange(0.1,20,0.01),np.arange(-20,20,0.01)):
        Dmax = 10
        w = [w1, w2]
        N = 130
        V = 1
        J = 0.0
        ed = 0.1
        #plt.title(r'$D = {}, V = {}, J = {}, \epsilon_d = {}, \omega = {}$'.format(Dmax, V, J, ed, w))
        old_den = den(w, Dmax, ed, J)
        X = []
        Y = []
        Z = []
        step = N
        for D in np.linspace(Dmax, 0, N):
            X.append(step)
            Y.append(J)
            Z.append(ed)
            new_den = den(w, D, ed, J)
            #print (np.round(old_den,4), np.round(new_den,4))
            if old_den[0] * new_den[0] <= 0 and old_den[1] * new_den[1] <= 0:
                if ed > 0.1:
#                    ax[0].plot(X, Y, label="J")
#                    ax[1].plot(X, Z, label="ed")
#                    plt.legend()
#                    plt.show()
#                    plt.clf()
                    print ("End: w1 = {}, w2 = {}, J*={}, ed*={}".format(w1, w2, J, ed))
                break
            old_den = [den for den in new_den]
            ed, V, J = rg(w, D, ed, V, J)
            step -= 1

        #ax.plot(X, Z, marker=".")
        #ax.set_ylabel(r'$J$')
        #ax.set_xlabel(r'$D$')
        #ax.scatter(X[0], Z[0], color="green", label="start")
        #ax.scatter(X[-1], Z[-1], color="red", label="end")
        ##ax2.plot(X, Z, color="orange")
        ##ax2.scatter(X[0], Z[0], color="green")
        ##ax2.scatter(X[-1], Z[-1], color="blue")
        ##ax2.set_ylabel(r'$\epsilon_d$', color="orange")
        #ax.legend()
        #plt.show()

#fig,ax = plt.subplots()
#ax2 = ax.twinx()
all_flow()
#plt.tight_layout()
#plt.savefig("af.png")
