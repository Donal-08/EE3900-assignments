import numpy as np
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

N = 14
n = np.arange(N)
print(n)
fn=(-1/2)**n
print(fn)

un1=np.pad(fn, (0,2), 'constant', constant_values=(0))
un2=np.pad(fn, (2,0), 'constant', constant_values=(0))
print(un1)
print(un2)
h = un1+un2
print(h)

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])  # x_n in question
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
print(X)

for k in range(0,N):
    for n in range(0,N):
        X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)

    print(X[k])

print(X)