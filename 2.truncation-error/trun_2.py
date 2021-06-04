%matplotlib notebook
import math
import numpy as np
import pylab as pl

pi4 = math.pi / 4

#2
#(1)
print("#2.1")
def f(x,k):
    sum = 0
    n = 0
    while n < k+1:
        sum += (((-1)**n)*x**(2*n))/math.factorial(2*n)
        n = n+1
    return sum
x = [0,1,2,3,4,5]
y = []
for i in x:
    temp = f(pi4,x[i])
    y.append(temp)
print(y)
#(2)
def f2(x,k):
    sum = 0
    n = 0
    while n < k+1:
        sum += (((-1)**n)*(x-1)**(2*n))/math.factorial(2*n)
        n = n+1
    return sum    
x2 = [0,1,2,3,4,5]
y2 = []
for i in x2:
    temp = f2(pi4,x2[i])
    y2.append(temp)
print(y2)
#(3)
y3 = []
for i in range(0,6):
    y3.append(y2[i]-y[i])
pl.figure(1)
pl.plot(x,y3)