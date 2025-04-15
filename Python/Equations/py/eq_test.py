import numpy as np
from solver import bisect, newton

eps = 1e-12
a = -10
b = 10

def func(x):
    return (x-np.pi)**9

def deriv_1(x):
    return 9*(x-np.pi)**8

# x = bisect(func, a, b, eps)
x = newton(func, deriv_1, 5)

print(f'{x:.13f}')    