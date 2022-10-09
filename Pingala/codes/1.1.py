import numpy as np

n = 100
roots = np.roots([1,-1,-1])     #  [1,-1,-1] => np.roots() will return the roots of x^2-x-1 = 0 
alpha = roots[0]
beta = roots[1]

k = np.linspace(1, n, n)       # return evenly spaced numbers over 1 to 100 i.e. array
a = (alpha**k - beta**k)/(alpha - beta)    # a is also an array

ca = np.cumsum(a)                                         # ca is an array of cumulative sums of a[0], a[1], a[2] and so on i.e ca[1] = ca[0] + a[1]  
if (np.allclose(ca[:98], a[2:] - 1)): print("1.1 correct")    # Returns True if two arrays are element-wise equal within a tolerance.

else: print("1.1 incorrect")
