import numpy as np
from solver import bisect, newton

eps = 1e-12
a = -10
b = 10

def func(x):
    return x**10

def deriv_1(x):
    return 10*x**9

def deriv_2(x):
    return 90*x**8

# x = bisect(func, a, b, eps)
x = newton(func, deriv_1, deriv_2, a, b)

print(f'{x:.13f}')    