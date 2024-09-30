import numpy as np

def get_gamma(metric, core, A, f):
    N = A.shape[0]
    guesses = 2**10
    x1 = np.random.randint(-2**12, 2**12,size=(guesses, N))
    x2 = np.random.randint(-2**12, 2**12,size=(guesses, N))

    gamma = [metric(core(A, f, x1[i], N), core(A, f, x2[i], N))/metric(x1[i], x2[i]) for i in range(guesses)] 
    return max(gamma) 

def norm_r(x: np.array):
    return max(np.abs(x))

def norm_1(x: np.array):
    return np.sum(np.abs(x))

def norm_2(x: np.array):
    return np.sqrt(np.sum(np.square(x)))

def norm_p(x: np.array, p: int):
    return np.sum(pow(x, p))**(1/p)

def metric(x1: np.array, x2: np.array):
    return norm_2(x1-x2)