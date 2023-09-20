import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]

# Dempingen valgt bestemmer hvor symmetrisk polynomene blir
t = np.linspace(0, 20, 101)
t = np.linspace(0, 50, 101)
t = np.linspace(0, 10, 101)

sol = odeint(pend, y0, t, (b, c))
sol1 = sol[:, 0]
sol2 = sol[:, 1]

fig = plt.figure(0, (10, 6))

# Plot the results
plt.plot(t, sol1, label='Theta(t)')
plt.plot(t, sol2, label='Omega(t)')
plt.xlabel('Time (t)')
plt.ylabel('Solution')
plt.title('Pendulum Motion')
plt.legend()
plt.grid()
plt.show()