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
def newton(f, f_prime, x0, eps=1e-11, max_iter=1000000):

	x, x_prev, i = x0, x0 + 2 * eps, 0

	while abs(x - x_prev) >= eps and i < max_iter:
		x_m_1 = x_prev
		x, x_prev, i = x - f(x) / f_prime(x), x, i + 1
		
	print(f"p={(1 - (x - x_prev) / (x_prev  - x_m_1)) ** -1}")


	return x

# Метод Ньютона для вектор-функций
def newton_sys(F, dF, x0, eps=1e-7, max_iter=1000000):

	x, x_prev, i = x0, x0 + 2 * eps, 0

	while np.linalg.norm(x - x_prev) >= eps and i < max_iter:
		dx = np.linalg.solve(dF(x), -F(x))
		x, x_prev, i = x + dx, x, i + 1
		# print(x)

	return x


