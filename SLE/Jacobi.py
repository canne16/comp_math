import numpy as np
from util import get_gamma, metr

def solve_jacobi(A, f, eps):

    N = A.shape[0]
    
    x = np.zeros_like(f)

    gamma = get_gamma(metr, func, A, f)
    d_0 = metr(x, func(A, f, x, N))
    N_iterations = int(np.log(eps*(1-gamma)/d_0)/np.log(gamma))
    
    print(f'Iterations: {N_iterations}')
    
    for iter in range(N_iterations):
        x_old = x.copy()
        x = func(A, f, x_old, N)

    return x

def func(A, f, x_old, N):
    x = np.array([0]*N, dtype=np.float32)
    for j in range(N):  
        x[j] = (f[j] - np.dot(A[j], x_old))/A[j][j] + x_old[j]
    return x