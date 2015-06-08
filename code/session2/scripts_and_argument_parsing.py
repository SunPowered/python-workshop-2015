#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    scripts_and_argument_parsing.py - Advanced Topics 4 - Creating scripts that parse arguments.
    
    If you find yourself doing similar work repeatedly with slight variations, 
    it becomes very useful to make a script that can do this for you.  
"""
import argparse


def main(options):
    """
        Though not required, it is useful to wrap the option handling in a function.    
    """
    if options.verbose:
        print "Verbosity of level: {}".format(options.verbose)
        
    if options.count:
        print "There are a total of {} system arguments".format(len(options.args))
        
    if options.duplicate:
        print "Printing duplicates of script arguments"
        for arg in options.args:
            print arg, arg
    
    
if __name__ == "__main__":
    """
        This odd little statement isolates code to run only when the file is run itself
        rather than being imported in another script.
    """
    
    """
        Next we define the argument parser, for when you want to pass options
        or flags to your script from the command line.  
        
        Useful arguments to ArgumentParser.add_argument():
        
            dest:  The destination variable to save the argument result
            action: Defines what should be done when this argument is encountered
            help: The help message to display for this argument
            nargs: The number of parameters to expect for this argument
    """
    parser = argparse.ArgumentParser(prog="Program Script")    
    parser.add_argument('-c', '--count', dest="count", action="store_true",
                        help="Count and return the number of arguments")
    parser.add_argument('-d', '--duplicate', action="store_true",
                        help="Duplicate the ordered parameters passed to the script")
    parser.add_argument('-v', dest="verbose", action="count",
                        help="Increase verbosity levels up to max of 3")
    parser.add_argument('args', nargs='*', 
                        help="Script Arguments")
    """
        Now we have defined what arguments the script takes, parse the arguments provided
        this defaults to sys.argv.  This returns a Namespace object, which is a simple object
        with the arguments as attributes
    """
    options = parser.parse_args()  
    
    """
        Now do whatever the script needs to do
    """
    print options
    main(options)