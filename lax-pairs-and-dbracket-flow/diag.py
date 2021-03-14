#!/bin/python

import numpy as np
import matplotlib
from matplotlib import pyplot as plt

font = {'family' : 'Source Code Pro',
        'size'   : 25}

matplotlib.rc('font', **font)
matplotlib.rcParams['text.usetex'] = True

A = np.array([[1.1,0.2,1],[0.1,1,0.2],[1,0.2,0.9]])
C = np.diag([0.1, 0.2, 0])
B = np.matmul(A, C) - np.matmul(C, A)
print (B)
print (np.matmul(B, B))
print (np.trace(np.matmul(B, B)))
for i in range(1,100):
    B = np.matmul(A, C) - np.matmul(C, A)
    plt.scatter(i, np.log10(abs(np.trace(np.matmul(B, B)))), color='b', marker='.')
    A -= np.matmul(A, B) - np.matmul(B, A)

plt.title(r'Variation of the function $-\frac{d\chi}{dt}$')
plt.xlabel(r'steps')
plt.ylabel(r'$\log_{10}|\frac{d\chi}{dt}|$')
plt.show()
print (np.trace(np.matmul(B, B)))
