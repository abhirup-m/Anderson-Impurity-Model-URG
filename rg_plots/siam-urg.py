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
    for Dmax in [10, 100, 1000, 10000, 100000, 1000000]:
        for ed in [4]:
            w = -Dmax/2
            N = 10*Dmax
            V = 1
            J = Dmax/5
            #ed = -5
            plt.title(r'Bare values: $V={}, J=D/5, \epsilon_d={}, \omega=-D/2$'.format(V, ed ))
            old_den = den(w, Dmax, ed, J)[3]
            flag = False
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
                    flag = True
                    break
                else:
                    old_den = new_den

                ed, V, J = rg(w, D, ed, V, J)
                step -= 1

            if flag is True: 
                x.append(np.log10(D))
                y.append(np.log10(J))
                #print ("End: Dmax={}, D*={}, J*={}".format(Dmax, D, J))
                #plt.plot(X, Y, label=r'$J$')
                #plt.scatter(X[0], Y[0], color="g", label="start")
                #plt.scatter(X[-1], Y[-1], color="r", label="end")
                #plt.plot(X, Z, label=r'$V$')
                #ax.plot(X, Y, color="darkgreen")
                #ax.set_ylabel(r'$J$', color='darkgreen')
                #ax2.plot(X,Z, color='brown')
                #ax2.set_ylabel(r'$\epsilon_d$',color='brown')
                #ax.set_xlabel(r'$\leftarrow$ RG step')
                #ax.scatter(X[0], Y[0], color="b", label="start")
                #ax.scatter(X[-1], Y[-1], color="gold", label="end")
                #ax.legend()
                #plt.show()
                #plt.savefig('ed_to_large2.png',bbox_inches='tight', transparent="True", pad_inches=0)

fig,ax = plt.subplots()
#ax2 = ax.twinx()
x,y = [], []
all_flow()
ax.scatter(x,y, label="fixed points")
ax.set_xlabel(r'$\log_{10}D$')
ax.set_ylabel(r'$\log_{10}J$')
linear_model=np.polyfit(x,y,1)
linear_model_fn=np.poly1d(linear_model)
print (x[0])
x_s=np.arange(1,7,1)
plt.plot(x_s,linear_model_fn(x_s),label="best fit", color="green")
plt.legend()
plt.show()
