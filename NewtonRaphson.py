import numpy as np
import matplotlib.pyplot as plt

def main():
    xn = 5
    err = 0.01
    maxit = 100
    NewtonRaphson(xn,err,maxit)


def NewtonRaphson(xn,err=0.0001,maxit=50):
    t=0 
    while True:
        x0=xn
        f,df = func(xn) 
        xn -= f/df
        t +=1
        if abs(xn-x0) < err:
            print(f'root is= {xn}')
            break

def func(x):
    f = x**2-2*x
    df = 2*x-x
    return f,df 

main()
