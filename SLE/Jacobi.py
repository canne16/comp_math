import numpy as np
import SLE.matGen as matGen

N = 10
scale = 5
N_iterations = 100

A = matGen.randMat(N, scale)         
x_ref, f = matGen.matToSLE(A, scale)       


x = np.zeros_like(f)

for iteration in range(N_iterations):
    for j in range(N):  
        x[j] = f[j]/A[j][j] - np.dot(A[j]/A[j][j], x) + x[j]


print('\nReal | Jacobi:\n')

for i in range(N):
    print(f'{x_ref[i]:+} | {x[i]:+}')
