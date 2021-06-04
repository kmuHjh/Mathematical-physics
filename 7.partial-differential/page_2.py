import numpy as np
import pylab as pl
import math
import sympy as sp

from scipy.optimize import minimize_scalar
print("#1")
def V(r):
    return 4*((1/r)**12 - (1/r)**6)

x = np.linspace(-4,0,10)
x2 = np.linspace(0,4,10)
y = []
y2 = []
for i in range(0,9):
    y.append(V(x[i]))
for i in range(1,10):
    y2.append(V(x2[i]))
pl.figure(1)
pl.plot(x[0:9],y,x2[1:10],y2)

res = minimize_scalar(V,bounds=(-4,0),method='bounded')
print("minimum is ",res.x)

print(sep ='')
print("#2")
x = sp.symbols('x')
w = (27-18*x+2*x**2)*sp.exp(-x/3)
sp.plot(w,(x,0,15))
sp.minimum(w,x)