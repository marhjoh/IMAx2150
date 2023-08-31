n = 5000
time_backsubstitution = n**2 * 0.005
time_gauss_elimination = (2/3) * n**3 * 0.005
total_time = time_backsubstitution + time_gauss_elimination

# Konverter total_time til nærmeste hele sekund
total_time_seconds = round(total_time)

print(f"Total tid for å løse likningssystemet: {total_time_seconds} sekunder")
