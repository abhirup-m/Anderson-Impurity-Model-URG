#!/bin/python
from sympy import *
import numpy as np
from matplotlib import pyplot as plt


Tk = 3.5
kB = 1
B, J, b, T = symbols("B J b T")
b = (kB*T)**(-1)
Z = cosh(b*B/2) + cosh(b*sqrt(B**2 + J**2)/2)
Z_deri = diff(Z,B)
Z_deri2 = diff(Z_deri,B)
chi = (Z_deri2/Z - (Z_deri/Z)**2)/b
print (chi)
B_val = 0
chi_T = chi.subs(J,16)
for B_val in range(10,100,10): 
    chi_T_final = chi_T.subs(B,B_val)
    plot(chi_T_final)

"""
Trange = np.arange(0.1,1.5*Tk,0.5)
for B_val in range(0,100,10): 
    print (B_val)
    chi_T = chi.subs({B: B_val, J:16})
    chi_arr=[]
    for T in Trange:
        chi_arr.append(chi_T.subs(b,1/(T*kB)))
    col=plt.plot(Trange/Tk, chi_arr, label="B=%d" % B_val)[-1].get_color()
    print (col)
    plt.axvline(Trange[chi_arr.index(max(chi_arr))]/Tk,0,10,ls='--', color=col)
plt.legend()
plt.show()
"""
