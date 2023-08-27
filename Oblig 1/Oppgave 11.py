import numpy as np
from decimal import Decimal, getcontext

# Angi antall desimaler for høy presisjon
getcontext().prec = 50  # Angi ønsket antall desimaler

# Lengdene av kateterne og det lengste beinet
a = Decimal("3344556600.0")
b = Decimal("1.2222222")

# Beregn hypotenusen
c = np.sqrt(a**2 + b**2)
#print(hyp - katet_a)

# Finn differansen mellom hypotenusen og det lengste beinet
diff = c - max(a, b)

# Skriv ut resultatet med høy presisjon
print(f"Hypotenusen er {diff:.50f} lengdeenheter lenger enn det lengste beinet i trekanten.")
print(c-a)