import math

# Parametere
h = 10  # Kjeglehøyde i cm
V = 60  # Volum av iskrem i cm³

# Funksjon for å beregne f(r)
def f(r):
    return (1/3) * math.pi * r**2 * h + (2/3) * math.pi * r**3 - V

# Derivert av f(r)
def f_prime(r):
    return (2/3) * math.pi * r * h + 2 * math.pi * r**2

# Newtons metode
def newtons_method(guess, tolerance):
    r = guess
    while abs(f(r)) > tolerance:
        r = r - f(r) / f_prime(r)
    return r

# Start med et kvalifisert gjett for radius (f.eks. halvparten av kjeglen)
initial_guess = h / 2
tolerance = 1e-4  # Ønsket nøyaktighet

# Kjør Newtons metode og få estimert radius
radius = newtons_method(initial_guess, tolerance)

# Skriv ut estimert radius med 4 desimalers nøyaktighet
print(f"Estimert radius for halvkulen: {radius:.4f} cm")
