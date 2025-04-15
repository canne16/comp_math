import numpy as np
import matplotlib.pyplot as plt

# i-й множитель в многочлене Лагранжа
def coeff(x, i, x_points):
    res = 1
    for j in range(len(x_points)):
        if j != i:
            res *= (x - x_points[j]) / (x_points[i] - x_points[j])
    return res

# интерполяционный многочлен Лагранжа
def lagrange_interpolation(x, x_points, y_points):
    result = 0
    for i in range(len(x_points)):
        result += y_points[i] * coeff(x, i, x_points)
    return result

# Разделенные разности для многочлена Ньютона
def divided_differences(x_points, y_points):
    n = len(x_points)
    coef = np.zeros([n, n])
    coef[:,0] = y_points

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x_points[i+j] - x_points[i])

    return coef[0]

# интерполяционный многочлен Ньютона
def newton_interpolation(x, x_points, coef):
    n = len(coef)
    result = coef[0]
    product = 1.0
    for i in range(1, n):
        product *= (x - x_points[i-1])
        result += coef[i] * product
    return result

