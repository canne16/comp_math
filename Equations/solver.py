import numpy as np


# Метод бисекции, func(a)*func(b) < 0
def bisect(func, a, b, eps):
    
    while abs(a-b) > eps:
        c = (b+a)/2
        if func(c)*func(a) < 0:
            b = c
        else:
            a = c

    return (a+b)/2

# Метод Ньютона
def newton(func, deriv_1, deriv_2, a, b, eps = 0):
    
    x_old = (a+b)/2

    while func(x_old)*deriv_2(x_old) <= 0:
        x_old = a+(b-a)*np.random.rand()

    if eps:
        while True:
            print(x_old)
            x = x_old - func(x_old)/deriv_1(x_old)

            if abs(x-x_old) < eps/2:
                break
            x_old = x

    else:
        x_old_old = x_old-1
        delta_fr = 0

        while True:
            print(x_old)
            x = x_old - func(x_old)/deriv_1(x_old)
    
            delta_fr = (x-x_old)/(x-x_old_old)

            x_old_old = x_old
            x_old = x


            print(f'delta: {delta_fr}')
            print(f'p: {1/(1-delta_fr)} ~ {int(1/(1-delta_fr))}')

    return x

