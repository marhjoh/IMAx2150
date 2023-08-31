def halvering_solve(f, a, b, tol):
    while(b-a) > tol:
        mid = round((a + b) / 2, 6)  # Beregn midtpunktet med seks desimaler presisjon
        if f(mid) == 0:
            return 0
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

    # Definer funksjonen f(x) = x^3 - 9


f = lambda x: x ** 3 - 9
maks_feil = 1e-6  # Maksimal feil for å finne roten med minst 6 desimaler
a = 2.0
b = 3.0
x_sol = halvering_solve(f, a, b, maks_feil)  # Startintervallet er [a, b]
print(x_sol)  # Skriv ut tilnærmingen til roten av funksjonen