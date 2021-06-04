import numpy as np
import pylab as pl

def f(x):
    return x**3.5 - 80

x = range(1,20)
y = []
for i in x:
    y.append(f(i))
pl.plot(x,y)