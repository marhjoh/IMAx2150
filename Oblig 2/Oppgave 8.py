n = 5000
equations = n**2
time = 5e-3
time_gauss_elimination = (2 * n**3 / 3)
total_time = (time_gauss_elimination/equations) * time

# Konverter total_time til nærmeste hele sekund
total_time_seconds = round(total_time)

print(f"Total tid for å løse likningssystemet: {total_time_seconds} sekunder")