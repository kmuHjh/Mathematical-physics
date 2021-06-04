import numpy as np
#(1) Gauss elimination
print("Gauss elimination")
def gauss(a,b):
    n = len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k:n] = a[i,k:n] - lam*a[k,k:n]
                b[i] = b[i] - lam*b[k]
    return a,b
A = np.array([[2,0,-1],[6,5,3],[2,-1,0]])
B = np.array([2,7,4])
A1,B1 = gauss(A,B)
print(A1,B1)
#(2) Cramer's rule
print(sep ='')
print("Cramer's rule")
A = np.array([[2,0,-1],[6,5,3],[2,-1,0]])
B = np.array([2,7,4])

dA = np.linalg.det(A)
C = A.copy()
C[:,0] = B
x = (np.linalg.det(C))/dA
print(x)
print(C)

C = A.copy()
C[:,1] = B
y = np.linalg.det(C)/dA
print(y)
print(C)

C = A.copy()
C[:,2] = B
z = np.linalg.det(C)/dA
print(z)
print(C)

#(3) Inverse matrix
print(sep ='')
print("Inverse matrix")
A = np.array([[2,0,-1],[6,5,3],[2,-1,0]])
B = np.array([2,7,4])
invA = np.linalg.inv(A)
print(invA.dot(B))

#(4) numpy linalg package
print(sep ='')
print("numpy linalg package")
A = np.array([[2,0,-1],[6,5,3],[2,-1,0]])
B = np.array([2,7,4])
C = np.linalg.solve(A,B)
print(C)