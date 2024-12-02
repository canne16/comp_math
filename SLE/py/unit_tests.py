import SLE.matGen as matGen
import numpy as np

def test_det():
    M = None
    print('Scanning for null determinants')
    for N in range(1, 6):
        for i in range(1000):
            M = matGen.randMat(N, 50)
            if matGen.detCalc(M) == 0:
                print('Null determinant found:')
                print(M)
                break
    print(f'{N} - ok')
        

def test_Jacobi():
    M = None
    print('Scanning for Jacobi condition')
    for N in range(2, 6):
        for i in range(1000):
            M = matGen.randMat(N, 50)
            for j in range(N):
                if abs(M[j][j]) < np.sum(np.abs(M[j])) - abs(M[j][j]):
                    print('Fail')
                    print(M)
                    break


    print(f'{N} - ok')

test_det()
test_Jacobi()