import numpy as np

# Definer matrisen A
A = np.array([[1, 2], [3, 4]])

# Beregn uendelighetsnormen til matrisen A
norm_A = np.linalg.norm(A, np.inf)

# Velg en vilkårlig vektor x (for eksempel [1, 1])
x = np.array([1, 1])

# Beregn A*x
Ax = np.dot(A, x)

# Beregn uendelighetsnormen til A*x
norm_Ax = np.linalg.norm(Ax, np.inf)

# Beregn uendelighetsnormen til x
norm_x = np.linalg.norm(x, np.inf)

# Beregn (||A_x||∞)/(||x||∞)
result = norm_Ax / norm_x

# Sammenlign med ||A||∞
if np.isclose(result, norm_A, 1e-6):
    print("Vektoren x tilfredsstiller ligningen.")
else:
    print("Vektoren x tilfredsstiller ikke ligningen.")
