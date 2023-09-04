import numpy as np

def naive_gauss_with_backsub(A, b):
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

    x = S[:, -1]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] = x[i] - S[i, j] * x[j]
        x[i] = x[i] / S[i, i]
    return x


A = np.array([1, 2, -1, 0, 3, 1, 2, -1, 1])
A = A.reshape((3, 3))
b = np.array([2, 4, 2]).T
x = naive_gauss_with_backsub(A, b)
print("Løsning x: ")
print(x)