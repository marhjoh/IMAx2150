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

    # Tilbakeinnsetting
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = S[i, -1] / S[i, i]
        for j in range(i - 1, -1, -1):
            S[j, -1] = S[j, -1] - S[j, i] * x[i]

    return x

# Definer A og b
A = np.array([[1, 2, -1], [0, 3, 1], [2, -1, 1]])
b = np.array([2, 4, 2]).reshape((-1,))  # Definer b som en vektor med form (3,)
x = naive_gauss_with_backsub(A, b)
print("Løsning x: ")
print(x)