import numpy as np
from util import get_gamma, metric


def jacobi(A, f, eps):

    print('jacobi', end=' ')
    x, N_iterations = pre_calc(A, f, eps)
    
    for iter in range(N_iterations):
        x_old = x.copy()
        x = jacobi_core(A, f, x_old, A.shape[0])

    return x


def seidel(A, f, eps):

    print('seidel', end=' ')
    x, N_iterations = pre_calc(A, f, eps)
    
    for iter in range(N_iterations):
        for j in range(A.shape[0]):  
            x[j] = (f[j] - np.dot(A[j], x))/A[j][j] + x[j]

    return x


def jacobi_core(A, f, x_old, N):
    x = x_old.copy()
    for j in range(N):  
        x[j] = (f[j] - np.dot(A[j], x_old))/A[j][j] + x_old[j]
    return x


def pre_calc(A, f, eps):

    N = A.shape[0]
    
    x = np.zeros_like(f, dtype=np.float32)

    gamma = get_gamma(metric, jacobi_core, A, f)
    
    # print('    Jacobi')
    # print(f'\tgamma: {gamma}')

    x_1 = jacobi_core(A, f, x, N)
    if np.allclose(x, x_1, atol=eps):
        return x_1
    
    d_0 = metric(x, x_1)

    # print(f'd_0: {d_0}')
    # print(f'1) {np.log(gamma)}\n2) {eps*(1-gamma)/d_0}\n3)  {np.log(eps*(1-gamma)/d_0)/np.log(gamma)}')
    
    N_iterations = int(np.log(eps*(1-gamma)/d_0)/np.log(gamma))+1
    print(f'iterations: {N_iterations}')

    return x_1, N_iterations

