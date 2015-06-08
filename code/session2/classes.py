# -*- coding: utf-8 -*-

"""
    classes.py - Advanced Topics 1.  
    
    An intro to classes
"""

"""
    Classes are the meat and bones of any library and the core language itself.   
    Remember, everything is an object?  Well, 'object' is a real thing ... its the parent 
    of all classes!
    
    Classes are the core of Object Oriented Programming, made popular by Java.  It is incredibly useful,
    and makes for very robust, testable, and extendable code.  It is very good coding practice, though
    can be a little too mucb overhead for simple needs.
"""

print "'object' is a real thing in Python, strangely it has type of : '{}'".format(type(object))

"""
    The class object is a data structure, holding attributes (variables) and methods (functions).  All 
    class methods take itself as a required first argument, called 'self'.  
    
    Classes are defined with the 'class' keyword, though must be instantiated to be effective.  
    The '__init__' method runs upon instantiation and serves to setup the class.
"""

class MyClass(object):
    """Here we go, our first class."""
    
    def __init__(self, *args, **kwargs):
        """Our class takes any number of args and kwargs"""
        self.first_arg = None
        self.remaining_args = None
        
        if len(args) > 0:
            self.first_arg = args[0]
        if len(args) > 1:
            self.remaining_args = args[1:]

        self.data = kwargs  # For now just save all kwargs in a data attribute            

    def print_args(self):
        """ This method prints the arguments that the class was instantiated with"""
        print "The first argument was: {}".format(self.first_arg)
        print "The remaining arguments were: {}".format(self.remaining_args)
        print "The data kwargs were: {}".format(self.data)
        
    def n_kwargs(self):
        """ This returns the number of keyword arguments the class was instantiated with"""
        return len(self.data)
        

    def foo(self):
        """ This returns the total number of arguments and keyword arguments """
        
        n = self.n_kwargs()
        if self.first_arg:
            n += 1
        if self.remaining_args:
            n += len(self.remaining_args)
        
        return n
        
print "MyClass has been defined but not yet instantiated, it has type: {}".format(type(MyClass))

""" 
    Instances of the class can be created by calling the class like we are running a function,
    this calls the '__init__' method.
"""
class1 = MyClass(1,2,3, one=1, two=2)
class2 = MyClass(3,4,5, three=3)

print "We can call methods on these objects individually"
print "class1.print_args():"
class1.print_args()
print
print "class2.print_args():"
class2.print_args()
print



print "Calling 'foo' method of class1: {}".format(class1.foo())
print "Calling 'foo' method of class2: {}".format(class2.foo())

#raw_input("More...")
"""
    Here is where classes can be useful, we can override methods and attributes of classes.  Methods
    can really only be overriden before instantiation
"""

print
class1.first_arg = "Sucka!"
class1.print_args()
print

def new_foo(self):
    """ Some different logic than before"""
    n = self.n_kwargs()
    if self.first_arg:
        n -= 1
    if self.remaining_args:
        n -= len(self.remaining_args)
    return n
    
MyClass.foo = new_foo

class3 = MyClass(3,4,5,6, three=3)
print "I just changed the 'foo' method of MyClass.  See? {}".format(class3.foo())


#raw_input("More...")

""" Classes can be extended by defining them as a parent of new classes"""

class Car(object):
    """ The base Car object"""
    
    def __init__(self, manufacturer=None, colour=None, num_doors=None, horsepower=None):
        self.manufacturer = manufacturer or 'unknown manufacturer'
        self.colour = colour or 'unknown colour'
        self.horsepower = horsepower or 'unknown'
        self.num_doors = num_doors or 4
        
    def is_sedan(self):
        return self.num_doors == 4
    
    def is_coupe(self):
        return self.num_doors == 2
        
    def print_specs(self):
        
        print "This is a {} door {} car made by {}.  It can put out {} horsepower".format(
            self.num_doors, self.colour, self.manufacturer, self.horsepower)
            

"""
    Now we can subclass the general 'Car' class to more specific variants.  Showing the 'super' function
"""
class Volkswagon(Car):
    """ The people's car"""
    def __init__(self, **kwargs):
        kwargs['manufacturer'] = 'VW'
        super(Volkswagon, self).__init__(**kwargs)
    

class Beetle(Volkswagon):
    """ The VW Beetle"""
    def __init__(self, **kwargs):
        kwargs['num_doors'] = 2
        kwargs['horsepower'] = 100
        super(Beetle, self).__init__(**kwargs)
    
class MyBug(Beetle):
    """ The classic Bug"""
    def __init__(self):
        super(MyBug, self).__init__(colour="blue")
    
generic_car = Car()
vw = Volkswagon()
red_beetle = Beetle(colour="red")
mybug = MyBug()

"""
    We can check whether objects are children of higher level classes via 'isinstance'.
    Checking the parents of class definitions requires another method 'issubclass'
"""
print
print "The generic_car is an instance of Car: {}".format(isinstance(generic_car, Car))
print "The generic_car is an instance of Volkswagon: {}".format(isinstance(generic_car, Volkswagon))
print "The mybug is an instance of Car: {}".format(isinstance(mybug, Car))
print "MyBug is a subclass of Volkswagon: {}".format(issubclass(MyBug, Volkswagon))

print
print "Now, compare the specs of each of these instantiated classes"

"""
    Classes can be imported by module.ClassName format in several ways
    
    from at1 import Car
    import at1.Car
    import at1.Car as Auto
    from at1 import Car as Auto    
"""