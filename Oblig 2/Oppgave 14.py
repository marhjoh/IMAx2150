import numpy as np


def LUfactorize(A):
    n, m = np.shape(A)

    if n != m:
        raise ValueError("Inputmatrisen må være kvadratisk.")

    L = np.eye(n)
    U = A.copy()

    for j in range(n):
        if U[j, j] == 0:
            raise np.linalg.LinAlgError("Zero pivot encountered")
            return None, None

        for i in range(j + 1, n):
            mult = U[i, j] / U[j, j]
            L[i, j] = mult
            U[i, j:] -= mult * U[j, j:]

    return L, U


# Eksempel
A = np.array([[1.0, 2, -1], [0, 3, 1], [2, -1, 1]])
A = A.reshape((3, 3))

try:
    L, U = LUfactorize(A)
except np.linalg.LinAlgError as e:
    print(f"LinAlgError: {e}")
