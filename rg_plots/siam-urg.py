#!/bin/python


import itertools
import time
from math import sqrt

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

font = {'family' : 'normal',
        'size'   : 15}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def plot(gx,gy,title):
    norm_gx = [gxi/abs(max(gx, key=abs)) for gxi in gx]
    norm_gy = [gyi/abs(max(gy, key=abs)) for gyi in gy]
    plt.scatter(gx, gy)
    plt.scatter(gx[-1], gy[-1], color='r')
    plt.xlabel(r'J')
    plt.ylabel(r'U')
    plt.title(title)
    plt.show()


def init_check_fp(w, D, U, V, J):
    ''' checks if any denominator is 0 at the 
    beginning, meaning we are starting from a fixed 
    point, and sets corresponding flag to 0.'''

    d = den(w, D, U, V, J)
    flags = [1 if di != 0 else 0 for di in d]
    return flags


def den(w, D, U, V, J):
    ''' Defines and evaluates all the 
    denominators in the problem.'''

    d1 = w - 0.5 * D + U/2 + J/4
    d2 = w - 0.5 * D - U/2
    d3 = w - 0.5 * D + U/2 - J/4
    return d1, d2, d3


def rg(w, D, U, V, J, flags):
    '''Evaluates the change in each coupling 
    at a particular RG step. Also checks if 
    any denominator changed sign.'''

    d = den(w ,D, U, V, J)
    d = [0.1 if flags[i] == 0 else d[i] for i in range(len(flags))]
    deltaU = 4 * V**2 * sqrt(D) * (1/d[0] - 1/d[1]) - J**2 * D * (1/8) * (5*1/d[0] + 1/d[2])
    deltaV = (-3/4) * J * sqrt(D) * V * 1/d[0]
    deltaJ = -J**2 * sqrt(D) * 1/d[0]
    U += deltaU
    V += deltaV
    J += deltaJ
    flags = check_fp(w, D, U, V, J, d, flags, [deltaU, deltaV, deltaJ])
    return U, V, J, flags

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
    N = 5000
    w_0 = np.linspace(-2,2,20,endpoint=True)
    D_0 = [1]
    V_0 = [2]
    J_0 = [1]
    U_0 = [1]
    flag = False
    for w,D0,U,V,J in itertools.product(w_0,D_0,U_0,V_0,J_0):
        title = r'$\omega={},D={},U={},V={},J={}$'.format(w,D0,U,V,J)
        U_arr, V_arr, J_arr = [U], [V], [J]
        print ("Start: w={}, D={}, U={}, V={}, J={}".format(w, D0, U, V, J))
        flags = init_check_fp(w, D0, U, V, J)
        for D in np.linspace(D0, 0, N):
            if flags[0] == 0:
                flag = True
                break
            U, V, J, flags = rg(w ,D, U, V, J, flags)
            U_arr.append(U)
            V_arr.append(V)
            J_arr.append(J)
        if flag:
           print ("End: w={}, U={}, V={}, J={}\n".format(w,U, V, J))
           plot(J_arr, U_arr, title)

all_flow()
