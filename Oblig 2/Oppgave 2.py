import numpy as np

def fikspunkt_solve(g, x0, tol):
    x_i = x0
    max_iterations = 1000  # Sett øvre grense for antall iterasjoner

    for i in range(max_iterations):
        x_i = g(x_i)
        if abs(x_i - x0) < tol:
            return x_i
        x0 = x_i

    return x_i

f1 = lambda x: np.cbrt(2*x+2)
f2 = lambda x: np.log(7-x)
f3 = lambda x: np.log(4 - np.sin(x))

startverdier = [np.sqrt((2/3)), 1.5, 1.0]  # Passende startverdier for hver funksjon
funcs = [f1, f2, f3]
maks_feil = 1e-8
sols = []

for func, x0 in zip(funcs, startverdier):           # Kombiner elementene fra listene
    x_sol = fikspunkt_solve(func, x0, maks_feil)  # Bruk riktig funksjon og startverdi x0
    sols.append(x_sol)

print(f"Løsning til første ligning x = {sols[0]}")
print(f"Løsning til andre ligning x = {sols[1]}")
print(f"Løsning til tredje ligning x = {sols[2]}")
