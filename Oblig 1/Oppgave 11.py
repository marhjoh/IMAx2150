import numpy as np

# Lengdene av kateterne og det lengste beinet
katet_a = 3344556600.0
katet_b = 1.2222222

# Beregn hypotenusen
hyp = np.sqrt(katet_a**2 + katet_b**2)
print(hyp-katet_a)

# Finn differansen mellom hypotenusen og det lengste beinet
diff = hyp - max(katet_a, katet_b)

# Skriv ut resultatet
print(f"Hypotenusen er {diff:.12f} lengdeenheter lenger enn det lengste beinet.")
