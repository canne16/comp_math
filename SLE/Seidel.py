import numpy as np
import matGen

N = 10
scale = 100
eps = 1e-6
gamma = 1
N_iterations = 0

A = matGen.randMat(N, scale)         
x_ref, f = matGen.matToSLE(A, scale)       


x = np.zeros_like(f)

for iter in range(N_iterations):
    for j in range(N):  
        x[j] = (f[j] - np.dot(A[j], x))/A[j][j] + x[j]


print('\n' + ' '*5 + 'Real | Seidel:\n')
for i in range(N):
    print(f'{x_ref[i]:+9} | {x[i]:+}')