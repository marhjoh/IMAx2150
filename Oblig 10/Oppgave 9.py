import numpy as np
from scipy.optimize import minimize

# Data
x = np.array([0, 1, 2, 3, 4])
y = np.array([3, 8, 19, 49, 137])

# Modell
model = lambda p, x: p[0] * x + p[1]

# Kvadratisk feilfunksjon
error = lambda p, x, y: np.sum((np.log(y) - model(p, x))**2)

# Initialisering av parametre a og b
initial_params = [1, 0]

# Minimer feilfunksjonen med hensyn til parametrene a og b
result = minimize(error, initial_params, args=(x, y))

# Hent optimale parametre
optimal_params = result.x

# Parameter a og b
a, b = optimal_params

print(f"Optimal a: {a}, Optimal b: {b}")
