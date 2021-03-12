#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True
#plt.style.use('ggplot')

def rg1(D,J):
    delta = 2 * J**2 /(D - J/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

def rg2(w,D,J):
    delta = -2 * J**2 /(w - D/2 + J/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

plt.title(r'Bare: $J = -D/10, N = D \times 10$')
X = []
Y = []
for Dmax in [10,100,1000,10000,100000, 1000000]:
    print (Dmax)
    J = Dmax/10
    N = Dmax*10
    for D in np.linspace(Dmax,0,N):
        den = D - J/2
        J = rg1(D, J)
        if J == 0 or den * (D - J/2) <= 0:
            break
    X.append(Dmax)
    Y.append(J)
    
plt.scatter(np.log10(X), np.log10(Y), label="data")
plt.xlabel(r'$\log_{10}D$')
plt.ylabel(r'$\log_{10}J^*$')
#plt.scatter(X[0], Y[0], color='r', marker='o', label="start point")
#plt.scatter(X[-1], Y[-1], color='g', marker='o', label="fixed point")
#plt.legend()
linear_model=np.polyfit(np.log10(X),np.log10(Y),1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(1,7,1)
plt.plot(x_s,linear_model_fn(x_s),label="best fit", color="green")
plt.legend()
plt.show()
    #plt.savefig('match2.png',bbox_inches='tight', transparent="True", pad_inches=0)
