import numpy as np
import random


def generate_inv_mat(size:int, scale:int):
    '''
        Generates invertible matrixes of size*size elements 
        with non-null diagonal elements. 
        'scale' sets an approximate size of an element    
    '''

    matrix = np.eye(size).astype(int)
    old_matrix = np.eye(size).astype(int)

    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i] += old_matrix[j]*random.randint(-scale,scale)  
        
    for i in range(size):
        for j in range(size):
            matrix[i][i] += abs(matrix[i][j])
        matrix[i][i] *= random.sample([-1, 1], 1)[0]

    return matrix 


def matJacobiCorr(matrix:np.ndarray):
    size = matrix.shape[0]

    diffs = [np.sum(np.abs(matrix[i]))-2*abs(matrix[i][i]) for i in range(size)]

    max_arg = np.argmax(diffs)
    if diffs[max_arg] > 0:
        if matrix[max_arg][max_arg] > 0:
            matrix = matrix + np.eye(size)*(diffs[max_arg]+1)
        else:
            matrix = matrix - np.eye(size)*(diffs[max_arg]+1)
        
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


def matrixToSLE(matrix:np.ndarray, scale:int):
    "Returns a column of X and f"
    size = matrix.shape[0]
    x = np.array([random.randint(-scale, scale) for i in range(size)]).astype(int)
    f = matrix @ x

    printSLE(matrix, x, f)

    return x, f


def printSLE(matrix:np.ndarray, x:np.array, f:np.array):
    size = matrix.shape[0]
    for i in range(size):
        print(f'{matrix[i]} [{x[i]:3}] -> [{f[i]}]')
