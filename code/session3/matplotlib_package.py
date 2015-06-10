# -*- coding: utf-8 -*-

"""
    matplotlib_package.py - 3 Data Analysis
    
    The dominant plotting library in Python was constructed to 
    emulate the standard MATLAB plotting syntax and functionality,
    hence the name 'matplotlib'.  
    
    There are several ways to interface with matplotlib.  One can plot 
    interactively, which is useful for on the fly visualization.  One
    can subclass or wrap consistent and repetitive functionality 
    to customize plots. Plotting options can be defined on the local
    operating system, if desired.
    
    It is important to configure the plotting backend for your system,
    this is done in Spyder in the iPython settings->Graphics.  For this 
    module, inline plotting is recommended.
    
    Resources:  
        http://matplotlib.org/examples/pylab_examples/
        
"""

import os
import numpy as np

np.random.seed(12345)

plot_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'plots'))

SAVE_FIGS = False
N_FIG = 1
DEBUG = False

def more():
    global SAVE_FIGS, N_FIG, plot_dir, DEBUG
    if SAVE_FIGS:
        plot_name = os.path.join(plot_dir, "plot{}.png".format(N_FIG))
        plt.savefig(plot_name)
    N_FIG += 1
    plt.show()
    if not DEBUG:
        print
        raw_input("More...")
        print
        
"""
    Interactive Plotting
    
    By utilizing the matplotlib module pyplot, one easily has access
    to all the standard plotting and customization mechanisms
    
"""

from matplotlib import pyplot as plt
print
print "Plot 1"
time = np.linspace(0, 6 * np.pi)
data = 2 * np.sin(time) + 3 * np.cos(time)

plt.plot(time, data)
plt.title('A title')
plt.xlabel('Time')
plt.ylabel('Data')

plt.savefig(os.path.join(plot_dir, 'plot_example.png'))

"""
    Multiple series can be plotted at once, with the following 
    argument a flag for linestyle and colour.  
    
    Important to note that each plot is made up of a figure, 
    and axes, and plots.  if we keep plotting and changing 
    options, the same axes on the same figure will be modified
    in place.  
    
    Plots amend the current figure, use the 'figure' function 
    to start a new figure.  Alternatively, we can use
    the 'show' function to force the current figure to be
    rendered.
"""
more()

print
print 'Plot 2'
#plt.figure()
sin_data = np.sin(time)
cos_data = np.cos(time)

plt.plot(time, cos_data, '-b', time, sin_data, '*r')
plt.title('Sin/Cos')
plt.xlabel('Time')
plt.ylabel('Data')

plt.legend(['Cosine', 'Sine'])

"""
    Some more advanced figures include multiple axes on 
    one figure.  These are called 'subplots', and can be
    created and modified as follows.
"""


more()

print 
print "Plot 3"

ax = plt.subplot(2, 1, 1)  # 2 rows, 1 col, current plot 1
plt.plot(time, sin_data, "--k")
plt.title("Damped/Undamped Oscillator")
plt.ylabel("Sin")
plt.xlabel('Time')

damped_sin = np.sin(time) * np.exp(-time / 5)
plt.subplot(2, 1, 2)   # This go to the next subplot axes
plt.plot(time, damped_sin, '-g')
plt.ylabel("Damped Sin")
plt.xlabel("Time")

"""
    There are many other types of plots that are available
"""

more()

print
print "Plot 4"

hist_data = np.random.randn(2000)
plt.hist(hist_data, color="g", bins=50)
plt.title("Normally Distributed Data")

more()


"""
    With some careful manupulation, some advanced plottypes are
    also possible, such as a heatmap
"""
import matplotlib.mlab as mlab  # Matlab compatible names
import matplotlib.cm as cm  # Colour maps

print
print "Plot 5"
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = Z2 - Z1  # difference of Gaussians

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
                origin='lower', extent=[-3, 3, -3, 3],
                vmax=abs(Z).max(), vmin=-abs(Z).max())
plt.title("Heatmaps!")
plt.xlabel("X (mm)")
plt.ylabel("Y (mm)")
more()
