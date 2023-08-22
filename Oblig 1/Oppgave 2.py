import numpy as np

# Denne funksjonen skal evaluere polynomet med koeffisienter c[] i x vha horners metode
def nest(c, x):
    n = len(c) - 1
    result = c[n]

    for i in range(n - 1, -1, -1):
        result = result * x + c[i]

    return result

# Denne funksjonen printer ut feilen man får når man bruker funksjonen "funk(c,x)"
# til å evaluere polynomet fra oppgaveteksten gjennom sammenligning med det og det ekvivalente uttrykket
def test_feil(funk):
    c = np.ones(51)  # Koeffisienter for polynom: 1 + x + x^2 + ... + x^50
    x = 1.00001
    Px = (x ** 51 - 1) / (x - 1)  # Ekvivalent uttrykk for polynom fra oppgavetekst, evaluert i x=1.00001
    return round(abs(Px - funk(c, x)), 23) # Trenger ikke å runde av

print(test_feil(nest))