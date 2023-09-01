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


def LUsolve(L, U, b):
    c = np.zeros_like(b)
    n = len(c)

    for i in range(n):
        c[i] = b[i]
        for j in range(i):
            c[i] -= L[i, j] * c[j]

    x = np.zeros_like(b)

    for i in range(n - 1, -1, -1):
        x[i] = c[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x


A = np.array([[3.0, 1.0, 2.0], [6.0, 3.0, 4.0], [3.0, 1.0, 5.0]])
b = np.array([0.0, 1.0, 3.0])  # Define b as a float array

try:
    L, U = LUfactorize(A)
    x = LUsolve(L, U, b)
    print("Løsning x:")
    print(x)
except np.linalg.LinAlgError as e:
    print(f"LinAlgError: {e}")
