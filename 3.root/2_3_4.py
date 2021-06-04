import numpy as np
import pylab as pl
from scipy import optimize

def v(x):
    return 2*(1-np.exp(-(x-1)))**2 - 2
x = []
y = []
for i in range(0,11):
    x.append(i)
    y.append(v(i))
pl.plot(x,y)

#(2)
h = 0.001
def dv(x):
    return -(v(x+h)-v(x-h))/(2*h)
dy = []
for i in range(0,11):
    dy.append(dv(i))
pl.plot(x,dy)

#(3)
def f(x):
    return dv(x)

root = optimize.brentq(f,-2,5)
print(root)
