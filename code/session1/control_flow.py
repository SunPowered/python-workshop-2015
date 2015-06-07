# -*- coding: utf-8 -*-
"""
    control_flow.py - Getting Started - Program Control Flow
    
    This file describes the logic control elements needed for 
    program scripting.  Many of these ideas carry forward from 
    other languages.
"""
import os

#
#  If / Elif / Else
#

"""
    -- Syntax -- 
    if {Boolean}:
        {do something}
    else:
        {do something else}
"""
print
my_flag = True

if my_flag:
    print "The flag is True"
else:
    print "The flag is False"

print
none_flag = None

if none_flag:
    print "none_flag is True"
else:
    print "none_flag is False"
    
if 2 > 1:
    print "Look at that, 2 is bigger than 1"
else:
    print "Not gonna happen"
    
print
my_case = 2 > 1

if my_case:
    print "2 is still bigger than 1"
else:
    print "Hmm, 2 is less than or equal to 1?"

"""
    You can call an extra if in the else statement with elif
""" 
do_it = False

if do_it:
    print "let it be done"
elif do_it is None:
    print "We have lost do_it"
else:
    print "Don't do it"

raw_input("More...")

#
#  For loops
#

"""
    -- Syntax -- 
    for {var} in {iterable}:
        {do something with 'var'}
"""
print
print "I can count to 10"
for i in range(10):
    print i

print
print "Days of the week:"
weekdays = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
for day in weekdays:
    print "Today is {}".format(day)

raw_input("More...")

#
# While
#

"""
    -- Syntax -- 
    while {Boolean}:
        {do something}
"""

print
print "Count to 5"
counter = 0
while counter < 5:
    print counter
    counter += 1

raw_input("More...")

#
# with
#

with open('file.txt', 'w') as f:
    f.write("This is a line")
    f.write("This is another line")
os.remove("file.txt")


#
#  try / except / else / finally
#

"""
    -- Syntax -- 
    try:
        {some code}
    except {Exception Type}:
        {some more code}
    else:
        # optional
        {code if no exception raised}
    finally:
        # optional
        {code to run after all is finished, regardless of exception}
"""
print
print "Try / Except"
my_case = 0
my_list = [1, 2, 3, 4]
try:
    print my_list[2]
except IndexError:
    print "There is no index here, do something else"
    my_case = 1
else:
    my_case = 2
finally:
    print "I always run"
    my_case = 3
    print "my_case: {}".format(my_case)
