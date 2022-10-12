import numpy as np
import matplotlib.pyplot as plt

N = np.linspace(-40,40,21)
x = np.exp((1j*3*np.pi*N)/4)

plt.stem(N,x)
plt.title('$x[n] = e^{j(3\pi n/4)}$')
plt.savefig('donal.png')
plt.show()
