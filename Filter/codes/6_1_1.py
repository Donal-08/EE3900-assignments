# Plotting the discrete Fourier transforms of x(n) and h(n)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 20

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def h(n):
    if n == 0:
        return 1
    elif n > 0:
        return delta(n) + delta(n-2) - 0.5*h(n-1)
    else:
        return 2*(delta(n+1) + delta(n-1) - h(n+1))

def DFT(k, fun):
    ksum = 0
    for n in range(N):
        ksum += fun(n) * np.exp(-2j * np.pi * k * n / N)
    return ksum

K = np.linspace(0, N-1, N)
plt.subplot(2, 1, 1)
plt.stem(K, np.real(DFT(K, x)))
plt.ylabel('$X(k)$')
plt.title('Discrete Fourier Transform')
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(K, np.real(DFT(K, h)))
plt.ylabel('$H(k)$')
plt.xlabel('$k$')
plt.grid()

plt.savefig('figs/6.1.png')
plt.show()
