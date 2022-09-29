# Computing the DFT using the FFT algoritthm

import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1], dtype=float)
x_padded =  np.pad(x, (0, 2) , 'constant', constant_values = (0))

# print(x_padded)

# Fast Fourier transform
y = fft(x_padded)
print(y)

plt.stem(np.real(y))
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('FFT after zero padding $\mathbf{x}$')
plt.grid()
plt.savefig('figs/7.12.png')
plt.show()