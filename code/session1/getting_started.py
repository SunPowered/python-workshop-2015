"""
    This is a Python file for the starter workshop.

    Notice i can write anything I want here?  that's because it's a multi-line
        comment.
"""

# There are also single line comments

#
#   Except for the most basic of Python scripts, you usually need to import
#   other packages to provide any sort of meaningful functionality
#
#   BTW - This is another way to include multi-line comments

import sys
print sys.path

#
#  Basic Data Types
#

i = 2           # Integer

pi = 3.14159     # Float
two = 2.         # Also a float!

is_this_the_matrix = False  # Boolean

does_it_actually_matter = None  # Truthy...


#
# Mapping Types
#

first_name = "Jebidiah"  # A string

my_list_scores = [2.5, 3.5, 4.0, 3.5]  # A list

my_dict_scores = {"Mon": 2.5, "Wed": 3.5, "Fri": 4.0}  # A dictionary

my_set_scores = set(my_list_scores)

my_tuple_scores = tuple(my_list_scores)


#
#  Mapping operators
#

last_name = "Springfield"
full_name = first_name + " " + last_name  # String concatenation using *+*

extended_list = my_list_scores + ["Three", "Four"]  # List concatenation


#
#  Data Input / Output
#

print "My name is " + full_name  # A *print* statement with string concatenation

# Special string formatting can be used
print
print "Pi is a pretty special number.  It is {} to 5 decimal places".format(pi)
print "What is Pi to only 2 decimal places.  It's {:.2f}".format(pi)

print
middle_name = raw_input("What is your middle name: ")  # Simple user input
print "Your full name is: {} {} {}".format(first_name, middle_name, last_name)

raw_input("More...")


#
#  Type functions
#

# We can go back and forth between types via type functions, ex. *str*
string_pi = str(pi)
int_pi = int(pi)

# We can check types via the *type* function
print
print "Type before: {}.  Type after:{}".format(type(pi), type(string_pi))

# Something that ends up being useful: the *isinstance* function
print
print "Is 'int_f' an integer? : {}".format(isinstance(int_pi, int))
print "Is 'int_f' a float?: {}".format(isinstance(int_pi, float))

raw_input("More...")


#
# Math functions
#

# Unsurprisingly, we can use our computers to ... compute
radius = 2.0
circumference = 2 * pi * radius
print
print "Circumference: {}".format(circumference)
print "The radius was: {}".format(circumference / (2 * pi))

area = pi * radius**2
print "The area of the circle is: {}".format(area)
print

r2 = 7 + 3  # Wait, wasn't the plus used to concat strings together?  What happened?

#
#  Some trickery with the '/' operator
#

print "6/2.0 is a {}".format(type(6/2.0))
print "6/2 is a {}".format(type(6/2))
print "11/3 is a {}".format(type(11/3))
print "11/3 = {}".format(11/3)
print "11/3. = {}".format(11/3.)

raw_input("More...")
#
#  Let's play with some mapping functions
#
print
print "My list scores: {}".format(my_list_scores)
print "There are {} scores".format(len(my_list_scores))
print "The total scores is {}".format(sum(my_list_scores))
print "The second score is {}".format(my_list_scores[1])
print "The last score is {}".format(my_list_scores[-1])

raw_input("More...")

print
print "My dict scores: {}".format(my_dict_scores)
print "Monday's dict score: {}".format(my_dict_scores["Mon"])
print "Score keys: {}".format(my_dict_scores.keys())
print "Score values: {}".format(my_dict_scores.values())
print "The number of keys: {}".format(len(my_dict_scores))

raw_input("More...")

print
print "A set contains unique values of a list of the same type"
print "My unique scores are: {}".format(my_set_scores)
#
# Sets do not support indexing, try 'my_set_scores[2]'
#

#
# Check out the difference between tuples and lists
#

#
# Explore string functions, lower(), upper(), find()
#