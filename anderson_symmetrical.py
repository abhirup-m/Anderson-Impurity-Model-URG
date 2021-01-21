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
    for w in range(-11,11,3):
        for D0 in np.arange(1,20,6):
            print (D0)
            J = 0
            U0 = 10
            D = D0
            U = U0
            b = 0.999
            V = 2
            x = []
            y = []
            while D > 0:
                x.append(D)
                y.append(U)
                den = (w - D/2)*(w - D/2 + U/2)
                #plt.scatter(D,U)
                deltaU = -2 * V**2 * D**0.5 / ((w - D/2)*(w - D/2 + U/2))
                U += deltaU
                D *= b
                if den * (w - D/2)*(w - D/2 + U/2) <= 0:
                    print ("stable")
                    break
                if  U <= 0:
                    print ("zero")
                    break
                if abs(deltaU) < 10**(-100) :
                    print ("too slow")
                    break
            plt.title(r'J fixed $\rightarrow \omega={}, J={}, U_0={}$'.format(w,J,U0))
            plt.xlabel(r'D')
            plt.ylabel(r'U')
            plt.plot(x,y)
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
    b = 0.9999
    colors = ['r','b','w','y','g']
    for U in np.arange(0.2,1,0.1):
        for J in np.arange(0.2,1,0.1):
            colors = colors[-1:]+colors[:-1]
            X = []
            Y = []
            D0 = 20
            D = D0
            X.append(J)
            Y.append(U)
            while D > 0:
                print (D**2 - J**2/16)
                deltaU = J**2 * D**(5/2) * (6*D + J)/(4 * (D**2 - J**2/16))
                deltaJ = J**2 * D**2 / (2 * (D**2 - J**2/16))
                U += deltaU
                J += deltaJ
                X.append(J)
                Y.append(U)
                D *= b
                if deltaU * (D**2 - J**2/16) <= 0:
                    print (J,U)
                    break
            plt.plot(X,Y,color=colors[-1])
    plt.xlabel(r'J')
    plt.ylabel(r'U')
    plt.title(r'both flow $\rightarrow \omega=0, J_0=0.1, U_0=100, D_0 = 20$')
    plt.show()

fixed_VJ()
