from matGen import randMat, matToSLE, printSLE
from sys_solver import jacobi, seidel
from util import metric
import numpy as np

eps = 1e-3
N = 4
scale = 100

print(f'\nEpsilon: {eps}')

for i in range(1):

    # A = randMat(N, scale)
    # x_ref, f = matToSLE(A, scale)
    
    A = np.array([
        [10.123, 5.352, 3.123],
        [3.11, 21.34, 1.19],
        [3.14, 4.47, 11.99],
    ], dtype=np.float32)

    x_ref = np.array([2.71, 3.14, 4.13])
    f = A @ x_ref

    printSLE(A, x_ref, f)

    x_1 = jacobi(A, f, eps)
    x_2 = seidel(A, f, eps)

    if metric(x_2, x_ref) > eps:
        print(f'bruh: norm(x-x_ref) {metric(x_2, x_ref)} > {eps} eps')

    print('\n' + ' '*5 + 'Real |' + ' '*4 + 'Jacobi |' + ' '*5 + 'Seidel:\n')
    for i in range(x_1.shape[0]):
        print(f'{x_ref[i]:+9.3f} | {x_1[i]:+9.3f} | {x_2[i]:+9.3f}')
