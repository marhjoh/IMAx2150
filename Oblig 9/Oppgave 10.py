import numpy as np

# Definer matrisen A
A = np.array([[-0.0891582135625, -1.28344749659, -1.30116310526, -0.91309339248],
              [0.106019795464, 0.794180546675, 0.694019820601, 0.487029573678],
              [0.187389513614, 1.20997546067, 1.33628687589, 0.860822590042],
              [-0.0653955486106, -0.422259535923, -0.428088044463, -0.190801551997]])

# Initialisering av tilnærmede egenverdikandidater
eigenvalue = 1.0
eigenvector = np.array([1.0, 1.0, 1.0, 1.0])

# Antall iterasjoner
iterations = 100
rtol=1e-6

# Potensmetoden
for i in range(iterations):
    # Beregn ny tilnærming til egenverdi
    new_eigenvalue = np.dot(np.dot(eigenvector, A), eigenvector) / np.dot(eigenvector, eigenvector)

    # Beregn ny tilnærming til egenvektor
    eigenvector = np.dot(A, eigenvector)

    # Normaliser egenvektor
    eigenvector /= np.linalg.norm(eigenvector)

    # Sjekk konvergens
    if np.allclose(eigenvalue, new_eigenvalue, rtol):
        break

    eigenvalue = new_eigenvalue

# Skriv ut resultatene
print("Tilnærmet egenverdi:", eigenvalue)
print("Tilnærmet egenvektor:", eigenvector)
