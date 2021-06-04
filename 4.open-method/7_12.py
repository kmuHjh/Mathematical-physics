import numpy as np
from scipy.optimize import fsolve
def f(x):
    return [-x[0]**2 + x[0] +0.75 - x[1],x[1]+5*x[0]*x[1]-x[0]**2]
x0 = [1.2,1.2]
fsolve(f,x0)
