from matGen import randMat, matToSLE, printSLE
from sys_solver import grad_desc
import numpy as np

eps = 1e-10
N = 4
scale = 10

for i in range(1):

    A = np.array([
        [1, 0, 3],
        [0, 1, 0],
        [0, 0, 1],
    ], dtype=np.float32)

    x_ref = np.array([1, 2, 3])
    f = A @ x_ref
    
    printSLE(A, x_ref, f)

    x = grad_desc(A, f, eps)

    print('\n' + ' '*5 + 'Real |' + ' '*4 + 'Grad_desc:\n')
    for i in range(x.shape[0]):
        print(f'{x_ref[i]:+9.3f} | {x[i]:+9.3f}')
