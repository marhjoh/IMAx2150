import numpy as np

A = np.array([[3, 2], [3, 3], [1, 1]])
b = np.array([[1], [1], [1]])

# Bruk normal ligninger for å finne x
ATA = np.dot(A.T, A)
ATb = np.dot(A.T, b)
x = np.linalg.solve(ATA, ATb)

print("Minste kvadraters løsning x:")
print(x)
