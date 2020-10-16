#!/bin/python
from sympy import *


B, J, b = symbols("B J b")
Z = cosh(b*B/2) + cosh(b*sqrt(B**2 + J**2)/2)
Z_deri = diff(Z,B)
Z_deri2 = diff(Z_deri,B)
chi = ((Z_deri2/Z - (Z_deri/Z)**2)/b).doit()
print (chi)
print ()
prettyprint(chi.evalf(subs={B: 0}))


