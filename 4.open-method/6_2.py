import numpy as np
import pylab as pl
#6.2
#(a)
x = np.linspace(-2,4,30)
def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x -5
y = []
y2 = []
for i in range(0,30):
    y.append(f(x[i]))
    y2.append(0)

pl.plot(x,y)
pl.plot(x,y2)

#(b)
print("Fixed-point iteratioin method")
x_0 = 3
for i in range(6):
    x_0 = f(x_0)
    print(i,x_0)

#(c)
print(sep ='')
print("Newton-Raphson method")
def df(x):
    return 6*x**2 - 23.4*x + 17.7

x_0 = 3
newX = x_0
i = 0
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1
print(sep ='')
print("Secant method")
def df(x1,x2):
    df = (f(x1)-f(x2))/(x1-x2)
    return df
i = 0
x0 = 4
x1 = 3
x2 = x0
x3 = x0+0.5
tol = 1e-8

while abs(x3-x2) > tol:
    x1 = x2
    x2 = x3
    x3 = x2-f(x2)/df(x1,x2)
    i = i+1
    print (i,x3,f(x3))

print(sep ='')
print("Modified secant method")
def df2(x,dx):
    df = (f(x+dx)-f(x))/dx
    return df
x1 = 3
x2 = 0.5
dx = 0.01
i = 0
while abs(x2-x1) > 1e-10:
    x1 = x2
    x2 = x1 - f(x1)/df(x1,dx)
    print(i,x1,f(x1))
    i = i +1

print(sep ='')
print("poly1d of numpy")

f = np.poly1d([2,-11.7,17.7,-5])
result = np.roots(f)
print(result)