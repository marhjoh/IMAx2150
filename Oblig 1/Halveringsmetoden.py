import numpy as np

def bisection(f, a, b, eps):
    it = 0
    nr = 0 #maximum iterations allowed
    #if f(a) * f(b) > 0:
    if np.sign(f(a))*np.sign(f(b)) > 0:
        return " "
    while (b-a)/2 > eps:
        mid = (a+b)/2
        if f(mid) == 0:
            break
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
            if it < nr:
                pass
            else:
                return mid
            it += 1
            return mid