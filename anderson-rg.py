#!/bin/python
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import os

mpl.rcParams["savefig.directory"] = os.chdir(os.path.dirname(__file__))

fig, axs = plt.subplots(2, 2)
axs[0,0].set_title("ed")
axs[0,1].set_title("U")
axs[1,0].set_title("vp")
axs[1,1].set_title("vm")

def rg_eq(W, g, V2, num, i):
    ed, u, vp, vm = g
    if i == 0:
        numr = -0.5 * num * (vm**2 * (W + 2*ed + u) + vp**2 * W)
        den = W * (W + 2*ed + u)
    elif i ==1:
        numr = num * (vm**2 * ed * (W - ed) * (W + 2*ed + u) - vp**2 * W * (W + ed) * (3*ed + u))
        den = W * (W**2 - ed**2) * (W + 2*ed + u)
    elif i ==2:
        numr = -0.5 * num * vp * V2 * (2*W + ed + u)
        den = (W + 2*ed + u) * (W - ed)
    elif i ==3:
        numr = -num * vm * V2
        den = W + ed
    return numr, den


def master_eq(W, g, V2, num, dens):
    global flags, flag, df
    g_new = [0,0,0,0]
    den_new = [0,0,0,0]
    numr_new = [0,0,0,0]
    for i in range(len(g[-1])):
        if flags[i] == False:
            numr_new[i],den_new[i] = rg_eq(W, g[-1], V2, num, i)
            if dens != [] and dens[-1][i] * den_new[i] <= 0:
                flags[i] = True
                g_new[i] = g[-1][i]
            else:
                g_new[i] = g[-1][i] + numr_new[i]/den_new[i]
        else:
            g_new[i] = g[-1][i]
    if flags == [True, True, True, True]:
        flag = True

    g.append(g_new)
    dens.append(den_new)
    return g,dens


A       = 1
b       = 0.9999
flag    = False
flags   = [False, False, False, False]

for w in np.arange(91, 92, 5):
    for D0 in range(186, 187, 5):
        ed      = -1000
        vp      = 1
        vm      = vp
        u       = 1000
        g       = [[ed, u, vp, vm]]
        dens    = []
        D       = D0
        x       = [D]
        V2      = vp**2/D0
        flag    = False
        flags   = [False, False, False, False]
        j_start = 500
        j_range = [j_start+1]
        for j in range(j_start,0,-1):
            W = w - D/2
            num = A * D
            g, dens = master_eq(W, g, V2, num, dens)
            j_range.append(j)
            if flag == True:
                break
            D *= b
            x.append(D)
        if flag == True:
            break

print (flags)
axs[0,0].plot(j_range,[g[i][0] for i in range(0,len(g))], marker='.')
axs[0,1].plot(j_range,[g[i][1] for i in range(0,len(g))], marker='.')
axs[1,0].plot(j_range,[g[i][2] for i in range(0,len(g))], marker='.')
axs[1,1].plot(j_range,[g[i][3] for i in range(0,len(g))], marker='.')
fig.suptitle("D0 = {}, w = {}, D* = {}\ninit = {}\nfinal = {}".format(D0, w, round(D,1), g[0], np.array(g[-1]).round(2)))
plt.show()


#axs[0,0].plot(j_range,[g[i][0] for i in range(1,len(g))], marker='.')
#fig = plt.figure()
#plt.plot(j_range,[g[i][0] for i in range(0,len(g))], marker='.')
#fig.suptitle("ed,\n init=({})".format(g[0]))
#fig = plt.figure()
#plt.plot(j_range,[g[i][1] for i in range(0,len(g))], marker='.')
#fig.suptitle("U,\n init=({})".format(g[0]))
#fig = plt.figure()
#plt.plot(j_range,[g[i][2] for i in range(0,len(g))], marker='.')
#fig.suptitle("Vp,\n init=({})".format(g[0]))
#fig = plt.figure()
#plt.plot(j_range,[g[i][3] for i in range(0,len(g))], marker='.')
#fig.suptitle("Vm,\n init=({})".format(g[0]))
#axs[1,0].plot(j_range,[g[i][2] for i in range(1,len(g))], marker='.')
#axs[1,1].plot(j_range,[g[i][3] for i in range(1,len(g))], marker='.')
 #   axs[0,0].scatter(D, ed, marker='.')
 #   axs[0,1].scatter(D, u,  marker='.')
 #   axs[1,0].scatter(D, vp, marker='.')
 #   axs[1,1].scatter(D, vm, marker='.')
#    axs[0,0].plot(x,[y[i][0] for i in range(0,len(y))], marker='.')
#    axs[0,1].plot(x,[y[i][1] for i in range(0,len(y))], marker='.')
#    axs[1,0].plot(x,[y[i][2] for i in range(0,len(y))], marker='.')
#    axs[1,1].plot(x,[y[i][3] for i in range(0,len(y))], marker='.')
#plt.show()
