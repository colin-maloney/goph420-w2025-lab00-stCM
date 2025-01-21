import numpy as np
from goph420_lab00 import (
add, 
multiply,  
)

def main():
    print(f'multiply(2, 12.): {multiply(2, 12.)}')
    # test for arrays
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = 2. * np.ones(A.shape) 
    C = 64 
    D = 8
    print(f'A:\n{A}')
    print(f'B:\n{B}')
    print(f'add(A, B):\n{add(A, B)}')
    print(f'multiply(A, B):\n{multiply(A, B)}')

if __name__ == '__main__':
    main()
