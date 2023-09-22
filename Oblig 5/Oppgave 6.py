import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

def getNAK_System(x_coords, y_coords):
    n = x_coords.size  # Antall punkter

    # delta_i = x_(i+1) - x_i
    delta = np.array([x_coords[i] - x_coords[i - 1] for i in range(1, n)])

    # BigDelta_i = y_(i+1) - y_i
    BigDelta = np.array([y_coords[i] - y_coords[i - 1] for i in range(1, n)])

    A = np.zeros((n, n))

    # Man kan fylle diagonaler i numpy feks slik:
    lowerDiag = np.array([delta[i - 1] for i in range(1, n)])
    # negativ indeksering indekserer baklengs x[-1] = siste element
    lowerDiag[-1] = 1
    # Før vi fyller diagonalen slicer vi matrisen A slik at
    # diagonalen like under hoveddiagonal blir den nye hoveddiagonalen
    # (vi fyller hoveddiagonalen på matrisen vi får ved å fjerne øverste rad og siste kolonne)
    np.fill_diagonal(A[1:, :-1], lowerDiag)

    mainDiag = np.ones(n)
    mainDiag[-1] = -1
    mainDiag[1:-1] = np.array([2 * (delta[i - 1] + delta[i]) for i in range(1, n - 1)])

    upperDiag = np.array([delta[i] for i in range(n - 1)])
    upperDiag[0] = -1

    np.fill_diagonal(A, mainDiag)
    np.fill_diagonal(A[:-1, 1:], upperDiag)

    b = np.zeros(n)
    b[1:-1] = np.array([3 * (BigDelta[i] / delta[i] - BigDelta[i - 1] / delta[i - 1]) for i in range(1, n - 1)])

    return A, b

x = np.array([1, 2, 4, 5., 7, 9])
y = np.array([2, 1, 4, 3., 0, 2])
A, bs = getNAK_System(x, y)

# Now, you can solve the linear system and compute the spline coefficients
spline_coefs = np.linalg.solve(A, bs)

def getNAK_splines(A, b, x_coords, y_coords):
    n = x_coords.size

    # Solve the linear system for c
    c = solve(A, b)

    # Calculate coefficients a, b, and d
    a = y_coords[:-1]
    d = np.zeros(n - 1)
    b = np.zeros(n - 1)

    for i in range(n - 1):
        d[i] = (c[i + 1] - c[i]) / (3 * (x_coords[i + 1] - x_coords[i]))
        b[i] = (y_coords[i + 1] - y_coords[i]) / (x_coords[i + 1] - x_coords[i]) - (x_coords[i + 1] - x_coords[i]) * (
                    2 * c[i] + c[i + 1]) / 3

    return a, b, c, d

A, bs = getNAK_System(x, y)
a, b, c, d = getNAK_splines(A, bs, x, y)

a_t = a
b_t = b
c_t = c
d_t = d

# Plot the splines
for i in range(len(a)):
    xi = np.linspace(x[i], x[i + 1], 100)
    yi = a[i] + b[i] * (xi - x[i]) + c[i] * (xi - x[i]) ** 2 + d[i] * (xi - x[i]) ** 3
    plt.plot(xi, yi)

plt.scatter(x, y, c='red', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Cubic Splines with Not-a-Knot End Conditions')
plt.grid()
plt.show()
