#!/bin/python

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
matplotlib.rcParams['text.usetex'] = True
#    for U in range(10,20,50):
#        V = 0.1
#        V2 = 0.1
#        D_o = 100000
#        b = 0.999999999999
#    for w in np.linspace(-300,300,20):
#        U = 1000
#        V = 0.1
#        V2 = 0.1
#        b = 0.999999999999
#        D = 10
#        col = colors[0]
#        colors = colors[-1:] + colors[0:-1]
#        for i in range(100):
#            den = U**2 - (4*w - 2*D)**2
#            U += 32*U*D*V**2/den
#            V += -D*V*V2/(U + 4*w - 2*D)
#            plt.scatter(V, U, marker='.', color=col)
#            D *= b
#            if den * (U**2 - (4*w - 2*D)**2) <=0 or U <=0:
#                break
#        print (w)
#        plt.show()
#        plt.clf()

#   U = 1000
#   V2 = 0.01
#   b = 0.9999
#   Do = 100
#   D = Do
# for i in range(10000):
#    den = D**2 - U**2/4
#    print (den)
#    U += 2*U*D*V2*Do/den
#    D *= b
#    if den * (D**2 - U**2/4) <=0:
#        print (D,U)
#        break


# Constant hyb, vary starting D, plot flow of U for fixed starting U, omega = 0, J = 2
def fixed_VJ():
    for D0 in np.arange(0.1,31,5):
        D = D0
        V = 2*D
        J = V**2 / D
        U = 10
        b = 0.99
        while D > 0:
            plt.scatter(D,U)
            deltaU = J**2 * D**(5/2) * (6*D + J)/(4 * (D**2 - J**2/16)) - 4 * V**2 * D * (U + J/4)/((D - U/2 - J/4) * (D + U/2))
            U += deltaU
            D *= b
            if deltaU * (D**2 - J**2/16) <= 0:
                print (D,U)
                break
    plt.title(r'J fixed $\rightarrow \omega=0, J=2, U_0=10, D_0 \in [1,20]$')
    plt.xlabel(r'D')
    plt.ylabel(r'U')
    plt.show()

# Constant hyb, vary starting D, plot flow of U for fixed starting U, omega = 0, J = 2
def fixed_J():
    for D0 in np.arange(0.1,21,5):
        J = 0.1
        D = D0
        U = 10
        b = 0.99
        while D > 0:
            plt.scatter(D,U)
            deltaU = J**2 * D**(5/2) * (6*D + J)/(4 * (D**2 - J**2/16))
            U += deltaU
            D *= b
            if deltaU * (D**2 - J**2/16) <= 0:
                print (D,U)
                break
    plt.title(r'J fixed $\rightarrow \omega=0, J=2, U_0=10, D_0 \in [1,20]$')
    plt.xlabel(r'D')
    plt.ylabel(r'U')
    plt.show()


# plot flow of U and J for omega = 0
def all_flow():
    b = 0.999
    D0 = 0.2
    V = 0.1
    colors = ['r','b','w','y','g']
    for U0 in np.arange(0.01,1,0.01):
        for J0 in np.arange(0.01, 0.8 - 2*U0, 0.1):
            colors = colors[-1:]+colors[:-1]
            X = []
            Y = []
            J = J0
            U = U0
            V1 = V
            V0 = V
            D = D0
            #X.append(J/D)
            #Y.append(U/D)
            plt.scatter(J,U,marker='.')
            sign1 = D - U/2 - J/4
            sign2 = D - J/4
            sign3 = D + U/2
            sign4 = D + J/4
            sign5 = U + J/4
            count = 0
            print ("start",J,U)
            while D > 0:
                #print (sign1)
                if sign1 * (D - U/2 - J/4) <= 0:
                    print ("cutoff by 1, after", count, " steps")
                    break
                elif sign2 * (D - J/4) <= 0:
                    print ("cutoff by 2, after", count, " steps")
                    break
                elif sign3 * (D + U/2) <= 0:
                    print ("cutoff by 3, after", count, " steps")
                    break
                elif sign4 * (D + J/4) <= 0:
                    print ("cutoff by 4, after", count, " steps")
                    break
                elif sign5 * (U + J/4) <= 0:
                    if J0 == 0:
                        U = 0
                    print ("cutoff by 5, after", count, " steps")
                    break
                sign1 = D - U/2 - J/4
                sign2 = D - J/4
                sign3 = D + U/2
                sign4 = D + J/4
                sign5 = U + J/4
                deltaU = - 2 * (V1**2 + V0**2) * D**(1/2) * (U + J/4) / ((D - U/2 - J/4) * (D + U/2)) + J**2 * D * (6*D + J)/(4 * (D**2 - J**2/16))
                deltaJ = J**2 * D**(1/2) / (2 * (D**2 - J**2/16))
                deltaV1 = V1 * D**(1/2) * (3*J/4) / (D - U/2 - J/4)
                deltaV0 = V0 * D**(1/2) * (3*J/4) / (D - J/4)
                if abs(deltaU) < 10**(-15):
                    print ("cutoff by 6, after", count, " steps")
                    break
                U += deltaU
                J += deltaJ
                V1 += deltaV1
                V0 += deltaV0
                #plt.scatter(J,U,marker='.')
                #X.append(J)
                #Y.append(U)
                D *= b
                count += 1
                #print (J,U,V1,V0)
            #plt.plot(X,Y,color=colors[-1])
                print (J, U)
            if U<0:
                input()
            #plt.xlabel(r'J')
            #plt.ylabel(r'U')
            #plt.title(r'both flow $\rightarrow \omega=0, V1_0={}, V0_0={}, J_0={}, U_0={}, D_0 = 5$'.format(V10,V00,J0,U0))
            #plt.show()
            #plt.clf()

all_flow()
