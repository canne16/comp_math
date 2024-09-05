import numpy as np
import matrix_generator

N = 1000
scale = 5
N_iterations = 100

A = matrix_generator.generate_inv_mat(N, scale)         
x_ref, f = matrix_generator.matrixToSLE(A, scale)       


x = np.array([0]*N).astype('float32')

for cycle in range(N_iterations):
    for j in range(N):  
        x[j] = f[j]/A[j][j] - np.dot(A[j]/A[j][j], x) + x[j]


print('\nReal | Jacobi:\n')

for i in range(N):
    print(f'{x_ref[i]:+} | {x[i]:+}')
