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


def all_flow():
    '''master function to call other functions'''
    name=0
    sign = 1
    J0 = 0.6
    ratio = []
    for Dmax in [10,12, 14]:
        ratio.append([])
    #for J0,sign in itertools.product([0.6],[1]):
        name += 1
        K0 = 0.5
        plt.clf()
        for V0 in np.arange(0.00,1,0.05):
            print (V0)
            count = [0,0,0]
            plt.title(r'sign$(U)={},J={}, K={}$'.format(sign, J0, K0))
            for U0 in np.arange(sign*0.11, sign*10.1, sign*0.05):
                for w in np.arange(-5,5,0.05):
                    #Dmax = 11
                    N = Dmax*10
                    V = V0
                    J = J0
                    K = K0
                    U = U0
                    title = r'$[D_0,J_0,K_0,U_0,\omega] = {},{},{},{},{}$'.format(Dmax, J0, K0, U0, w)
                    old_den = den(w, Dmax, U, J, K)[2]
                    X = []
                    Y = []
                    Y2 = []
                    Z = []
                    W = []
                    step = N
                    for D in np.linspace(Dmax, 0, N):
                        X.append(step)
                        Y.append(J/J0)
                        Y2.append(K/K0)
                        Z.append(U/U0)
                        W.append(V)
                        new_den = den(w, D, U, J, K)[2]
                        #print (np.round(old_den,4), np.round(new_den,4))       
                        if old_den * new_den <= 0:
                            if U > U0:
                                count[0] += 1
                            elif U < U0:
                                count[1] += 1
                            else:
                                count[2] += 1

                            #plot_all(X, [Z], r'RG steps', [r'$\frac{U}{U_0}$'], [title], ["large_U.png"])
                            break
                        old_den = new_den
                        U, V, J, K = rg(w, D, U, V, J, K)
                        step -= 1
            #count = np.log10([c+1 for c in count])
            #plt.scatter(V0, count[0], marker='.', color='r')
            #plt.scatter(V0, count[1], marker='.', color='b')
            ratio[-1].append(count[1]/count[0])
        #plt.scatter(V0, count[0], marker='.', color='r', label=r'$U>U_0$')
        #plt.scatter(V0, count[1], marker='.', color='b', label=r'$U<U_0$')
    #plt.legend()
        
    for i in range(3):
        plt.plot(np.arange(0.00,1,0.05), ratio[i], label=r'$D_0={}$'.format(10+i), color=['r','g','b'][i])
    
    plt.xlabel(r'$V_0$')
    plt.ylabel(r'ratio of number of fixed points')
    plt.legend()
    plt.show()
        #plt.savefig(str(name)+".png")

        #print ("V={:.2f}".format(V0),"\t U>U0 {:3d}".format(count[0]),"\t U<U0 {:3d}".format(count[1]), "\t U=U0 {:3d}".format(count[2]))
            #print (w, J, U)
            #plot_all(X, [Y, Y2, Z], r'RG steps', [r'$\frac{J}{J_0}$', r'$\frac{K}{K_0}$', r'$\frac{U}{U_0}$'], [title]*3, ["J.png", "K.png", "U.png"])
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
