import numpy as np
#gauss elimin
def gauss(a):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
    return a

A = np.array([[-2,4,7,3],[8,2,-9,5],[-4,6,8,4],[2,-9,3,8]])
dA = gauss(A)
ddA = np.diag(dA)
np.prod(ddA)
 # numpy linalg package

np.linalg.det(A)