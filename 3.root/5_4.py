%matplotlib notebook
import numpy as np
import pylab as pl

def f(x):
    return -13-20*x+19*x**2-3*x**3
print(f(2))
x = range(-5,5,1)
y = []
for i in x:
    y.append(f(i))

pl.plot(x,y)

#bisection

def bisection(f,a,b,n):
    if f(a)==0.0: return a
    if f(b)==0.0: return b
    for i in range(n):
        m = (a+b) / 2
        if f(m)==0: return m
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        return m
X1 = range(1,10)
Y1 = []
for n in X1:
    bb = bisection(f,0,5,n)
    Y1.append(bb)
    print(n,bb)
pl.plot(X1,Y1)

#false
def falseS(f,a,b,n):
    if f(a)==0.0: return a
    if f(b)==0.0: return b
    for i in range(n):
        m = b-f(b)*(a-b)/(f(a)-f(b))
        if f(m)==0: return m
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        return m

X2 = range(1,10)
Y2 = []
for n in X2:
    ff = falseS(f,-3,3,n)
    Y2.append(ff)
    print(n,ff)
pl.plot(X2,Y2)


