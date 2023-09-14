import numpy as np

def euler(f, y_init, start, stop, h):
   n = int((stop-start)/h)+1
   t = np.arange(start, stop, h)
   y = np.zeros([n, y_init.size])
   y[0,:] = y_init

   for i in range(n-1):
      y[i+1,:] = y[i,:]+h*f(y[i,:])

   return t,y

f = lambda y: np.array([y[0]+3*y[1], 2*y[0]+2*y[1]])
y_exact = lambda t: np.array([3*np.exp(-t)+2*np.exp(4*t),-2*np.exp(-t)+2*np.exp(4*t)])
y_init = np.array([5, 0])
t,y = euler(f, y_init, 0, 1, 0.25)

print(y)