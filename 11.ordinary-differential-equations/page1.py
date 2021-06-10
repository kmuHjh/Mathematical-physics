import numpy as np
import pylab as pl

print("(1). 질량 m인 물체가 떨어지고 있다.")
print("b) Euler, mid, Heun method를 각각 사용하여 속도 그래프를 그려라.")
print("Euler")

def euler(f,x0,x1,y0,h):
    x,y = x0, y0
    X = [x]
    Y = [y]
    while x<x1:
        y = y + f(x,y)*h
        x = x + h
        X.append(x)
        Y.append(y)
    return X,Y
def f(x,y):
    return -9.8 - 0.1*y
def rf(x,y):
    return (-9.8 - 0.1*y) * x

X,Y = euler(f,0,4,0,0.1)
pl.plot(X,Y)

pl.plot(X,Y,'o')



