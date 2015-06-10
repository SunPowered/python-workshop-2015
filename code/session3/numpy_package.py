"""
    numpy_package.py - 3 Data Analysis

    The numpy array.  At its core, the numpy.ndarray is a
    multidimensional array.  It's main elements are usually
    numbers.  It is much more flexible and memory efficient
    than traditional Python lists.
    
    Extra Resources:
        http://docs.scipy.org/doc/numpy/reference/
        http://www.engr.ucsb.edu/~shell/che210d/numpy.pdf
    
    Some useful ndarray attributes:
        ndarray.ndim - Number of axes (dimensions)
        ndarray.shape - The exact dimensions or shape of the array
        ndarray.size - The total number of elements of the array
        ndarray.dtype - The type of elements in the array
"""
import numpy

arr = numpy.arange(15)
print
print "A simple numpy array:"
print arr
arr = arr.reshape(3, 5)  # Repartition the dimensions of the array
print "Reshaped to be 3x5"
print arr
print "size: ", arr.size
print "ndim: ", arr.ndim
print "shape: ", arr.shape
print "dtype: ", arr.dtype

"""
    Arrays are created via the numpy.array function, which takes
    a list as its main argument and some optional keyword arguments
"""

print "An array of ints"
arr = numpy.array([1, 2, 3, 4])
print arr
print "dtype: ", arr.dtype
print
print "An array of floats"
arr = numpy.array([1.2, 2.3, 3.4, 4.5])
print arr
print "dtype: ", arr.dtype

"""
    Often, the array size is known, but the values are not.  
    Extending the array size on the fly is expensive, so it
    is useful to create an array of ones or zeros.    
"""

arr = numpy.zeros((3, 5))  # Notice the shape is a tuple
print "An array of zeros"
print arr
arr = numpy.ones((3, 5), dtype=complex)
print "An array of complex ones"
print arr
print "dtype: ", arr.dtype

"""
    Arithmetic Operations.  
    
    Arrays support basic arithmetic operations, which are 
    applied elementwise, in contrast to standard lists
"""
a = numpy.array([1, 2, 3, 4, 5])
print a
print "a * 5: ", a * 5
print "a**2: ", a ** 2
print
b = numpy.array([10, 20, 30, 40, 50])
print "b: ", b
print "b - a: ", b - a
print
print "sin(a): ", numpy.sin(a)
print "b<37: ", b < 37

"""
    The matrix dot product is produced by the 'dot' function, 
    the '*' operator still applies elementwise
"""

A = numpy.array([[2, 1],
                 [1, 2]])
B = numpy.array([[1, 0],
                 [2, 1]])
print                
print "A: "
print A
print "B: "
print B
print "A * B: "
print A * B
print "dot(A, B): "
print numpy.dot(A, B)

"""
    Similar to Python lists, indexing and slicing can be 
    performed though with numpy, we have more than one 
    dimension to index.  We can also assign extended slices
    itemwise.
"""

print "a: ", a
print "a[1]: ", a[1]
print "a[1:5]: ", a[1:5]
print "a[1:5:2]", a[1:5:2]
a[1:5:2] = -10
print "assigned extended slice: ", a
print
C = numpy.array([[1, 2, 3, 4], [4, 5, 6, 7], [6, 7, 8, 9]])
print "C:"
print C
print "multidimensional slice C[:, 2:] "
print C[:, 2:] 

"""
    Can also index by an array of indices, or booleans
"""
print
print "Indexing by another array"
print "a: ", a
idx = numpy.array([1, 3, 4])
print "idx: ", idx
print "a[idx]: ", a[idx]
print "a[a<-5]: ", a[a < -5]

""" 
    Iterating over an array iterates over the first dimension
"""
print "Iterating over C"
for row in C:
    print row

print
print "Iterating elementwise over C"
for element in C.flat:
    print element
    
"""
    Random numbers
    
    Simulations often require the generation of random numbers.  Numpy
    includes a random number generation module for arrays
"""

numpy.random.seed(12345)  # Important for reproducibility

d = 10 * numpy.random.random((2, 3))
print
print "Random array, d - (2x3)"
print d

"""
    Statistics
    
    Numpy arrays have the ability to compute simple statistics
    on themselves.  Methods such as 'sum', 'max', 'min', 'mean', 
    'std', 'var'
"""

print
print "Statistics on d"
print "d.sum(): ", d.sum()
print "d.mean(): ", d.mean()
print "d.std(): ", d.std()

"""
    Furthermore there are also useful methods that can locate
    interesting values returning indices, argmax, argmin, argsort
"""

time = numpy.linspace(0, 100)
data = numpy.sin(3 * time) - 2 * numpy.cos(time)
noise = 10 * numpy.random.random((1, 10))

print
print "Max data: ", data.max()
print "Min data: :", data.min()
max_idx = data.argmax()
min_idx = data.argmin()
print "Time at max data: ", time[max_idx]
print "Time at min data: ", time[min_idx]

print 
print "noise: ", noise
print "sorted noise indices: ", noise.argsort()

