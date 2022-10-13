from turtle import color
import numpy as np
from matplotlib import pyplot as plt

def unitstep(t):
    if (t < 0): return 0
    elif (t == 0):return 0.5
    else: return 1

# def v1(t):
#     if (t >= 0): return 2/3*(1 + np.exp(-t*1.5e6))*unitstep(t)
#     else: return 0

def v1(t):
    if t < 0:
        return 0
    else:
        return (2/3) * (1 + np.exp(-1.5e6 * t))

vc0 = np.vectorize(v1, otypes=['double'])
vc1 = np.loadtxt('v2.txt')
t = np.linspace(0, 1e-5, 1000000)
plt.plot(t, vc0(t))
plt.plot(vc1[:,0], vc1[:,1], '.', color="red")
plt.xlabel('t (s)')
plt.ylabel('$v_{C_0}(t)$ (V)')
plt.grid()
plt.legend(['Analysis', 'Simulation using ngspice'])
plt.savefig('../figs/3.4.png')
plt.show()
