import numpy as np
import matplotlib.pyplot as plt


def getNAK_System(x_coords, y_coords):
    n = x_coords.size  # Antall punkter

    # delta_i = x_(i+1) - x_i
    delta = np.array([x_coords[i] - x_coords[i - 1] for i in range(1, n)])

    # BigDelta_i = y_(i+1) - y_i
    BigDelta = np.array([y_coords[i] - y_coords[i - 1] for i in range(1, n)])

    A = np.zeros((n, n))

    # Fyller hoveddiagonalen
    mainDiag = np.ones(n)
    mainDiag[-1] = -1
    mainDiag[1:-1] = np.array([2 * (delta[i - 1] + delta[i]) for i in range(1, n - 1)])

    # Fyller øvre diagonal
    upperDiag = np.array([delta[i] for i in range(n - 1)])
    upperDiag[0] = 0

    # Fyller nedre diagonal
    lowerDiag = np.array([delta[i] for i in range(n - 1)])
    lowerDiag[-1] = 0

    np.fill_diagonal(A, mainDiag)
    np.fill_diagonal(A[1:, :-1], upperDiag)
    np.fill_diagonal(A[:-1, 1:], lowerDiag)

    b = np.zeros(n)
    b[1:-1] = np.array([3 * (BigDelta[i] / delta[i] - BigDelta[i - 1] / delta[i - 1]) for i in range(1, n - 1)])

    return A, b


x = np.array([1, 2, 4, 5., 7, 9])
y = np.array([2, 1, 4, 3., 0, 2])
A, bs = getNAK_System(x, y)

# Løs likningssystemet
spline_coefs = np.linalg.solve(A, bs)

# Legg til endepunktene
spline_coefs = np.concatenate(([0], spline_coefs, [0]))

# Bruk scipy.interpolate til å lage en splinefunksjon
from scipy.interpolate import CubicSpline

spline = CubicSpline(x, y, bc_type=((2, 0), (2, 0)))

# Plot data og spline
x_smooth = np.linspace(min(x), max(x), 500)
y_spline = spline(x_smooth)

plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_smooth, y_spline, label='Cubic Spline (not-a-knot)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Kubisk Spline med Not-a-Knot Endepunkter')
plt.grid()
plt.show()
