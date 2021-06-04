import numpy as np
from scipy.linalg import lu,lu_factor,lu_solve
print("#1. 다음 방정식을 Ax = B 형태의 matrix 방정식으로 변환")
A = np.array([[2,0,-1],[0,5,6],[0,-1,1]],dtype = float)
B = np.array([2,1,2],dtype = float)
print(A)
print(B)
print(sep ='')
print("2.(a) matrix A를 LU로 변환하라.")
def LUdecomp(a,L):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
                L[i,k] = lam
    return a,L
L = np.eye(len(A))
U,L = LUdecomp(A,L)
print('L= ',L)
print('U= ',U)
print(sep ='')
print("2.(b) determinant(LU)를 구하라")
print(np.linalg.det(A))
print(sep = '')
print("2.(c) 변환한 LU 를 이용하여 해 (x,y,z)를 구하라.")
def LUdecomp(a):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if abs(a[i,k]) > 1.0e-9:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
    return a

def LUsolve(a,b):
    n = len(a)
    for k in range(1,n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
LUdecomp(A)
print(A,B)
print("x,y,z = ",LUsolve(A,B))
print(sep = '')
print("2.(d) 변환한 LU를 이용하여 inversion A를 구하라")
I = np.eye(3)

lup = lu_factor(A)
inA = lu_solve(lup,I)
print(inA)
print(sep = '')
print("3.(a) 다음 matrix의 eigenvalue와 eigenvector를 구하라")
M = np.array([[1,-4,2],[-4,1,-2],[2,-2,-2]])
w,v = np.linalg.eigh(M)
print("eigenvalue :",w)
print("eigenvector :",v)
print(sep ='')
print("3.(b) eigenvector가 orthogonal 함을 보여라")
print(int(np.dot(v[0],v[1])))
print(int(np.dot(v[1],v[2])))
print(int(np.dot(v[0],v[2])))
print(sep ='')
print("3.(c) C(trans) = C(inv) 임을 보여라")
C = v
tC = np.transpose(C)
iC = np.linalg.inv(C)
print("transpose C")
print(tC)
print("inverse C")
print(iC)
print(sep ='')
print("3.(d) C(trans)MC = D임을 보여라")
D_inv = np.dot(np.dot(iC,M),C)
print("C(ins)MC = D, D_inv")
print(D_inv)
D_trans = np.dot(np.dot(tC,M),C)
print("C(trans)MC = D, D_trans")
print(D_trans)