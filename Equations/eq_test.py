import numpy as np
from solver import bisect, newton

eps = 1e-12
a = 0
b = 2**10

def func(x):
    return 1/x-1

def deriv_1(x):
    return -1/x**2

def deriv_2(x):
    return 1/2/x**3

# x = bisect(func, a, b, eps)
x = newton(func, deriv_1, deriv_2, a, b, eps)

print(x)    