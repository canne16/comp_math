import numpy as np
from solver import newton_sys

# f1 и производные
def f1(x, y):
    return x**2 + y**2 - 4

def dfx1(x, y):
    return 2*x

def dfy1(x, y):
    return 2*y

# f2 и производные
def f2(x, y):
    return x**2 - y**2 - 1

def dfx2(x, y):
    return 2*x

def dfy2(x, y):
    return -2*y

# Система F из f1 и f2
def F(X):
    x, y = X
    return np.array([f1(x, y), f2(x, y)])

def dF(X):
    x, y = X
    return np.array([dfx1(x, y), dfy1(x, y), dfx2(x, y), dfy2(x, y)]).reshape((2, 2))

X = np.array([10, 10])

print(dF(X))
print("----------")

print(newton_sys(F, dF, X))