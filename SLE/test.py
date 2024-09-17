import matGen
from Jacobi import solve_jacobi
from util import metr

eps = 1e-20
N = 10
scale = 100

print(f'\nEpsilon: {eps}')

A = matGen.randMat(N, scale)         
x_ref, f = matGen.matToSLE(A, scale)       

x = solve_jacobi(A, f, eps)

if metr(x, x_ref) > eps:
    print(f'bruh: norm(x-x_ref) {metr(x, x_ref)} > {eps} eps')


# print('\n' + ' '*5 + 'Real | Jacobi:\n')
# for i in range(N):
#     print(f'{x_ref[i]:+9} | {x[i]:+}')