# Plotting y(n) from the inverse discrete Fourier transform of Y(k)


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

def Y(k):
    return DFT(k, x) * DFT(k, h)

def IDFT(n, fun):
    nsum = 0
    for k in range(N):
        nsum += fun(k) * np.exp(2j * np.pi * k * n / N)
    return nsum / N


file = open("idft.txt", "w")


y_diff=np.loadtxt('codes/y.txt', dtype='double')


nvalues = np.linspace(0, N-1, N)
np.savetxt(file, np.real(IDFT(nvalues, Y)))

# file.write(np.real(IDFT(nvalues, Y)))
plt.stem(range(0,N),y_diff, linefmt=":",markerfmt="bo",label="Using Difference eq") 
plt.stem(nvalues, np.real(IDFT(nvalues, Y)), linefmt="--",markerfmt="go", label="using DFT")
plt.title('Filter Output using DFT')
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.legend()
plt.grid()
plt.savefig('figs/6.3.png')
file.close()
plt.show()

