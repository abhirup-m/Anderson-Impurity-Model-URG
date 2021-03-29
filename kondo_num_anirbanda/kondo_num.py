#!/usr/bin/python3

from matplotlib import pyplot as plt
import numpy as np
import matplotlib

font = {'family' : 'Source Code Pro',
        'size'   : 20}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True

def rg1(D,J):
    delta = 2 * J**2 /(D - J/2)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

def rg2(w,D,J):
    delta = np.sqrt(D) * J**2 * (w - D/2) / ((w - D/2)**2 - J**2/16)
    if J * (J + delta) <= 0:
        return 0
    else:
        return J+delta

for J0 in np.arange(0.01,0.31,0.01):
#for J0 in [0.1]:
    J = J0
    Dmax = J0*90
    w = Dmax*1.7081
    x, y = [], []
    N = int(Dmax)*1000
    den = (w - Dmax/2)**2 - J**2/16
    count = N
    for D in np.linspace(Dmax,0.01,N):
        x.append(count)
        y.append(J)
        if den * ((w - D/2)**2 - J**2/16) <= 0:
            print (np.round(J0,2), np.round(1/(2*w/D - 1),5))
            plt.scatter(J0,(1/(2*w/D - 1)), marker='.', color='r')
            #plt.scatter(x, y)
            break
            x += range(count-1,0,-1)
            y += [J]*(count-1)
            print (w, J0, 2*D/J)
            plt.plot(x,y)
            plt.show()
            break
        den = (w - D/2)**2 - J**2/16
        J = rg2(w, D, J)
        count -= 1
    
plt.axhline(0.4134,0,10, label="0.4134")
plt.xlabel(r'$J_0$')
plt.ylabel(r'$W$')
plt.legend()
plt.show()
#plt.xlabel(r'RG step')
#plt.ylabel(r'$J$')
#plt.tight_layout()
#plt.show()
#plt.savefig('/home/abhirup/IPhD-Project-II/kondo_num/rel2J.png')

#plt.scatter(np.log10(X), np.log10(Y), label="data")
#plt.xlabel(r'$\log_{10}D$')
#plt.ylabel(r'$\log_{10}J^*$')
##plt.legend()
#linear_model=np.polyfit(np.log10(X),np.log10(Y),1)
#linear_model_fn=np.poly1d(linear_model)
#x_s=np.arange(1,7,1)
#plt.plot(x_s,linear_model_fn(x_s),label="best fit", color="green")
#plt.legend()
#plt.show()
    #plt.savefig('match2.png',bbox_inches='tight', transparent="True", pad_inches=0)
