# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:29:42 2018

@author: Richard Thurston
A script to plot the line graph form of a function only works for monotonic 
functions, functions with multiple solutions are hard for sympy to solve nicely
"""
YMIN = -20
YMAX = 20
XMIN = -15
XMAX = 15
NUMB_LINES = 20
SLOPE_MIN = -4
SLOPE_MAX = 4

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_results(x, y):
    plt.plot(x, y)
    plt.ylim(YMIN, YMAX)
    plt.show()

def main():
    # Make symbolic expression and compute legendre transform
    x, p = sp.symbols("x p")
    y = (1/10)*x**2 # Modify this line to plot your own function
    y_prime = sp.diff(y, x)
    x_to_p_substitution = sp.solve(y_prime - p, x, dict=True)
    phi = y - x*y_prime
    phi = phi.subs(*x_to_p_substitution)
    
    # make python function from base point function
    f = sp.lambdify(x, y)
    
    # make python function for generating linear functions based on the transform
    y_0 = sp.lambdify(p, phi)
    def make_line_funct(m):
        return lambda x: m*x + y_0(m)
    
    # set up np arrays for x and y axis
    y_axis = []
    x_axis = np.linspace(XMIN, XMAX, 1000)
    slopes = np.linspace(SLOPE_MIN, SLOPE_MAX, NUMB_LINES)
    for slope in slopes:
        line = make_line_funct(slope)
        y_axis.append(line(x_axis))
        
    # plot
    plot_results(x_axis, f(x_axis)) # plot the point geometric representation
    plot_results(x_axis, np.array(y_axis).T) # plot the line geometric representation
    y_axis.append(f(x_axis))
    plot_results(x_axis, np.array(y_axis).T) # plot both representations

if __name__ == "__main__":
    main()