import numpy as np
import matplotlib.pyplot as plt


def main():
    X = [] 
    Y = []
    h = 0.1 # step 
    N = 100
    x = 0
    y = 1
    
    for i in range(N):
        y +=RK4(x,y,h)
        x += h
        X.append(x)
        Y.append(y)
    
    ## Exact cosine function 
    y1 = np.cos(np.array(X))
    Plot(X,Y,y1)

def init_func(t,y):
    return -np.sin(t)

def RK4(t0,y0,h):
    k1 = init_func(t0,y0)
    k2 = init_func(t0+h/2,y0+h*k1/2)
    k3 = init_func(t0+h/2,y0+h*k2/2)
    k4 = init_func(t0+h,y0+h*k3)
    return h*(k1+2*k2+2*k3+k4)/6

def Plot(x,y,y1):
    plt.plot(x,y1,"*",label="$y=cos(x)$")
    plt.plot(x,y,label="Runge Kutta 4th Order")
    plt.xlabel("x-axis",fontsize=10)
    plt.ylabel("y-axis",fontsize=10)
    plt.legend(loc="best") 
    plt.show()


main()



