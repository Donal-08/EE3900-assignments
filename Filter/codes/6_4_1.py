# Plotting y(n) by fast Fourier transform



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

x_vec = scipy.vectorize(x, otypes=[float])
h_vec = scipy.vectorize(h, otypes=[float])

n_arr = np.linspace(0, N-1, N)
x_arr = x_vec(n_arr)
h_arr = h_vec(n_arr)

X_arr = np.fft.fft(x_arr)
H_arr = np.fft.fft(h_arr)
Y_arr = X_arr * H_arr
y_arr = np.fft.ifft(Y_arr)
y_diff=np.loadtxt('codes/y.txt', dtype='double')
y_idft = np.loadtxt('idft.txt', dtype='double')


plt.stem(range(0,N), y_diff, linefmt="-.",markerfmt="bo",label="Using Difference eq")
plt.stem(range(0,N), y_idft, linefmt=":",markerfmt="ro", label="using DFT")
plt.stem(n_arr, np.real(y_arr), linefmt="--",markerfmt="go", label="using FFT")
plt.title('Filter Output using FFT')
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.grid()
plt.legend()
plt.savefig('figs/6.4.png')
plt.show()
