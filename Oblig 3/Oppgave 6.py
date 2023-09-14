import numpy as np


def trapezoidal_method(f, y0, h, t_end):
    num_steps = int(t_end / h) + 1
    t = np.linspace(0, t_end, num_steps)
    w = np.zeros(num_steps)
    w[0] = y0

    for i in range(1, num_steps):
        w[i] = w[i - 1] + 0.5 * h * (f(t[i - 1], w[i - 1]) + f(t[i], w[i]))

    return t, w


# Define the derivative function f(t, y)
f = lambda t, y: t

# Initial values
y0 = 1
h = 0.25
t_end = 1.0

# Solve using trapezoidal method
t, w = trapezoidal_method(f, y0, h, t_end)

# Print the results
for i in range(len(t)):
    print(f"t = {t[i]:.2f}, w = {w[i]:.4f}")
