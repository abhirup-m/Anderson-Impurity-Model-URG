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


def den(w, D, U, J, K):
    ''' Defines and evaluates all the
    denominators in the problem.'''

    d1 = w - 0.5 * D - U/2 + K/2
    d2 = w - 0.5 * D + U/2 + J/2
    d3 = w - 0.5 * D + J/4 + K/4

    return d1, d2, d3


def rg(w, D, U, V, J, K):
    '''Evaluates the change in each coupling 
    at a particular RG step.'''


    dens = den(w, D, U, J, K)
    deltaU = -4 * V**2 * (1/dens[0] - 1/dens[1]) - (3* (J**2 - K**2)/8) * D / dens[2]
    deltaV = (1/16) * K * V * (1/dens[0] - 1/dens[2]) - (3/4) * J * V * (1/dens[1] + 1/dens[2])
    deltaJ = - J**2 / dens[2]
    deltaK = - K**2 / dens[2]

    U = 0 if (U + deltaU) * U <= 0 else U + deltaU
    V = 0 if (V + deltaV) * V <= 0 else V + deltaV
    J = 0 if (J + deltaJ) * J <= 0 else J + deltaJ
    K = 0 if (K + deltaK) * K <= 0 else K + deltaK

    return U, V, J, K

def plot_all(X, Y, Y2, Z, W):
    '''plots U, J, K, V in separate plots'''
    fig, ax = plt.subplots(nrows=3)
    ax[0].plot(X, Y)
    ax[0].set_ylabel("J")
    ax[1].plot(X, Y2)
    ax[1].set_ylabel("K")
    ax[2].plot(X, Z)
    ax[2].set_ylabel("U")
    plt.tight_layout(pad=0,w_pad=0, h_pad=0)
    plt.show()


def all_flow():
    '''master function to call other functions'''
    for w in [4.7]:
        for J, K in [[1,1]]:
            U0 = 1
            Dmax = 10
            N = 1000
            V = 0.01
            J = 0.01
            K = 0.01
            U = U0
            #plt.title(r'$D = {}, V = {}, J = {}, \epsilon_d = {}, \omega = {}$'.format(Dmax, V, J, ed, w))
            old_den = den(w, Dmax, U, J, K)[2]
            X = []
            Y = []
            Y2 = []
            Z = []
            W = []
            step = N
            for D in np.linspace(Dmax, 0, N):
                X.append(step)
                Y.append(J)
                Y2.append(K)
                Z.append(U)
                W.append(V)
                new_den = den(w, D, U, J, K)[2]
                #print (np.round(old_den,4), np.round(new_den,4))
                if old_den * new_den <= 0:
                    print (w, U, J)
                    plot_all(X, Y, Y2, Z, W)
                    break
                old_den = new_den
                U, V, J, K = rg(w, D, U, V, J, K)
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
