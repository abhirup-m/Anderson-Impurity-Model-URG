#!/bin/python


import itertools
from math import sqrt

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 15}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def plot(gx,gy,title):
    norm_gx = [gxi/max(gx) for gxi in gx]
    norm_gy = [gyi/max(gy) for gyi in gy]
    plt.scatter(norm_gx, norm_gy)
    plt.scatter(norm_gx[-1], norm_gy[-1], color='r')
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
    deltaU = 4 * V**2 * sqrt(D) * (flags[0]/d[0] - flags[1]/d[1]) - J**2 * D * (1/8) * (5*flags[0]/d[0] + flags[2]/d[2])
    deltaV = (-3/4) * J * sqrt(D) * V * flags[0]/d[0]
    deltaJ = -J**2 * sqrt(D) * flags[0]/d[0]
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
    if all(delta == 0 for delta in deltas):
        flags = [0] * len(flags)
        print ("Changes are zero.")
        return flags
    if all(abs(delta) < 10**(-10) for delta in deltas):
        flags = [0] * len(flags)
        print ("Changes are too small.")
        return flags
    for i in range(len(d_old)):
        if d_old[i] * d_new[i] <= 0:
            flags[i] = 0
            #print ("Flag[{}] reached zero.".format(i))
    return flags



def all_flow():
    '''master function to call other functions'''
    N = 10
    w_0 = np.arange(-2, 2, 0.5)
    D_0 = [1]
    V_0 = [0]
    J_0 = [0.5]
    U_0 = [1]
    for w, D0, U, V, J in itertools.product(w_0, D_0, U_0, V_0, J_0):
        title = r'$\omega={},D={},U={},V={},J={}$'.format(w,D0,U,V,J)
        U_arr, V_arr, J_arr = [U], [V], [J]
        print ("Start: w={}, D={}, U={}, V={}, J={}".format(w, D0, U, V, J))
        flags = init_check_fp(w, D0, U, V, J)
        for D in np.linspace(D0,0,10):
            if not 1 in flags:
                break
            U, V, J, flags = rg(w ,D, U, V, J, flags)
            U_arr.append(U)
            V_arr.append(V)
            J_arr.append(J)
        print ("End: U={}, V={}, J={}\n".format(U, V, J))
        plot(J_arr, U_arr, title)

all_flow()


"""

    for D0 in [1,10,100,1000]:
        for J0 in [0]:
            D = D0
            U = 1
            V = 2
            J = 0
            sign1 = D - J/4
            sign2 = D - U/2 - J/2
            sign3 = D - 3*J/4
            sign5 = U + J/2
            flag = False
            count = 0
            print (V, U)
            while D > 0:
            #    print (D-J/4,D - U/2 - J/2,D - 3*J/4)
            #    print (U)
                if sign1 * (D - J/4) <= 0:
                    break
                elif sign2 * (D - U/2 - J/2) <= 0:
                    #print ("found 2")
                    break
                elif sign3 * (D - 3*J/4) <= 0:
                    #print ("found 3")
                    break
                elif sign5 * U <= 0 and J0 == 0:
                    U = 0
                    break
                sign1 = D - J/4
                sign2 = D - U/2 - J/2
                sign3 = D - 3*J/4
                sign5 = U + J/2
                deltaU = V**2 * D**(1/2) * sign5 / (sign1 * sign2) + J**2 * D**(3/2) * (6 * D - 4 * J)/(sign1 * sign3)
                deltaJ = J**2 * D**(1/2) / (4 * sign1)
                deltaV = V * D**(1/2) * (3*J/4) / sign1
                if flag == False:
                    #count -= 1
                    U += deltaU
                J += deltaJ
                V += deltaV
                D *= b
            #    x.append(U)
            #    y.append(V)
                count += 1
            print (V,U)
            x.append(D0)
            y.append(U)
            #plt.plot(x,y,marker='o')
            if U < 0:
                print (U)
            ci += 1
    plt.plot(np.log10(x),y,marker='o')
    plt.xlabel(r'$\log_{10}D$')
    plt.ylabel(r'$U^*$')
    plt.title(r'Dependence of $U^*$ on $D$($V=0.1$)')
    plt.show()

"""
