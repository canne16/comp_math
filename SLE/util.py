import numpy as np

def get_gamma(metr, func, A, f):
    N = A.shape[0]
    x1 = np.array([0]*N)
    x2 = np.array([1]*N)
    return metr(func(A, f, x1, N), func(A, f, x2, N))/metr(x1, x2)

def norm_r(x: np.array):
    return max(np.abs(x))

def norm_1(x: np.array):
    return np.sum(np.abs(x))

def norm_2(x: np.array):
    return np.sqrt(np.sum(np.square(x)))

def norm_p(x: np.array, p: int):
    return np.sum(pow(x, p))**(1/p)

def metr(x1: np.array, x2: np.array):
    return norm_r(x1-x2)