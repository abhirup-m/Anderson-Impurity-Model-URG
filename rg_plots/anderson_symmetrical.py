#!/bin/python

import math
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
    for w in np.arange(0.43,0.6,0.02):
        #print (w)
        for D0 in [1]:
            J = 0
            U0 = 0.1
            D = D0
            U = U0
            b = 0.999
            V = 2
            x = []
            y = []
            den = (w - D/2)*(w - D/2 + U/2)
            deltaU = -2 * V**2 * D**0.5 / ((w - D/2)*(w - D/2 + U/2))
            if den * (w - D/2)*(w - D/2 + U/2) == 0:
                print (w,"stable")
                break
            if  U == 0:
                print (w,"zero")
                break
            while D > 0:
                print (D)
                x.append(D)
                y.append(U)
                den = (w - D/2)*(w - D/2 + U/2)
                #plt.scatter(D,U)
                deltaU = -2 * V**2 * D**0.5 / ((w - D/2)*(w - D/2 + U/2))
                U += deltaU
                D *= b
                if den * (w - D/2)*(w - D/2 + U/2) <= 0:
                    print (w,"stable")
                    break
                if  U <= 0:
                    print (w,"zero")
                    break
                if abs(deltaU) < 10**(-10) :
                    print (w,"too slow")
                    break
            plt.title(r'J fixed $\rightarrow \omega={}, J={}, U_0={}$'.format(w,J,U0))
            plt.xlabel(r'D')
            plt.ylabel(r'U')
            plt.plot(x,y,marker="o")
            plt.show()

# Constant hyb, vary starting D, plot flow of U for fixed starting U, omega = 0, J = 2
def fixed_J():
    for w in range(-40,40,1):
        for D0 in np.arange(1,41,1):
            J = 0.1
            D = D0
            U = 10
            b = 0.999
            while D > 0:
                #plt.scatter(D,U)
                deltaU = 0
                U += deltaU
                D *= b
                if deltaU * (D**2 - J**2/16) <= 0:
                    if U < 10:
                        print ("end",D,U)
                    break
#        plt.title(r'J fixed $\rightarrow \omega=0, J=2, U_0=10, D_0 \in [1,20]$')
#        plt.xlabel(r'D')
#        plt.ylabel(r'U')
#        plt.show()


# plot flow of U and J for omega = 0
def all_flow():
    b = 0.999
    D0 = 1
    V0 = 0.1
    U0 = 1
    J0 = 1
    # \omega range for which J is relevant
    wrange1 = np.linspace(D0/2 - U0 - J0,D0/2 - U0/2 - J0/4,5)
    # \omega range for which J is irrelevant
    wrange2 = np.linspace(D0/2 - U0/2 - J0/4,D0/2,6)
    for w in wrange1:
        print ("w=",w)
        D = D0
        V = V0
        U = U0
        J = J0
        x = w - D/2

        # expressions of three denominators
        d1 = x
        d2 = x + U/2 + J/4
        d3 = x + U/2 - J/4

        #check denominators at start
        if d1 == 0 or d2 == 0 or d3 == 0:
            print ("U=",U,"J=",J)
            continue

        X,Y = [],[]
        count=0
        while D > 0:
            count += 1
            X.append(J)
            Y.append(U)
            deltaU = -V**2 * D**0.5 * (2*U + J)/(d1 * d2) + J**2 * D**(3/2) * (6*x - J)/(8 * d2 * d3)
            deltaV = -(3 * J * D**0.5 / 4) * V / d2
            deltaJ = -J**2 * D**0.5 / d2
            U += deltaU
            V += deltaV
            J += deltaJ
            D *= b
            x = w - D/2
            if d2 * (x + U/2 + J/4) <= 0:
                print ("U=",U-deltaU,"J=",J-deltaJ)
                break
            if abs(deltaU) < 10**(-10):
                print ("slow: U=",U-deltaU,"J=",J-deltaJ)
                break
#        plt.plot(X,Y,color=colors[-1])
#    plt.xlabel(r'J')
#    plt.ylabel(r'U')
        plt.plot(X,Y,label=r'$\omega=${}'.format(w))
    plt.title(r'Relevant J$\to J_0=V_0^2/D_0={}, U_0={}, V_0={}, D_0={}$'.format(J0,U0,V0,D0))
    plt.legend()
    plt.show()

all_flow()
