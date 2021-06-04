import numpy as np
import pylab as pl
#6.11
def f(x):
    return (np.exp(-0.5*x)*(4-x)-2)

#(a)
def df(x):
    return -np.exp(-0.5*x) -0.5*np.exp(-0.5*x)*(4-x) -2

x_0 = 2
newX = x_0
i = 0
print("x0 is 2 case")
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1

print(sep='')
x_0 = 6
newX = x_0
i = 0
print("x0 is 6 case")
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1

print(sep='')
x_0 = 8
newX = x_0
i = 0
print("x0 is 8 case")
while abs(f(newX)) > 1e-10:
    newX = newX - f(newX)/df(newX)
    print(i,newX,f(newX))
    i = i+1
print(sep ='')
print("초기값을 2,6,8으로 주었을때 모두 수렴하고 2,6,8에서 가장 가까운 해가 0.88이기때문에 모두 같은 결과가 도출되는 거 같습니다")