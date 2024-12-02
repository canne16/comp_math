from matGen import randMat, matToSLE, printSLE
from sys_solver import fwd_3
import numpy as np

N = 4
scale = 10

for i in range(1):

    A = randMat(N, scale)
    for i in range(N):
        for j in range(N):
            if abs(i-j) > 1:
                A[i][j] = 0
    
    x_ref, f = matToSLE(A, scale)

    printSLE(A, x_ref, f)

    x = fwd_3(A, f)

    print('\n' + ' '*5 + 'Real |' + ' '*4 + 'fwd_3:\n')
    for i in range(x.shape[0]):
        print(f'{x_ref[i]:+9.3f} | {x[i]:+9.3f}')
