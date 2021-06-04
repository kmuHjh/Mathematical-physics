import numpy as np
import pylab as pl
from sympy import solve,Symbol
from scipy import optimize

print("#13.2")
print("(a) Plot the function")
def ff(x):
    return -1.5*(x**6) - 2*(x**4) + 12*x

x = np.linspace(0,1.5,20)
y = []
for i in range(0,20):
    y.append(ff(x[i]))
pl.figure(1)
pl.plot(x,y)
print(sep = '')
print("(b) Use anlaytical methods to prove that the function is concave for all values of x")
x = Symbol('x')
solve(-9*(x**5) - 8*(x**3) + 12,x)
maxX = 0.916915
def ddf(x):
    return -45*(x**4) - 24*(x**2)
print(ddf(maxX))
print("function의 미분함수 df=0일때 실근은 0.916915 한개이고 이계미분 ddf에 대입 시 음수가 나오므로 이 함수는 concave function 이다.")
print(sep ='')
print("(c) Differentiagte the function and them use a root-location method to solve for the maximum f(x) and the corresponding value of x")
def f(x):
    return -9*(x**5) - 8*(x**3) + 12

def df(x,dx):
    df = (f(x+dx)-f(x))/dx
    return df

x1 = 2.0
x2 = 0.5
dx = 0.0001
i = 0
while abs(x2-x1) > 1e-10:
    x1 = x2
    x2 = x1 - f(x1)/df(x1,dx)
    print(i,x1,f(x1))
    i = i +1

print("x = 0.91691516 by Secant Method")
print("f(x) =",f(0.9))
print(sep='')
print("#13.3")
def search(f,a,b,tol=1.0e-9):
    nlter = 8
    R = (np.sqrt(5.0)-1.0)/2.0
    d = R*(b-a)
    x1 = a+d
    x2 = b-d
    f1 = f(x1)
    f2 = f(x2)
    for i in range(nlter):
        if f1 > f2:
            a = x2
            x2 = x1
            f2 = f1
            x1 = a + R*(b-a)
            f1 = f(x1)
        else:
            b = x1
            x1 = x2
            f1 = f2
            x2 = b-R*(b-a)
            f2 = f(x2)
        print(i+1,x1,f1,x2,f2)
    if f1 < f2: return x2,f2
    else: return x1,f1
x3 = 0
x4 = 2
print(search(ff,x3,x4))
print(sep ='')
print("#13.4")
def f(x):
    return -9*(x**5) - 8*(x**3) + 12
def df(x):
    return -45*(x**4) - 24*(x**2)
x_0 = 0
newX = x_0
i = 0
print("x0 is 0 case")
print("zero devision error")

print(sep='')
x_0 = 1
newX = x_0
i = 0
print("x0 is 1 case")
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1
print(sep='')
x_0 = 2
newX = x_0
i = 0
print("x0 is 2 case")
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1
print(sep ='')
print("#13.5")
x_0 = 2
newX = x_0
i = 0
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1
