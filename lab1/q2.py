import numpy as np
P=800
r=0.15
L=50000
N=np.log(P/(P-r*L/12)/12*np.log(1+r/12))
print(N*12)