import numpy as np
import math

def cosTay(x):
    sum=0
    err=1
    n=0
    while err>0.000001:
        temp=x**(2*n) * (-1)**n / (math.factorial(2*n))
        sum+=temp
        n+=1
        err=np.absolute(temp/sum)
    return sum