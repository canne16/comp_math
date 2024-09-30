import numpy as np
from util import get_gamma, metric
from matGen import printSLE

# Метод Якоби
def jacobi(A, f, eps):

    print('jacobi', end=' ')
    x, N_iterations = pre_calc(A, f, eps)
    
    for iter in range(N_iterations):
        x_old = x.copy()
        x = jacobi_core(A, f, x_old, A.shape[0])

    return x

# Метод Зейделя
def seidel(A, f, eps):

    print('seidel', end=' ')
    x, N_iterations = pre_calc(A, f, eps)
    
    for iter in range(N_iterations):
        for j in range(A.shape[0]):  
            x[j] = (f[j] - np.dot(A[j], x))/A[j][j] + x[j]

    return x

# Итерационаая часть алгоритма якоби
def jacobi_core(A, f, x_old, N):
    x = x_old.copy()
    for j in range(N):  
        x[j] = (f[j] - np.dot(A[j], x_old))/A[j][j] + x_old[j]
    return x

# Определение числа итераций
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

# Частный случай прямого метода на 3-диагональной матрице
def fwd_3(A, f):
    
    N = A.shape[0]

    x = np.zeros_like(f, dtype=np.float32)
    
    E = np.zeros(N-1, dtype=np.float32)
    F = np.zeros(N-1, dtype=np.float32)
    
    E[0] = f[0]/A[0][0]
    F[0] = -A[0][1]/A[0][0]

    for i in range(1, N-1):
        E[i] = (f[i]-A[i][i-1]*E[i-1])/(A[i][i-1]*F[i-1]+A[i][i])
        F[i] = -A[i][i+1]/(A[i][i-1]*F[i-1]+A[i][i])

    x[N-1] = (f[N-1]-A[N-1][N-2]*E[N-2])/(A[N-1][N-1]+A[N-1][N-2]*F[N-2])

    for i in range(N-2, -1, -1):
        x[i] = E[i] + F[i]*x[i+1]

    return x

# Метод наискорейшего спуска
def grad_desc(A, f, eps):

    x = np.zeros_like(f)
    x_new = x.copy()

    if np.any(A.T!=A):
        f = A.T @ f
        A = A.T @ A

    while True:
        x = x_new
        r = A @ x - f
        alpha = np.dot(r, r)/np.dot(A@r, r)
        x_new = x - alpha*r
        
        if metric(x, x_new) < eps/2:
            break

    return x_new

