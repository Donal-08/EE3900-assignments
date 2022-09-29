import imp
import numpy as np
import cmath
import math
from scipy import linalg
import matplotlib.pyplot as plt


# x(n) - the input signal given
x = np.array([1,2,3,4,2,1])

# Create the dft matrix
r = 0.5
i = -math.sqrt(3)/2
W_6 = complex(r,i)

F = np.ndarray((6,6), dtype=np.complex128)
# print(F)

for i in range(6):
    for j in range(6):
        power = i*j
        F[i][j] = pow(W_6, power)

# COmputing X = Fx

X = np.matmul(F,x)
print(X)

############    USING PREDEFINED DFT:   ###############


F_6 = linalg.dft(len(x))
X_6 = np.matmul(F_6, x)

plt.stem(np.real(X_6))
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('DFT using DFT Matrix')
plt.grid()
plt.savefig('figs/7.11.png')
plt.show()

