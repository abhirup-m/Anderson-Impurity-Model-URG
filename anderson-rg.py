#!/bin/python
import numpy as np
from matplotlib import pyplot as plt

fig, axs = plt.subplots(2, 2)

def eq_ed(W, U, ed, Vp, Vm, V2, num):
    numr = -0.5 * num * (Vm**2 * (W + 2*ed + U) + Vp**2 * W)
    den = W * (W + 2*ed + U)
    ed += numr / den
    print (den)
    return ed,  den


def eq_U(W, U, ed, Vp, Vm, V2, num):
    numr = num * (Vm**2 * ed * (W - ed) * (W + 2*ed + U) - Vp**2 * W * (W + ed) * (3*ed + U))
    den = W * (W**2 - ed**2) * (W + 2*ed + U)
    U += numr / den
    return U, den


def eq_Vp(W, U, ed, Vp, Vm, V2, num):
    numr = -0.5 * num * Vp * V2 * (2*W + ed + U)
    den = (W + 2*ed + U) * (W - ed)
    Vp += numr / den
    return Vp, den


def eq_Vm(W, U, ed, Vp, Vm, V2, num):
    numr = -num * Vm * V2
    den = W + ed
    Vm += numr / den
    return Vm, den


def check_den(W, U, ed, dens):
    global flags
    #print (dens)
    if dens[0] * W * (W + 2*ed + U) <= 0:
        flags[0] = True
    if dens[1] * W * (W**2 - ed**2) * (W + 2*ed + U) <= 0:
        flags[1] = True
    if dens[2] * (W + 2*ed + U) * (W - ed) <= 0:
        flags[2] = True
    if dens[3] * (W + ed) <= 0:
        flags[3] = True


def master_eq(W, U, ed, Vp, Vm, V2, num):
    global flags
    ed_new, den1 = eq_ed(W, U, ed, Vp, Vm, V2, num)
    U_new, den2 = eq_U(W, U, ed, Vp, Vm, V2, num)
    Vp_new, den3 = eq_Vp(W, U, ed, Vp, Vm, V2, num)
    Vm_new, den4 = eq_Vm(W, U, ed, Vp, Vm, V2, num)

    check_den(D*b/2, U_new, ed_new, [den1, den2, den3, den4])
    if flags[0] == True:
        ed_new = ed
    if flags[1] == True:
        U_new = U
    if flags[2] == True:
        Vp_new = Vp
    if flags[3] == True:
        Vm_new = Vm
    return [ed_new, U_new, Vp_new, Vm_new]



# system size = 100 x 100
A = 1

# RG scale factor
b = 0.99999

# upper energy cutoff
D = 1000


# starting values of couplings: ed,V << D << U
ed = 0
Vp = 10
Vm = Vp
U = 10

# value of extra coupling which remains fixed
V2 = Vp**2
num = A * D

global flags
flags = [False, False, False, False]

while D>999:
    print (flags)
    print (D)
    W = D/2
    num = A * D
    ed, U, Vp, Vm = master_eq(W, U, ed, Vp, Vm, V2, num)
    axs[0,0].scatter(D,ed, marker='.')
    axs[0,1].scatter(D,U, marker='.')
    axs[1,0].scatter(D,Vp, marker='.')
    axs[1,1].scatter(D,Vm, marker='.')
    D *= b


print (flags)
#plt.legend()
axs[0,0].set_title("ed")
axs[0,1].set_title("U")
axs[1,0].set_title("Vp")
axs[1,1].set_title("Vm")
plt.show()
