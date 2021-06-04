%matplotlib notebook
import math
import numpy as np
import pylab as pl

#1
#(1)
print("#1.1")
def f(x,k):
    sum = 0
    n = 0
    while n < k+1:
        sum += x**n/math.factorial(n)
        n = n+1
    return sum
#(2)
print("#1.2")
print(sep = '')
xx = [0,1,2,3,4,5,6,7,8,9,10]
y = []
for i in xx:
    temp = f(1,xx[i])
    y.append(temp)
pl.figure(1)
pl.plot(xx,y)
#(3)
print("#1.3")
print(sep = '')
E = np.exp(1)
pl.figure(2)
pl.plot(xx,E-y)