import numpy as np
import pylab as pl
from scipy.optimize import curve_fit
import math
print("(1).(a)")
x = np.array([0.75,2,3,4,6,8,8.5])
y = np.array([1.2,1.95,2,2.4,2.4,2.7,2.6])

def polyfit(x,y,m):
    A = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    for i in range(m+1):
        b[i] = np.sum(np.dot(x**i,y))
        for j in range(m+1):
            A[i,j] = np.sum(x**(i+j))
    return np.linalg.solve(A,b)
print(polyfit(x,y,1))
print("(1).(b)")
def f(x):
    return 1.46532204*x + 0.15481382
newY = []
for i in range(0,7):
    newY.append(f(x[i]))
pl.plot(x,newY)
print("(1).(c)")
sub = []
for i in range(0,7):
    sub.append(abs(y[i]-newY[i]))
newS = []
for i in range(0,7):
    newS.append(sub[i]**2)
print("오차의 제곱합 : ",np.sum(newS))
print("오차의 표준편차 :", np.std(sub, ddof=1))
print("(2).(a)")
x = np.array([1.2,2.8,4.3,5.4,6.8,7.9])
y = np.array([7.5,16.1,38.9,67.0,146.6,266.2])
z = np.polyfit(x,y,2)
def f(x):
    return z[0]*(x**2) + z[1]*x + z[2]
newY = []
for i in range(0,6):
    newY.append(f(x[i]))
print(newY)
pl.plot(x,newY)
print("(2).(b)")
def f(x,a,b,c):
    f = a*np.exp(b*x) + c
    return f
popt, pcov = curve_fit(f,x,y)
print(popt)
newY = []
for i in range(0,6):
    newY.append(3.53227072*np.exp(0.54695019*x[i]) + 0.47392348)
pl.plot(x,newY)
print("(3).(a)")
x = []
def fx(x):
    return (x*np.pi)/20
for i in range(0,21):
    x.append(fx(i))
y = []
for i in range(0,21):
    y.append(np.cos(x[i]))
z = np.polyfit(x,y,10)
newY = []
for i in range(0,21):
    newY.append(z[0]*x[i]**10+z[1]*x[i]**9+z[2]*x[i]**8+z[3]*x[i]**7+z[4]*x[i]**6+z[5]*x[i]**5+z[6]*x[i]**4+z[7]*x[i]**3+z[8]*x[i]**2+z[9]*x[i]+z[10])
print("10차 fitting 값",z)
print("(3).(b)")
pl.figure(2)
pl.plot(x,newY)
print("(3).(c)")
def tcos(x):
    temp = 0
    for i in range(0,11):
        temp = temp + (-1)**i * x**(2*i) / math.factorial(2*i)
    return temp
tY = []
for i in range(0,21):
    tY.append(tcos(x[i]))
sub = []
for i in range(0,21):
    sub.append(newY[i]-tY[i])
print("fiiting값 - 테일러값")
for i in range(0,21):
    print(sub[i])