# Gitt data
tid_2000x2000_system = 0.1  # sekunder
n = 100 #antall systemer
størrelse_8000x8000 = 8000

# Estimer tid per 8000x8000 system
forhold = (størrelse_8000x8000 ** 2) / (2000 ** 2)
tid_8000x8000_system = tid_2000x2000_system / forhold

# Total tid for 100 systemer
total_tid = ((tid_8000x8000_system * n)/tid_2000x2000_system)

print((n*tid_2000x2000_system)/forhold)
print(f"Estimert tid for å løse 100 ligningssystemer av størrelse 8000x8000 er: {total_tid:.0f} sekunder")

equations = n**2
time = 5e-3
time_gauss_elimination = (2 * n**3 / 3)
total_time = (time_gauss_elimination/equations) * time