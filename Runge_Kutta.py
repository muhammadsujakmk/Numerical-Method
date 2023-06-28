import numpy as np
import matplotlib.pyplot as plt




def main():
    print('Runge Kutta has been created!')
    h = 1 # step 
    

def init_func(t,y):
    # Initial value problem
    k1 = dy
    y0 = 1

def RK4(dy,y0,t0,h,k1,k2,k3,k4):
    k1 = init_func(t0,y0)
    k2 = init_func(t0+h/2,y0+h*k1/2)
    k3 = init_func(t0+h/2,y0+h*k2/2)
    k4 = init_func(t0+h,y0+h*k3)

    yn = y0 + h*(k1+2*k2+2*k3+k4)
    return yn 



main()



