import numpy as np
import matplotlib as mt
from scipy import integrate
import sympy as sp
print("(1). 다음 적분을 계산하라.")
print(sep = '')
print("(a). analytical calculation")
def A(f,a,b,n):
    dx = (b-a)/n
    x = np.arange(a+dx,b+dx,dx)
    return np.sum(f(x)*dx)

def f(x):
    return (np.cos(x))**2
print(A(f,0,np.pi,100))
print(sep = '')
print("(b). trapezoidal n = 1~6")
x = np.linspace(0,np.pi,10)
y = (np.cos(x))**2
print(np.trapz(y,x))
print(sep = '')
print("(c). Simpson's 1/3 n = 2,4,6")
def simpson13(f,a,b,n):
    h = (b-a)/n
    sum = (f(a)+f(b)) * h / 3.0
    for i in range(1,n,2):
        x = a + i*h
        sum = sum + f(x)*h*4.0/3.0
    for i in range(2, n-1, 2):
        x = a + i*h
        sum = sum + f(x) * h * 2.0 / 3.0
    return sum
print("n=2 case",simpson13(f,0,np.pi,2))
print("n=4 case",simpson13(f,0,np.pi,4))
print("n=6 case",simpson13(f,0,np.pi,6))
print(sep = '')
print("(d). Romberg n = 2,4")
def romberg(f,a,b,n):
    h1 = (b-a)/n
    h2 = h1/2
    return 4*f(h2)/3 - f(h1)/3
print("n = 2 case", romberg(f,0,np.pi,2))
print("n = 4 case", romberg(f,0,np.pi,4))
print(sep = '')
print("(e). Gauss quadrature")
def gauss_quadrature(f,a,b):
    return (b-a)*f(a)/2 + (b-a)*f(b)/2
print(gauss_quadrature(f,0,np.pi))
print(sep = '')
print("(f). scipy quad")
print(integrate.quad(f,0,np.pi))
print(sep ='')
print("(g). sympy")
x = sp.Symbol('x')
ff = (sp.cos(x))**2
print(sp.integrate(ff,(x,0,sp.pi)))

print(sep='')
print(("(2). 다음 적분을 계산하라."))
print("(a). analytical calculation")
x,y = sp.symbols('x,y')
ff = x*y
I = sp.integrate(ff,(y,0,x**2))
print(sp.integrate(I,(x,0,1)))
print("(b). scipy quad")
def f(x,y):
    return x*y
def g1(x):
    return 0
def g2(x):
    return x**2
print(integrate.dblquad(f,0,1,g1,g2))
print("(c). sympy")
sp.init_printing(use_latex='mathjax')
x,y = sp.symbols('x,y')
I = sp.integrate(x*y, (y,0,x**2),(x,0,1))
I.doit()
print(I)
print(sep='')
print("(3). monte-carlo 방법을 이용하여 pi값을 계산하라. ")
a,b = 0,1
c,d = 0,1
n = 100000

x = np.random.uniform(a,b,n)
y = np.random.uniform(c,d,n)
fn = np.sqrt(1-x**2)

nc = len(x[np.where(y<=fn)])
S=nc/float(n)*(b-a)*(d-c)
print("반경 1인 원 면적의 1/4은 ",S)
print("pi는 ",S*4)

