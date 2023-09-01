import numpy as np


def naive_gauss(A, b):
    n, m = np.shape(A)
    S = np.zeros((n, n + 1))
    S[:, 0:n] = A
    S[:, -1] = b
    for j in range(n - 1):
        for i in range(j + 1, n):
            mult = S[i, j] / S[j, j]
            S[i, j] = 0.0
            for k in range(j + 1, n + 1):
                S[i, k] = S[i, k] - mult * S[j, k]

    return S[:, 0:n], S[:, -1]


# Definer A og b
A = np.array([[1, 2, -1], [0, 3, 1], [2, -1, 1]])
b = np.array([2, 4, 2]).reshape((-1))

Ar, br = naive_gauss(A, b)
print("Naiv gausseliminasjon av A:")
print(Ar)
print("Resultatvektor b:")
print(br)
