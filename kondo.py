#!/bin/python
import numpy as np
from matplotlib import pyplot as plt

J = 0.01
k = 2.83
b = 0.999999999999
K = []
for c in np.arange(100,10,-1):
    K.append(J/k)
    delta_J = 3*J**2/(1 - (J/(4*0.7075*k))**(2))
    k *= b
    J += delta_J

plt.plot(np.arange(100,10,-1), K)
plt.show()
