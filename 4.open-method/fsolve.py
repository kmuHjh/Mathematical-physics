import numpy as np
from scipy.optimize import fsolve
m1 = 1
m2 = 2
v1 = 1
v2 = 0

a = 0.5*m1*v1*v1 + 0.5*m2*v2*v2
b = m1*v1 + m2*v2

def f(x):
    return [0.5*m1*x[0]**2+0.5*m2*x[1]**2-a,m1*x[0]+m2*x[1]-b]

x0 = [0.0,0.0]
fsolve(f,x0)
    