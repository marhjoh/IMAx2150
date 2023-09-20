import numpy as np

def trapes(f, y_init, start, stop, h):
    n = int((stop - start) / h) + 1
    t = np.arange(start, stop + h, h)
    y = np.zeros([n, 2])
    y[0, :] = y_init

    for i in range(1, n):
        k1 = h * f(t[i - 1], y[i - 1, :])
        k2 = h * f(t[i], y[i - 1, :] + k1)
        y[i, :] = y[i - 1, :] + 0.5 * (k1 + k2)

    return t, y

# Definer funksjonen f(t, y) som beskriver systemet
def f(t, y):
    y1_dot = y[1] + y[0]
    y2_dot = y[1] - y[0]
    return np.array([y1_dot, y2_dot])

# Initialbetingelser og tidsintervall
y_init = np.array([1.0, 0.0])
start_time = 0.0
end_time = 1.0
step_size = 1/4

# Bruk trapesmetoden
t, y = trapes(f, y_init, start_time, end_time, step_size)

# Skriv ut resultatene som vektorer
for i in range(len(t)):
    print(f"t = {t[i]:.2f}, w = [{y[i, 0]:.4f}, {y[i, 1]:.4f}]")
