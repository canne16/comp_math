import numpy as np
import random


def randMat(size:int, scale:int):
    '''
        Generates invertible matrixes of size*size elements 
        with non-null diagonal elements. 
        'scale' sets an approximate size of an element    
    '''

    matrix = np.eye(size, dtype=np.int32)
    old_matrix = np.eye(size, dtype=np.int32)

    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i] += old_matrix[j]*random.randint(-scale,scale)  
        
    for i in range(size):
        for j in range(size):
            matrix[i][i] += abs(matrix[i][j])
            # matrix[i][i] += abs(matrix[j][i])
        while matrix[i][i] == 0:
            matrix[i][i] = random.randint(-scale,scale)

        matrix[i][i] *= random.sample([-1, 1], 1)[0]

    return matrix 


def detCalc(matrix:np.ndarray):
    size = matrix.shape[0]
    
    if size == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(size):
            indxs = [j for j in range(size) if j != i]
            rows = np.array([[j]*(size-1) for j in range(1,size)])
            cols = np.array([indxs]*(size-1))
            det += (-1)**(i)*matrix[0][i]*detCalc(matrix[rows, cols])
        return det


def matToSLE(matrix:np.ndarray, scale:int):
    "Returns a column of X and f"
    size = matrix.shape[0]
    x = np.array([random.randint(-scale, scale) for i in range(size)]).astype(int)
    f = matrix @ x

    # printSLE(matrix, x, f)

    return x, f


def printSLE(matrix:np.ndarray, x:np.array, f:np.array):
    size = matrix.shape[0]
    for i in range(size):
        print('[', end='')
        for j in range(size):
            print(f'{matrix[i][j]:4.1f} ', end='')
        print(f'][{x[i]:4.1f}] -> [{f[i]:4.1f}]')
        