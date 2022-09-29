# Plotting the convolution of x(n) and h(n) by using a Toeplitz matrix
# y(n) = x(n) (*) h(n)



import numpy as np
import matplotlib.pyplot as plt
import scipy

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

vec_x = scipy.vectorize(x, otypes=[float])
N = np.linspace(0, 19, 20)
x_array = vec_x(N)
toeplitz_h = np.loadtxt('codes/toeplitz.dat', dtype='double')
y_array = np.dot(toeplitz_h, x_array)

plt.stem(N, y_array[:20])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.title('Filter Output using Convolution by Toeplitz Matrix')
plt.savefig('figs/5.5-toeplitz.png')
plt.show()