#!/bin/python


import itertools
from math import sqrt
import multiprocessing as mp
from multiprocessing import Pool
#mp.set_start_method('spawn')

import matplotlib
#matplotlib.use('agg')
from matplotlib import pyplot as plt

import numpy as np

font = {'family' : 'Source Code Pro',
        'size'   : 10}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def den(w, D, U, J, K):
    ''' Defines and evaluates all the
    denominators in the problem.'''

    d0 = w - 0.5 * D - U/2 + K/2
    d1 = w - 0.5 * D + U/2 + J/2
    d2 = w - 0.5 * D + J/4 + K/4

    return d0, d1, d2


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

def plot_all(X, Y, xl="", yl=[], title=[], name=[]):
    '''plots U, J, K, V in separate plots'''
    #fig, ax = plt.subplots(nrows=3)
    #plt.gca().set_aspect('equal')
    for i in range(len(Y)):
        plt.figure(figsize=(10,11))
        plt.title(title[i])
        plt.plot(X, Y[i], lw=4)
        plt.ylabel(yl[i])
        plt.xlabel(xl)
        plt.subplots_adjust(top=0.908, bottom=0.098, left=1.000, right=1.393, hspace=0.2, wspace=0.2)
        plt.tight_layout()
        plt.savefig(name[i])
        #plt.show()
    exit()

def get_fp(args):
    (w, Dmax, U0, V0, J0, K0) = args
    N = int(Dmax*10)
    V = V0
    J = J0
    K = K0
    U = U0
    count = np.zeros(3)
    old_den = den(w, Dmax, U, J, K)[2]
    for D in np.linspace(Dmax, 0, N):
        new_den = den(w, D, U, J, K)[2]
        if old_den * new_den <= 0:
            if U > U0:
                count[0] += 1
            elif U < U0:
                if U != 0:
                    count[1] += 1
                else:
                    count[2] += 1
            break
        old_den = new_den
        U, V, J, K = rg(w, D, U, V, J, K)
    return [V0, count]


def all_flow():
    '''master function to call other functions'''
    sign = 1
    J0 = 0.3
    K0 = 0
    V0 = 0.5
    V0_range = np.arange(0.01,0.5,0.01)
    Dmax = 10

    data = itertools.product(np.arange(-Dmax/1, Dmax/1, 0.05), [Dmax], np.arange(0.05, 10.05, 0.05), V0_range, [J0], [K0])

    with Pool(processes=40) as pool:
        outp = pool.map(get_fp, data)
    
    plot_data = [np.zeros(3) for V0 in V0_range]
    for o in outp:
        plot_data[np.where(V0_range == o[0])[0][0]] += o[1]

    print ("1")
    for i in range(len(V0_range)):
        plt.scatter(V0_range[i], plot_data[i][0], marker='.')
        plt.scatter(V0_range[i], plot_data[i][2], marker='.')

    print ("2")
    plt.show()
    

        #plt.scatter(V0,tot_count[0],color='r',marker='.')
        #plt.scatter(V0,tot_count[1],color='g',marker='.')
        #plt.scatter(V0,tot_count[2],color='b',marker='.')
        #y.append(tot_count[0]/tot_count[2])

#    plt.plot(0,0,color='r',label=r'$U>U0$')
#    plt.plot(0,0,color='g',label=r'$U<U0$')
#    plt.plot(0,0,color='b',label=r'$U=0$')
#    plt.legend()
#    plt.title(r'$V_0 = {:.2f}, J_0 = {:.2f}, K_0 = {:.2f}, sign(U)={}$'.format(V0, J0, K0, sign))
#    name = "sign_U={}:J={}:K={}V={}:Dvscount_log.png".format(sign, J0, K0, V0)
#    plt.plot(range(1,6), y, marker='.')
#    plt.ylabel(r'fraction of relevant fixed points')
#    plt.xlabel(r'$\log_{10}D$')
#    plt.savefig(name, dpi=400)
    #plt.show()


all_flow()
