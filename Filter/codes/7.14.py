# Plotting the running times of FFT/IFFT and convolution


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

fft_times = np.loadtxt('codes/fft_times.dat', dtype=float)
conv_times = np.loadtxt('codes/conv_times.dat', dtype=float)
matrix_times = np.loadtxt('dftmat.dat', dtype=float)

:N = np.logspace(1,len(fft_times), num=len(fft_times), base=2)

fft_fit = optimize.curve_fit(lambda x,a : a*x*np.log(x), N, fft_times)[0]
conv_fit = optimize.curve_fit(lambda x,a : a*x*x, N, conv_times)[0]
matrix_fit = optimize.curve_fit(lambda x,a : a*x*x, N, matrix_times)[0]

plt.subplot(2, 1, 1)
plt.plot(N, fft_fit * N * np.log(N), label='$O(n \log n)$')
plt.plot(N, fft_times, 'o', label='FFT/IFFT')
plt.plot(N, conv_fit * N * N, label='$O(n^2)$')
plt.plot(N, conv_times, 'o', label='Convolution')
plt.xlabel('Size of input')
plt.ylabel('Running time')
plt.title('Comparison between running times of FFT/IFFT and Convolution')
plt.legend()
plt.grid()


plt.subplot(2, 1, 2)
plt.plot(N, matrix_fit * N * N, label='$O(n^2)$')
plt.plot(N, matrix_times, 'o', label='Matrix multiplication')
plt.xlabel('Size of input')
plt.ylabel('Running time')
plt.title('Running time of DFT matrix multiplication')
plt.legend()
plt.grid()
plt.savefig('figs/7.14.png')
plt.show()
