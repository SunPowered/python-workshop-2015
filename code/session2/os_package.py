# -*- coding: utf-8 -*-

""" 
    os_package.py - Advanced Topics 2.  This file describes a useful built-in library, the 'os' module.  
    This involves all operating system level functions and very useful file path manipulations.
"""

# By default, very few modules are included in the interpreter
#   we must import them as we need them

import os

""" 
    The purpose of the os module is to abstract away the differences that various operating 
    systems handle themselves, such as file paths, working with directories, etc.  
    
    From the docs: 
        Programs that import and use ‘os’ stand a better chance of being portable between 
        different platforms. Of course, they must then only use functions that are defined 
        by all platforms (e.g., unlink and opendir), and leave all pathname manipulation 
        to os.path (e.g., split and join).
"""

# Some simple properties of each operating system that are generally useful
print 
print "The current operating system is: {}".format(os.name)
print "The current operating system uses '{}' as a path separator".format(os.sep)
print "The current working directory is: {}".format(os.getcwd())

# There are many other os specific attributes
#   Such as:  os.curdir, os.pathsep, etc

#raw_input("More...")
print

"""
    The most common use of the os library is to work with filenames and paths
"""

"""
    Path names can be constructed and modified via the 'os.path' module
"""

cwd = os.getcwd()
print "The basename of the cwd: {}".format(os.path.basename(cwd))
print "The dirname of the cwd: {}".format(os.path.dirname(cwd))

"""
    The os.path.split and os.path.join functions can be useful for more avanced path manipulation
"""
print "Joining paths 'a', 'b', and 'c': {}".format(os.path.join('a', 'b', 'c'))
print "Splitting the cwd: {}".format(os.path.split(cwd))

"""
    Paths can be checked whether they are files or directories in the filesystem
"""

print "Is the cwd a directory? {}".format(os.path.isdir(cwd))
print "How about a file? {}".format(os.path.isfile(cwd))

"""
    Filenames can be specifically manipulated
"""

foo_txt = os.path.join(os.pardir, 'data', 'foo.txt')  # os.pardir is the parent directory
print "foo.txt path: {}".format(foo_txt)
print "Is foo.txt a file? {}".format(os.path.isfile(foo_txt))
print "Does foo.txt exist? {}".format(os.path.exists(foo_txt))
print "foo.txt path split: {}".format(os.path.split(foo_txt))
print "foo.txt extension split: {}".format(os.path.splitext(foo_txt))
print "The full absolute path: {}".format(os.path.abspath(foo_txt))

#raw_input("More...")
print

"""
    The os module can also be used to make directories on the file system, using 
    os.mkdir() and os.makedirs(), which can come in handy for large sets of data processing.
    Alternatively, one can remove directories using os.rmdir() and os.removedirs().  More effective
    directory operations, namely intelligent removal, are available with the 'shutil' module.
"""

data_dir = os.path.join(os.pardir, 'data')
new_dir = os.path.join(data_dir, 'new_dir')
new_dirs = os.path.join(data_dir, 'new_dirs')
deep_dirs = os.path.join(new_dirs, 'deep_dir1', 'deep_dirs2')

if os.path.isdir(new_dir):
    print "Removing new_dir: {}".format(new_dir)
    os.rmdir(new_dir)

print "Making new_dir: {}".format(new_dir)
#os.mkdir(new_dir)
print

if os.path.isdir(new_dirs):
    import shutil
    print "Removing nested directories beginning at: {}".format(new_dirs)
    shutil.rmtree(new_dirs)
    
print "Making deep_dirs: {}".format(deep_dirs)
#os.makedirs(deep_dirs)


