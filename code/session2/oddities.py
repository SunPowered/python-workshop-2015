"""
    oddities.py - Some more esoteric structures that are not essential, but have their place
"""
print
squared = lambda x: x ** 2  # The lambda operator returns a function inline

print "What is 4**2?: {}".format(squared(4))
print "'squared' is of type: {}".format(type(squared))


#  It is equivalent to defining a function all on its own
def squared_f(num):
    return num ** 2
    
print "What is 4**2 again? {}".format(squared_f(4))
print "'squared_f' is of type: {}".format(type(squared_f))
print 

"""
    Quick script testing can be performed via the 'assert' function.  Must evaluate to a Boolean.
    Throws an AssertionError if it fails, does nothing if it doesn't fail. 
"""

assert 4 > 2

try:
    print "I'm trying an assertion here"
    assert 4 < 2
except AssertionError:
    print "Assertion raised, you should really know better"
    

