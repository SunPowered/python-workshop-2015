# -*- coding: utf-8 -*-
"""
    operators.py - Getting Started - Operators
    
    Operators are inherent functions that can act on 
    many types of Python objects.  These take common
    mathematical forms '+, - *, /', etc.  
    
    The interesting part of Python's lack of type 
    definition leads to a certain flexibility in code
    using operators.
"""

#
#  Arithmetic Operators
#

"""
    The '+' operator acts on simple numerics the way we expect
"""

int_add = 3 + 2
print "num_add: {}".format(int_add)

float_add = 3.14 + 2.56
print "float_add: {}".format(float_add)

"""
    When applied to strings and lists, the result changes
"""

list_add = [1, 2, 3] + [4, 5, 6]
print "list_add: {}".format(list_add)

string_add = "Hello, " + "World"
print "string_add: {}".format(string_add)

"""
    Not all mapping types support the '+' operand.  Try 
    using it on a pair of dict or set objects.  Throws a 'TypeError'
"""

raw_input("More...")

"""
   Similarly to the '+' operator, the '*' operator can act on numerics
   and some mappings
"""

print
num_mult = 3.2 * 3
print "num_mult: {}".format(num_mult)

list_mult = [1, 2] * 3  # notice what we are doing here?
print "list_mult: {}".format(list_mult)

string_mult = "-" * 20
print "string_mult: {}".format(string_mult)

raw_input("More...")

""" 
    A little less interesting are the numeric operators, 
    
    '/' (division)
    '%' (modulo)
    '**' (power)
    '//' (floor)
"""

print 
num_div = 23 / 10  # Should be 2
print "num_div: {}".format(num_div)

float_div = 23 / 10.
print "float_div: {}".format(float_div)

"""
    Modulo is the remainder after integer division
"""

num_modulo = 23 % 10  # Should be 3
print "num_modulo: {}".format(num_modulo)

num_power = 2 ** 3
print "num_power: {}".format(num_power)

float_floor = 23 // 10.0 
print "float_floor: {}".format(float_floor)

raw_input("More...")

#
#  Comparison Operators
#

"""
    Comparison operators return boolean objects, which are useful in some
    comtrol statements.  These are mostly similar to common math comparisons
"""

print
is_equal = 20 == 20
print "is_equal: {}".format(is_equal)

is_not_equal = 30 != 20
print "is_not_equal: {}".format(is_not_equal)

is_greater = 20 > 30
print "is_greater: {}".format(is_greater)

# Same with '<'  less than

is_greater_or_equal = 30 >= 30
print "is_greater_or_equal: {}".format(is_greater_or_equal)

# Same with '<='  less than or equal


raw_input("More...")


#
#  Assignment operators
#

""" 
    These are useful pieces of 'syntactic sugar' that are not necessarily required,
    but often save much time and typing.  
"""

"""
    We have seen many examples of the simple assignment operator '=', 
    hopefully no further examples are needed
"""
print 

a = 5
a += 3  # ADD and Assignment operator
print "a: {}".format(a)

b = 5
b -= 3  # SUBTRACT and Assignment operator
print "b: {}".format(b)

"""
    The {operator} AND assignment works for all numeric operators
"""

c = 10
c -= 2
print "c: {}".format(c)

d = 5
d *= 3
print "d: {}".format(d)

e = 15
e /= 5
print "e: {}".format(e)

raw_input("More...")

#
#  Logical Operators
#

"""
    These operators come in handy very often when used with control flow statements.
    They are also very similar to other standard programming languages, with some
    added functionality due to Python's type agnostic format.
"""

print
a_bool = True
b_bool = False

c_bool = a_bool and b_bool  # Should be False
print "c_bool: {}".format(c_bool)

d_bool = a_bool or b_bool  # Should be True
print "d_bool: {}".format(d_bool)  

e_bool = not a_bool  # Should be False
print "e_bool: {}".format(e_bool)

"""
    Interesting that the Logical Operators accept non Boolean arguments
"""
print

print "3 or 5: {}".format(3 or 5)
print "3 and 5: {}".format(3 and 5)
print "None or 3: {}".format(None or 3)
print "3 or None: {}".format(3 or None)
print "None and 5: {}".format(None and 5)

raw_input("More...")

#
#  Membership and Identity Operators
#

""" 
    Membership operators are useful for checking whether a value is a member
    of a mapping.  They are simply 'in' and 'not in', and return a Boolean.
"""

a_list = [3, 4, 5, 6, 7]
a_dict = {"one": 1, "two": 2, "three": 3}

print "4 in a_list: {}".format(4 in a_list)
print "8 not in a_list: {}".format(8 not in a_list)

""" When used on dicts, it compares the value to the keys"""
print "'one' in a_dict: {}".format('one' in a_dict)
print "'two' not in a_dict: {}".format('two' not in a_dict)

"""
    Identity operators are a quick way to check whether two variables point to 
    the same object
"""
print

a = 3
b = a
c = 3

print "a is b: {}".format(a is b)
print "b is c: {}".format(b is c)
print "a is not c: {}".format(a is not c)









