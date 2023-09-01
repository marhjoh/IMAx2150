import numpy as np

# Definer matrisen A
A = np.array([[1, 2.01], [3, 6]])

# Beregn uendelighetsnormen til A
norm_A = np.linalg.norm(A, np.inf)

# Beregn den inverse av A
A_inv = np.linalg.inv(A)

# Beregn uendelighetsnormen til den inverse av A
norm_A_inv = np.linalg.norm(A_inv, np.inf)

# Beregn kondisjonstallet K(A)
condition_number = norm_A * norm_A_inv

print(f"Uendelighetsnormen til A er: {norm_A}")
print(f"Uendelighetsnormen til A^-1 er: {norm_A_inv}")
print(f"Kondisjonstallet til A er: {condition_number}")
