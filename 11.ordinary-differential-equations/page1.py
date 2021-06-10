import numpy as np
import pylab as pl
from scipy.integrate import odeint
print("(1). 질량 m인 물체가 떨어지고 있다.")
print("b) Euler, mid, Heun method를 각각 사용하여 속도 그래프를 그려라.")
print("Euler method")

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

X,Y = euler(f,0,4,1,0.1)
pl.figure(1)
pl.plot(X,Y)
pl.plot(X,Y,'o')
X1 = np.linspace(0,4,100)
Y1 = rf(X1,0)
pl.plot(X1,Y1)

print("mid method")
def midpoint(f,x0,x1,y0,h):
    x,y =x0,y0
    X = [x]
    Y = [y]
    while x<x1:
        k1 = f(x,y)
        k2 = f(x+h/2, y+h/2*k1)
        y = y + h*k2
        x = x + h
        X.append(x)
        Y.append(y)
    return X,Y

Xm,Ym = midpoint(f,0,4,1,0.1)
pl.figure(2)
pl.plot(Xm,Ym)
pl.plot(Xm,Ym,'o')
X1 = np.linspace(0,4,100)
Y1 = rf(X1,0)
pl.plot(X1,Y1)

def heun(f,x0,x1,y0,h):
    x,y = x0,y0
    X = [x]
    Y = [y]
    while x<x1:
        k1 = f(x,y)
        k2 = f(x+h, y+h*k1)
        y = y+h*(k1+k2)/2
        x = x +h
        X.append(x)
        Y.append(y)
    return X,Y
Xh,Yh = heun(f,0,4,1,0.1)
pl.figure(3)
pl.plot(Xh,Yh)
pl.plot(Xh,Yh,'o')
X1 = np.linspace(0,4,100)
Y1 = rf(X1,0)
pl.plot(X1,Y1)

print("(2) Damped harmonic motion")
def dy(y,t):
    f = np.zeros(2)
    f[0] = y[1]  
    f[1] = -20*y[1] - c*y[0]
    return f
y0 = [0,1]
t = np.arange(0,15,0.1)
c = 0
y1 = odeint(dy,y0,t)
print(y1)
pl.figure(4)
pl.plot(t,y1)

c = 5
y1 = odeint(dy,y0,t)
print(y1)
pl.figure(5)
pl.plot(t,y1)

c = 40
y1 = odeint(dy,y0,t)
print(y1)
pl.figure(6)
pl.plot(t,y1)

c = 200
y1 = odeint(dy,y0,t)
print(y1)
pl.figure(7)
pl.plot(t,y1)