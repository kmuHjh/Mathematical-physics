import math
import numpy as np
import pylab as pl
def f(x):
    return 5*x**5 - 3*x**4 + 4*math.sin(x) +1
def df(x):
    return 25*x**4 - 12*x**3 + 4*math.cos(x)
def d2f(x):
    return 100*x**3 - 36*x**2 - 4*math.sin(x)
x = 1.0
h = 0.2
#forward
f1 = (f(x+h)-f(x))/h
et = (df(x)-f1)/df(x) * 100
print("forward")
print (df(x),f1,et)
#backward
f2 = (f(x)-f(x-h))/h
et = (df(x)-f2)/df(x) * 100
print("backward")
print(df(x),f2,et)
#centered
f3 = (f(x+h)-f(x-h))/(2*h)
et = (df(x)-f3)/df(x)*100
print("centered")
print(df(x),f3,et)

#forward
f1 = (f(x+h)-f(x))/h
et = (d2f(x)-f1)/d2f(x) * 100
print("forward")
print (d2f(x),f1,et)
#backward
f2 = (f(x)-f(x-h))/h
et = (d2f(x)-f2)/d2f(x) * 100
print("backward")
print(d2f(x),f2,et)
#centered
f3 = (f(x+h)-f(x-h))/(2*h)
et = (d2f(x)-f3)/d2f(x)*100
print("centered")
print(d2f(x),f3,et)

def h(n):
    return 1/2**n
x = []
y = []
for i in range(1,11):
    x.append(i)
    y.append(h(i))
print(x)
print(y)
newY = []
h2 = []
for i in range(0,10):
    temp = (f(1+y[i])-f(1-y[i]))/(2*y[i])
    newY.append(temp)