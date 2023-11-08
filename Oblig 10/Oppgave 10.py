# Merknad: Selv om flere løsninger er mulige
# skal du i definisjonene f1(x,y) og f2(x,y)
# flytte alt mot venstre side av likhetstegnet
# i likningene over for å få uttelling på disse
# oppgavene.
import numpy as np


def f1(x, y):
    return x ** 4 - 7 * x ** 2 + 13 - 7 * y ** 2 + y ** 4


def f2(x, y):
    return x ** 2 - 4 + (y + 2) ** 2


def jacobian(x, y):
    df1x = 4 * x ** 3 - 14 * x
    df1y = 4 * y ** 3 - 14 * y
    df2x = 2 * x
    df2y = 2 * y + 4
    J = np.array([df1x, df1y, df2x, df2y]).reshape((2, 2))
    return J


def newtons(f1, f2, x0, y0, tol):
    X_old = np.zeros((2, 1))
    F = np.zeros((2, 1))
    X_old[0] = x0
    X_old[1] = y0

    F[0] = f1(X_old[0], X_old[1])
    F[1] = f2(X_old[0], X_old[1])
    error = F[0] ** 2 + F[1] ** 2
    iterations = 0
    while error > tol and iterations < 500:
        F[0] = f1(X_old[0], X_old[1])
        F[1] = f2(X_old[0], X_old[1])
        J = jacobian(X_old[0], X_old[1])
        try:
            s = np.linalg.solve(-J, F)
        except np.linalg.LinAlgError:
            print(f'Newtons metode feilet etter {iterations} iterasjoner, LinAlgError')
            return 'f', 'f'
        X_old[0] = X_old[0] + s[0]
        X_old[1] = X_old[1] + s[1]
        iterations += 1
        error = F[0] ** 2 + F[1] ** 2

    return X_old[0], X_old[1]


def solve(x0, y0):
    x, y = newtons(f1, f2, x0, y0, 0.01)
    return x, y
