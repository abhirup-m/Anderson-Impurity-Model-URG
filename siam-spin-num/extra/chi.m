syms T J B
b=1/T
Z = cosh(b*B/2)+cosh(b*sqrt(B^2 + J^2)/2)
M = diff(Z,B)/(b*Z)
chi = diff(M,B)
subs(chi,T,0)
