import numpy as np
np.random.seed(27)
a = np.random.randint(1, 10, size=(3, 2))
b = np.random.randint(1, 10, size=(2, 3))
print(f"Matrix A:\n {a}\n")
print(f"Matrix B:\n {b}\n")


def multiply_matrix(A, B):
    global C
    if A.shape[1] == B.shape[0]:
        C = np.zeros((A.shape[0], B.shape[1]), dtype=int)
        for row in range(A.shape[0]):
            for col in range(B.shape[1]):
                for elt in range(len(B)):
                    C[row, col] += A[row, elt] * B[elt, col]
        print(f"Result:\n {C}\n")
    else:
        print("Sorry, cannot multiply A and B.")


multiply_matrix(a, b)