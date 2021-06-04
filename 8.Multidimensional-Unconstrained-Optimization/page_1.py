import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import Bounds, minimize
from scipy.optimize import brent
#1.(1) graph
def f(x,y):
    z = x**2 + y**2 + 2*x - 4*y + 10
    return z

x = np.linspace(-2,2,9)
y = np.linspace(-2,2,9)
temp = np.zeros((len(x),len(y)))
for i in range(9):
    for j in range(9):
        temp[j,i] = f(x[i],y[j])
xx,yy = np.meshgrid(x,y)
plt.figure(figsize = (5,3.5))
ax = plt.subplot(1,1,1,projection='3d')
ax.plot_surface(xx,yy,temp)
plt.show()

#1.(2) 임계점
def fx(x,y):
    z = 2*x + 2
    return z
def fy(x,y):
    z = 2*y - 4
    return z
print("임계점은 (-1,2)")
print(sep ='')

#1.(3) 임계점의 극소 극대
def fxx(x,y):
    z = 2
    return z
def fyy(x,y):
    z = 2
    return z
def fxy(x,y):
    return 0
def fyx(x,y):
    return 0
H = fxx(-1,2)*fyy(-1,2) - fxy(-1,2)*fyx(-1,2)
print("헤시안 행렬의 고유값이 양수이므로 (-1,2)는 극소점")

print(sep ='')
#1.(4)
print("newton method를 이용하여 극소점 구하기")
def fx(x,y,dx):
    return (f(x+dx,y)-f(x-dx,y))/(2*dx)
def fxx(x,y,dx):
    return (fx(x+dx,y,dx)-fx(x-dx,y,dx))/(2*dx)
def fy(x,y,dy):
    return (f(x,y+dy)-f(x,y-dy))/(2*dy)
def fyy(x,y,dy):
    return (fy(x,y+dy,dy)-fy(x,y-dy,dy))/(2*dy)
def fxy(x,y,dx,dy):
    return (fx(x,y+dy,dx)-fx(x,y-dy,dx))/(2*dy)

def Hs(x,y,dx,dy):
    H = np.array([[fxx(x,y,dx),fxy(x,y,dx,dy)],[fxy(x,y,dx,dy),fyy(x,y,dy)]])
    return H
H = Hs(0,0,1e-3,1e-3)
Hl = np.linalg.inv(H)
X = np.zeros(2)
X0 = np.array([-1,1])
dx, dy = 1e-3 , 1e-3
gf = np.array([fx(X0[0],X0[1],dx),fy(X0[0],X0[1],dy)])
X = X0 - np.dot(Hl,gf)
print(X)

#1.(6)극소점 구하기
#1.(6).(a) Random search
maxf = -1e9
a,b = -2,2
c,d = -1,3
n = 10000
for i in range(1,n):
    x = np.random.uniform(a,b)
    y = np.random.uniform(c,d)
    fn = x**2 + y**2 + 2*x - 4*y + 10
    if fn > maxf :
        maxf = fn
        maxx = x
        maxy = y
print("random search로 구한 값",maxx,maxy,maxf)
#1.(6).(b) univariate method
"""def f(x,y):
    return -(x**2 + y**2 + 2*x - 4*y + 10)
def gx(h):
    return f(x+h,y)
def gy(h):
    return f(x,y+h)
x0, y0 = 0.0, 0.0
X1 = [x0]
Y1 = [y0]
for i in range(1,10):
    x,y = x0,y0
    a=brent(gx)
    x0 = x0 + a
    X1.append(x0)
    Y1.append(y0)
    b=brent(gy)
    y0 = y0 + b
    X1.append(x0)
    Y1.append(y0)
    print (i,a,b,x0,y0,-f(x0,y0)) """
#1.(6).(c) scipy.optimize.minimize
def f(x):
    return -(x[0]**2 + x[1]**2 + 2*x[0] -4*x[1] + 10)
x0 = np.array([-1.0,1.0])
a = minimize(f,x0)
print("scipy.optimize.minimize를 이용하여 구한 값",a.x)

#2 Find the shortest distance
print(sep='')
print("#2 Find the shortest distance")
def func(x):
    return x[0]**2-x[1]**2-1
res = minimize(func,[1.0,1.0])
print(res.x)
print(func(res.x))

#3
#3.(1)
def f(x,y):
    z = 2*x**2 - 3*y**2 -2*x
    return z

x = np.linspace(0,4,9)
y = np.linspace(0,4,9)
temp = np.zeros((len(x),len(y)))
for i in range(9):
    for j in range(9):
        temp[j,i] = f(x[i],y[j])
xx,yy = np.meshgrid(x,y)
plt.figure(figsize = (5,3.5))
ax = plt.subplot(1,1,1,projection='3d')
ax.plot_surface(xx,yy,temp)
plt.show()

def T(x):
    return 2*x[0]**2 - 3*x[1]**2 - 2*x[0]

bs = Bounds([0,0],[4,4])
res = minimize(T,[1.0,1.0], bounds=bs)
print(res.x)
print(T(res.x))
