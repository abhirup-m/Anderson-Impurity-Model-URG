#!/bin/python
import numpy as np
from matplotlib import pyplot as plt

J = 0.01
k = 2.83
b = 0.9999
K = []
flag = False
sgn = 1 - (J/(4*0.7075*k))**(2)
for c in np.arange(100,10,-1):
    if sgn*(1 - (J/(4*0.7075*k))**(2)) <=0:
        flag = True
    else:
        sgn = 1 - (J/(4*0.7075*k))**(2)
    if flag:
        K.append(K[-1])
    else:
        K.append(J/k)
        delta_J = 1000*3*J**2/(1 - (J/(4*0.7075*k))**(2))
        k *= b
        J += delta_J

plt.plot(np.arange(100,10,-1), K)
plt.show()
