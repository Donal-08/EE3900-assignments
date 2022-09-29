# Plotting 8-point FFT


import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt('codes/fft.dat', dtype=float)
plt.stem(X)
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('$8$-point FFT')
plt.grid()
plt.savefig('figs/7.13.png')
plt.show()
