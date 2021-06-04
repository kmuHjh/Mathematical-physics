import numpy as np
def f(x):
    return (x-1)/(x**2-1)

epsilon = np.finfo(np.float64).eps
print(epsilon)
x1 = 1 + epsilon
print(x1, f(x1))
x2 = 1 + 1e-17
print(x2, f(x2))

# x1의 경우 epsilon을 더해주었기 때문에 분모에서 1과 근사한 값이 나오더라도
# 1과 같지 않다고 계산하기 때문에 분모가 0이 아니므로 결과값이 나오지만
# x2의 경우 1e-17을 더하더라도 x2의 제곱은 1과 같은 값이라도 판단하여
# x2의 제곱에 1은 뺀 경우 0이되어 0으로 나누는 셈이 되므로 오류가 발생합니다.