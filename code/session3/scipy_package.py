# -*- coding: utf-8 -*-

"""
    scipy_package.py - 3 Data Analysis - scipy routines
    
    Many useful scientific algorithms and routines are provided
    in the scipy module.  Some of these modules are:
    
        integration
        linear algebra
        fast fourier transforms
        interpolation
        signal processing
    
    Some examples of these will be provided here
"""

DEBUG = False

def more():
    global DEBUG
    print
    if not DEBUG:
        raw_input("More...")
    print
    
import numpy as np
import scipy.linalg as linalg

"""
    Some linear algebra
"""

A = np.array([[2, 1], [3, 4]])
print
print "Linear Algebra"
print "A:"
print A
print "det(A): ", linalg.det(A)
print "inv(A):"
print linalg.inv(A)

more()

print """Solving a linear system of equations:
x+3y+5z = 10
2x+5y+z = 8
2x+3y+8z = 3
"""
B = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
c = np.array([10, 8, 3])
print "B:"
print B
print "c: ", c
s = linalg.solve(B, c)
print "Solution, s[x,y,z] = ", s 

more()

"""
    Fast Fourier Transforms
"""

from scipy.fftpack import fft, ifft, fftshift, fftfreq
from matplotlib import pyplot as plt

noise = 1
N = 1000
T = 0.05
x = np.linspace(0.0, N * T, N)

y1 = 3 * np.sin(2.0 * 2 * np.pi * x)
y2 = 0.5 * np.cos(6.5 * 2 * np.pi * x)
y3 = np.sin(4.0 * 2 * np.pi * x) 

y = y1 + y2 + y3 + noise * np.random.randn(len(x))

plt.plot(x, y)
plt.title("Real Function")
plt.show()

y_f = fft(y)

"""
    This returns both positive and negative frequency terms,
    as per the definition of FFT, must take the subset of result 
    that we need
"""

x_f = fftfreq(N, T)
x_f_disp = fftshift(x_f)
y_f_disp = fftshift(y_f)
plt.plot(x_f_disp, 1.0 / N * np.abs(y_f_disp))
plt.title("FFT")
plt.show()

"""
 Try to reconstruct the original function via the inverse
 fourier transform
"""

y_orig = ifft(y_f)
plt.plot(x, y_orig)
plt.title("Inverse FFT")
plt.show()
