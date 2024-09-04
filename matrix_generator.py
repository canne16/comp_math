import numpy as np
import random

def generate_inv_mat(size:int, limit:int):
    "Generates invertible matrixes of n*n elements. limit sets an approximate size of element"
    matrix = np.eye(size)
    old_matrix = np.eye(size)

    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i] += old_matrix[j]*random.randint(-limit,limit)  
        
    for i in range(size):
        matrix[i][i] *= random.randint(-limit, limit)
    
    return matrix 


def determinant(matrix:np.ndarray):
    size = matrix.shape[0]
    
    if size == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(size):
            indxs = [j for j in range(size) if j != i]
            rows = np.array([[j]*(size-1) for j in range(1,size)])
            cols = np.array([indxs]*(size-1))
            det += (-1)**(i)*matrix[0][i]*determinant(matrix[rows, cols])
        return det

def matrixToSLE(matrix:np.ndarray, limit:int):
    "Returns a column of X and f"
    size = matrix.shape[0]
    x = np.array([random.randint(-limit, limit) for i in range(size)])
    f = matrix @ x

    printSLE(matrix, x, f)

    return x, f

def printSLE(matrix:np.ndarray, x:np.array, f:np.array):
    size = matrix.shape[0]
    for i in range(size):
        print(f'{matrix[i]} [{x[i]:3}] -> [{f[i]}]')
