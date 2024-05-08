import numpy as np
import time

n = 1000
A = np.random.randint(1,10,(n,n))
B = np.random.randint(1,10,(n,n))

A_matrix = np.asmatrix(A)
B_matrix = np.asmatrix(B)

def dot_array(A, B):
    start_time = time.time()
    
    A_result = A.dot(B)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The function took {elapsed_time} seconds to run.")
    return A_result

def dot_matrix(A_matrix, B_matrix):
    start_time = time.time()
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    A_result = A_matrix@B_matrix

    print(f"The function took {elapsed_time} seconds to run.")
    return A_result
    

def matrix_dot_for(A_matrix, B_matrix):
    start_time = time.time()
    A_result = np.zeros((n,n))
    for row in range(n):
        for col in range(n):
            A_result[row,col] = A_matrix[row,:].dot(B_matrix[:,col])
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"The function took {elapsed_time} seconds to run.")
    return A_result

def array_dot_for(A, B):
    start_time = time.time()
    A_result = np.zeros((n,n))
    for row in range(n):
        for col in range(n):
            A_result[row,col] = A[row,:].dot(B[:,col])
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"The function took {elapsed_time} seconds to run.")
    return A_result




def main():
    dot_array(A,B)
    dot_matrix(A_matrix,B_matrix)
    matrix_dot_for(A_matrix,B_matrix)
    array_dot_for(A, B)


main()