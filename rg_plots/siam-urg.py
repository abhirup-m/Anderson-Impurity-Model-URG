#!/bin/python


import itertools
from math import sqrt
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 27}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True


def den(w ,D, U, V, J):
    d1 = w - 0.5 * D + U/2 + J/4
    d2 = w - 0.5 * D - U/2
    d3 = w - 0.5 * D + U/2 - J/4
    return d1, d2, d3


def rg(w, D, U, V, J, flags):
    b = 0.9999
    d = den(w ,D, U, V, J)
    deltaU = 4 * V**2 * sqrt(D) * (flags[0]/d[0] - flags[1]/d[1]) - J**2 * D * (1/8) * (5*flags[0]/d[0] + flags[2]/d[2])
    deltaV = (-3/4) * J * sqrt(D) * V * flags[0]/d[0]
    deltaJ = -J**2 * sqrt(D) * flags[0]/d[0]
    print (deltaU)
    U += deltaU
    V += deltaV
    J += deltaJ
    D *= b
    flags = check_den(w, D, U, V, J, d, flags)
    return D, U, V, J, flags

def check_den(w, D, U, V, J, d, flags):
    d_old = d
    d_new = den(w, D, U, V, J)
    #print (d_new)
    for i in range(len(d_old)):
        if d_old[i] * d_new[i] <= 0 or d_new[i] > 10**5:
            flags[i] = 0
    return flags


def init_check_den(w, D, U, V, J):
    d = den(w, D, U, V, J)
    flags = [1 if di != 0 else 0 for di in d]
    return flags


def all_flow():
    U_arr = V_arr = J_arr = []
    w_0 = [0]
    D_0 = [1]
    V_0 = [1]
    J_0 = [2]
    U_0 = [10]
    for w, D, U, V, J in itertools.product(w_0, D_0, U_0, V_0, J_0):
        print ("Start: w={}, D={}, U={}, V={}, J={}".format(w, D, U, V, J))
        flags = init_check_den(w, D, U, V, J)
        while D > 0:
            if not 1 in flags:
                break
            D, U, V, J, flags = rg(w ,D, U, V, J, flags)
            #print (U)
        print ("End: U={}, V={}, J={}".format(U, V, J))

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
all_flow()
