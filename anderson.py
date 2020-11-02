#!/bin/python
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
font = {'size'   : 20}

matplotlib.rc('font', **font)
E = -10
D = 100
b = 0.99
while E > -D:
    print (E)
    plt.scatter(D,E,marker='.')
    delta_E = np.sqrt(D)/(-D - E)
    D *= b
    E += delta_E

plt.xlabel("Bandwidth D")
plt.ylabel(r'On-site energy $\epsilon_d$')
plt.show()
