import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt

def getNAK_System(x_coords, y_coords):
    n = x_coords.size

    # Compute differences
    delta = np.diff(x_coords)
    BigDelta = np.diff(y_coords)

    # Initialize the system matrix A
    A = np.zeros((n - 2, n - 2))

    # Fill the diagonals with A
    for i in range(n - 2):
        A[i, i] = 2 * (delta[i] + delta[i + 1])
        if i > 0:
            A[i, i - 1] = delta[i]
            A[i - 1, i] = delta[i]

    # Initialize the right-hand side vector b
    b = np.zeros(n - 2)

    for i in range(n - 2):
        b[i] = 3 * (BigDelta[i] / delta[i + 1] - BigDelta[i + 1] / delta[i])

    return A, b

def getNAK_splines(A, b, x_coords, y_coords):
    n = x_coords.size
    delta = np.diff(x_coords)
    BigDelta = np.diff(y_coords)

    # Solve the system for c values
    c = np.zeros(n)
    c[1:-1] = solve(A, b)

    # Compute d values
    d = np.zeros(n - 1)
    for i in range(n - 1):
        d[i] = (c[i + 1] - c[i]) / (3 * delta[i])

    # Compute a and b values
    a = y_coords[:-1]
    b = np.zeros(n - 1)
    for i in range(n - 1):
        b[i] = (BigDelta[i] / delta[i]) - (delta[i] / 3) * (2 * c[i] + c[i + 1])

    return a, b, c, d

x = np.array([1, 2, 4, 5., 7, 9])
y = np.array([2, 1, 4, 3., 0, 2])

A, bs = getNAK_System(x, y)
a, b, c, d = getNAK_splines(A, bs, x, y)

# Plot the cubic splines
for i in range(len(x) - 1):
    S = lambda t, i=i: a[i] + b[i] * (t - x[i]) + c[i] * (t - x[i]) ** 2 + d[i] * (t - x[i]) ** 3
    t = np.linspace(x[i], x[i + 1], 100)
    plt.plot(t, S(t))

# Plot data points
plt.scatter(x, y, c='red', label='Data Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Cubic Splines with Not-a-Knot End Conditions')
plt.grid()
plt.show()
