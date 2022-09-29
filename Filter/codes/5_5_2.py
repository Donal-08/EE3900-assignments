# Plotting the convolution of x(n) and h(n)
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

def y(n):
    return x(0)*h(n) + x(1)*h(n-1) + x(2)*h(n-2) + x(3)*h(n-3) + x(4)*h(n-4) + x(5)*h(n-5)

vec_y = scipy.vectorize(y, otypes=[float])

N = np.linspace(0, 19, 20)
plt.stem(N, vec_y(N))
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.title('Filter Output using Convolution')
plt.savefig('figs/5.5.png')
plt.show()