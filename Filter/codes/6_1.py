import numpy as np
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

N = 14
n = np.arange(N)   #[ 0  1  2  .... 13]
fn=(-1/2)**n        # (-1/2)^n u(n) [u(n)=1]

# hn1 = (-1/2)^n u(n)   hn2 = (-1/2)^n u(n-2)
# n = 0 to 13 
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0)) 
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])  # x_n in question
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))

# Generating X(k)

X = np.zeros(N) + 1j*np.zeros(N)




for k in range(0,N):
    for n in range(0,N):
        X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)
    
    
np.savetxt("x_data.txt", X.view(float).reshape(-1, 2))

# Generating H(k)

H = np.zeros(N) + 1j*np.zeros(N)

for k in range(0,N):
    for n in range(0,N):
        H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)


np.savetxt("h_data.txt", H.view(float).reshape(-1, 2))
