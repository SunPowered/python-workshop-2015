# -*- coding: utf-8 -*-
"""
    functions.py - Getting Started - Functions

    This file describes Python functions and the use of arguments and 
    keyword arguments.  It also demonstrates the use of whitespace to 
    group code under defined functions.
"""

#
# Functions are defined via the 'def' statement
#

def fooa(arg1, arg2):
    """
        The function 'foo' takes two required arguments returning the sum
    """
    return arg1 + arg2

def foob(*args):
    """
        The function 'foob' takes a variable number of arguments
        passed to the tuple 'args' and returns the average of them
    """
    n_args = len(args)
    return sum(args) / n_args

def fooc(arg1, kw1=1, kw2=2, kw3=None):
    """
        The function 'fooc' takes one argument, and three
        keyword arguments.  It returns the sum of them all.
    """

    if kw3 is None:
        return kw1 + kw2 + arg1
    else:
        return kw1 + kw2 + kw3 + arg1

def food(**kwargs):
    """
        This function takes any number of keyword arguments and prints
        the kwarg keys and values
    """
    return kwargs.keys(), kwargs.values()

def fooe(*args, **kwargs):
    """
        This function prints the number of each arguments and keyword arguments 
        to the console.
    """
    #
    # Notice we don't have to return anything if we don't want to
    #
    print "You have passed {} arguments and {} keyword arguments".format(
        len(args), len(kwargs))
    print "The first argument is {}".format(args[0])

"""
    Let's try using some of these functions to see what happens
"""

# r1 = fooa(1, 2)

# r2 = foob(1, 2, 3)

# r3 = fooc(4)

# r4 = fooc(4, kw1=2)

# r5 = fooc(4, kw1=2, kw3=4)

# r6 = food(kw1="Hello", kw2="World", kw3=3.14)

# r7 = fooe(1, 2, 3, kw1="One", kw2="Two")

"""
    Functions are objects too!
"""

def run_a_func(func, *args, **kwargs):
    """
        This function is a little redundant, it takes a function, 
        some arguments and some keyword arguments and runs it
    """
    print
    print "I am about to run function '{}'".format(func.__name__)
    print "I will use arguments: {} and kwargs: {}".format(args, kwargs)
    print "Function docstring: {}".format(func.__doc__)
    ret = func(*args, **kwargs)
    print "The returned value is: {}".format(ret)

"""
    Let's compare the output to before, passing our functions as
    regular variables to our new function
"""

# run_a_func(fooa, 1, 2)

# run_a_func(foob, 1, 2, 3)\

# run_a_func(fooc, 4)

# run_a_func(fooc, 4, kw1=2)

# run_a_func(fooc, 4, kw1=2, kw2=4)

# run_a_func(food, kw1="Hello", kw2="World", kw3=3.14)

# run_a_func(fooe, 1, 2, 3)
