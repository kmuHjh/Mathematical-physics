import numpy as np

#1
#(a)
print("#1.(a)")
a = 2**4
print(-1*a,"~",a-1)
print(sep ='')

#(b)
print("#1.(b)")
a = 2**9
print(-1*a,"~",a-1)
print(sep ='')

#2
#(a)
print("#2.(a)")
print("mantissa is",np.finfo(np.float).nmant)
print("exponent is",np.finfo(np.float).maxexp)
print(sep ='')

#(b)
print("#2.(b)")
print("machine epsilon is",np.finfo(np.float).eps)
print(sep ='')

#(c)
print("#2.(c)")
print("max vlaue is",np.finfo(np.float).max)
print("min vlaue is",np.finfo(np.float).tiny)
print(sep ='')

#(d)
print("#2.(d)")
max = (2-2**-1025)*2**1023
print(max)
print(sep ='')

#3
print("#3")
print(np.finfo(np.float).eps)
print(sep ='')

#4
print("#4")
print("{:.50f}".format(1.0))
print("{:.50f}".format(0.1))
print("{:.50f}".format(0.001))
print(sep ='')

#5
print("#5")
def f(n):
    x = 1-(1+10**(-n)-1)*10**n
    return x
for i in range(1,21):
    print(f(i))
print(sep = '')

#6
print("#6.(a)")
num = '101101'
base = 2
answer = int(num,base)
print(answer)
print(sep = '')

print("#6.(b)")
num = '10101100001'
base = 2
answer = int(num,base)
print(answer)
print(sep = '')