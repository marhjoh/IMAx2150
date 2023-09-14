import numpy as np


def euler(f, y_init, h, t_slutt):
    n = int(t_slutt / h) + 1
    t = np.arange(0, t_slutt + h, h)
    y = np.zeros((n, len(y_init)))
    y[0, :] = y_init

    for i in range(1, n):
        y[i, :] = y[i - 1, :] + h * f(t[i - 1], y[i - 1, :])

    return t, y


# Definer systemet av differensialligninger
def f(t, y):
    y1_dot = y[1] + y[0]
    y2_dot = y[1] - y[0]
    return np.array([y1_dot, y2_dot])


# Initialbetingelser
y_init = np.array([1.0, 0.0])

# Kjør Eulers metode
t, y = euler(f, y_init, 0.25, 1.0)

# Print resultatene
for i in range(len(t)):
    print(f"t = {t[i]:.2f}, w = [{y[i, 0]:.4f}, {y[i, 1]:.4f}]")
