#!/bin/python

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 25}

matplotlib.rc('font', **font)
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
    b = 0.9999
    colors = ['r','b','y','g']
    ci=0
    for D0 in [1,10,100,650,1000]:
        for J0 in [0]:
            D = D0
            U = 0.5
            V = 1
            J = 0
            sign1 = D - J/4
            sign2 = D - U/2 - J/2
            sign3 = D - 3*J/4
            sign5 = U + J/2
            flag = False
            count = 0
            x = [J]
            y = [U]
            print (J, U)
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
                x.append(J)
                y.append(U)
                count += 1
            print (U)
            plt.plot(np.log10(D0),U,marker='o')
            if U < 0:
                print (U)
            ci += 1
    plt.xlabel(r'$\log_{10}(D)$')
    plt.ylabel(r'$U^*$')
    plt.title(r'Variation of $U^*$ with bandwidth ($V=1$)')
    plt.show()

def func():
        J = 0.1
        sign1 = D + U/4 - J/8
        sign2 = D - U/4 - J/4
        sign5 = U + J/4
        count = 0
        #print ("start val: D={}, J={}, U={}".format(D, J,U))
        while D > 0:
            if sign1 * (D + U/4 - J/8) <= 0:
                print ("cut by 1,after",count," steps")
                break
            elif sign2 * (D - U/4 - J/4) <= 0:
                print ("cut by 2,after",count," steps")
                break
            elif sign5 * U <= 0 and J0 == 0:
                U = 0
                print ("cut by 5,after",count," steps")
                break
            sign1 = D + U/4 - J/8
            sign2 = D - U/4 - J/4
            sign5 = U + J/4
            deltaU = 0.5 * V**2 * D**(1/2) * sign5 / (sign1 * sign2)
            deltaJ = J**2 * D**(1/2) / (8 * sign1)
            deltaV = V * D**(1/2) * (3*J/4) / sign1
            U += deltaU
            J += deltaJ
            V += deltaV
            D *= b
            count += 1
        print ("End val: D={}, U={}, J={}".format(D,U,J))
        if U < 0:
            input()

all_flow()
