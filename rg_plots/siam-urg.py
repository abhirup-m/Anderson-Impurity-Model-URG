#!/bin/python


import itertools
from math import sqrt

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

font = {'family' : 'Source Code Pro',
        'size'   : 15}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def plot(gx, gy, title):
    norm_gx = [gxi/abs(max(gx, key=abs)) for gxi in gx]
    norm_gy = [gyi/abs(max(gy, key=abs)) for gyi in gy]
    plt.plot(gx, gy, ls="--")
    plt.scatter(gx[0], gy[0], color='g', label="start") # marking start point
    plt.scatter(gx[-1], gy[-1], color='r', label="end") # marking end point
    plt.xlabel(r'J')
    plt.ylabel(r'U')
    plt.legend()
    plt.title(title)
    plt.show()


def init_check_fp(w, D, U, V, J):
    ''' checks if any denominator is 0 at the
    beginning, meaning we are starting from a fixed
    point, and sets corresponding flag to 0.'''

    d = den(w, D, U, V, J)
    flags = [1 if di != 0 else 0 for di in d]
    return flags


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

    if (ed + deltaed) * ed <= 0:
        ed = 0
    else:
        ed += deltaed
    if (V + deltaV) * V <= 0:
        V = 0
    else:
        V += deltaV
    if (J + deltaJ) * J <= 0:
        J = 0
    else:
        J += deltaJ

    return ed, V, J

def check_fp(w, D, U, V, J, d, flags, deltas):
    ''' checks if any denominator has changed sign 
    during the flow. It also sets all flags to 
    0 if all renormalizations are 0. '''

    d_old = d
    d_new = den(w, D, U, V, J)
    for i in range(len(d_old)):
        if d_old[i] * d_new[i] <= 0:
            flags[i] = 0
    return flags



def all_flow():
    '''master function to call other functions'''
    for Dmax in [50]:
        for w in [-0.1]:
            N = 1000
            V = 0.1
            J = 0.8
            ed = -6
            plt.title(r'Bare values: $V={}, J={}, \epsilon_d={}, \omega={}, D = {}$'.format(V, J, ed, w, Dmax))
            old_den = den(w, Dmax, ed, J)[3]
            flag = False
            X = []
            Y = []
            Z = []
            for D in np.linspace(Dmax, 0, N):
                X.append(D)
                Y.append(J)
                Z.append(V)
                new_den = den(w, D, ed, J)[3]
                if old_den * new_den <= 0: 
                    flag = True
                    break
                else:
                    old_den = new_den

                ed, V, J = rg(w, D, ed, V, J)

            if flag is True: 
               #print ("End: Dmax={}, D*={}, J*={}".format(Dmax, D, J))
               #plt.plot(X, Y, label=r'$J$')
               #plt.scatter(X[0], Y[0], color="g", label="start")
               #plt.scatter(X[-1], Y[-1], color="r", label="end")
               print (V)
               plt.plot(X, Z, label=r'$V$')
               plt.plot(X, Y, label=r'$J$')
               #plt.scatter(X[0], Z[0], color="g")
               #plt.scatter(X[-1], Z[-1], color="r")
               plt.legend()
               plt.xlabel(r'$D$')
               plt.ylabel(r'$V$')
    plt.show()
all_flow()
