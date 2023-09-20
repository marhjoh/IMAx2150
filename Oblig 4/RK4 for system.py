import numpy as np
from numpy import *
def runge_kutta_system(f, y0, t0, t_end, h):
    num_steps=int((t_end-t0)/h)
    t=np.linspace(t0, t_end, num_steps+1)
    y=np.zeros((len(t), len(y0)))
    y[0]=y0
    for i in range (num_steps):
        k1=h*np.array(f(t[i], y[i]))
        k2=h*np.array(f(t[i] + 0.5*h, y[i]+0.5*k1))
        k3=h*np.array(f(t[i] + 0.5*h, y[i]+0.5*k2))
        k4=h*np.array(f(t[i] + h, y[i] + k3))
        y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6.0
    return t.tolist(), y.tolist()

def system_of_odes(t, y):
    dy1dt, dy2dt = y[1], -9.82*np.sin(y[0])
    return [dy1dt, dy2dt]

t0, t_end, h, y0 = 0.0, 0.5, 0.5, [1.0, 0.0]
t, y=runge_kutta_system(system_of_odes, y0, t0, t_end, h)
print(t)
print(y)
