#!/bin/python
import numpy as np
from matplotlib import pyplot as plt

for J0 in np.arange(0.0001,1,0.005):
    print (J0)
    J = J0
    D = 5
    b = 0.999
    while D>0:
        delta_J = J**2 * (D**(3/2) / 2) / (D**2/4 - J*2/16)
        D *= b
        J += delta_J
        if delta_J * (D**2/4 - J*2/16) <= 0:
            plt.scatter(np.log10(J0),np.log10(J))
            break

plt.show()
plt.clf()
