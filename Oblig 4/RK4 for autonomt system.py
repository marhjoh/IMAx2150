import numpy as np
def RK4OnAutSyst(F, Yinit, h, n):
    m = Yinit.size
    W = np.zeros([m, n+1])
    W[:,0] = Yinit
    for i in range (0,n):
        s1=F(W[:,i])
        s2=F(W[:,i]+(h/2)*s1)
        s3=F(W[:,i]+(h/2)*s2)
        s4=F(W[:,i]+h*s3)
        W[:,i+1]=W[:,i]+h*(s1+2*s2+2*s3+s4)/6
    return W

