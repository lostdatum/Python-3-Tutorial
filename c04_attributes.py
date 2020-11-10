# =============================================================================
#                            CLASSSES & ATTRIBUTES
# =============================================================================

# This tutorial is about classes. We will see how to define a class and see
# some kinds of attributes a class may have. On the way we will have a first
# glance at @classmethod and @staticmethod decorators.


# About objects, classes and instances in Python
# ----------------------------------------------
# An object is a data structure with a unique ID, containing other objects,
# which are called attributes of that object.
# There is a saying: "in Python, everything is an object". Are objects:
# data structures of any type, functions/methods, classes, exceptions, ...
# A class is an object which may be used as template to create other objects,
# which are called instances of that class.



# -------------------------------- DEFINITIONS --------------------------------


class CommonClass: # class definition
    """A class which has instance attributes and methods.""" # docstring

    # About special attributes
    # ------------------------
    # All attributes surrounded by double underscores,
    # as in '__membername__' are called special (or magic) attributes.
    # Special attributes names are similar to reserved keywords in class scope.

    # About instance methods
    # ----------------------
    # Instance methods may only be called from an instance.
    # Call example: instance.imethod()
    # Instance methods always take calling instance as argument, which is
    # refered to as 'self' inside method definition.


    def __init__(self, attr_1, attr_2): # Initializer (= constructor)
        """Initializes a CommonClass instance."""
        # This is a special instance method.
        # Called by CommonClass(). Always uses class name.
        # Instance attributes may be declared and initialized here.

        # Instance attributes
        self.instattr_1 = attr_1
        self.instattr_2 = attr_2
    

    def __repr__(self): # String representation
        """Returns a string representation of a CommonClass instance."""
        # This is a special instance method.
        # Called in particular by repr() and display for in interpreter,
        # and also str() and print() when method __str__ is not defined.

        formstr = "CommonClass instance: instattr_1 = {} ; instattr_2 = {}"
        return formstr.format(repr(self.instattr_1), repr(self.instattr_2))


    def dosmtg(self):
        """A method which does something."""
        # This is a standard instance method.
        # Called by instance.dosmtg().

        print("Doing something...")




class VeryHandyClass:
    """A class which only has class attributes and methods."""

    # About class methods
    # -------------------
    # Class methods can be declared with @classmethod decorator.
    # Class methods may be called from the class or from an instance.
    # Call examples: class.cmethod(), instance.cmethod()
    # Class methods always take caller's class as argument, which is
    # refered to as 'cls' inside method definition.


    # Class attributes
    clsattr_1 = 'a class attribute'
    clsattr_2 = 'another class attribute'


    @classmethod # declares following as class method
    def help(cls):
        """Prints help text."""
        # Here we use the __doc__ special class attribute.
        # It contains the class docstring.

        return cls.__doc__




class TotallyUsefulClass:
    """A class which only has static methods."""


    # About static methods
    # --------------------
    # Static methods can be declared with @staticmethod decorator.
    # Static methods may be called from class name or from an instance.
    # Call examples: classname.smethod(...), instance.smethod(...)
    # Static methods neither take caller instance nor class as argument.


    @staticmethod # declares following as static method
    def dostuff():
        """A method which does stuff."""
        # This is an example of static method.

        print("Doing stuff...")


    @staticmethod
    def donothing():
        """A method which does nothing."""
        # This is an example of static method.

        print("Doing nothing...")




class BestClassEver:
    """An empty class."""
    pass # does nothing but mandatory to comply with Python syntax




# -------------------------------- TEST SCRIPT --------------------------------


import misctest as mt


cls = CommonClass
mt.sectprint("Testing {}".format(cls))
mt.clsprint(cls)
print("Let us create an instance and print it.")
myinst = CommonClass('an instance attribute', 'another instance attribute')
print(myinst)
print("Let us declare a new instance attribute.")
myinst.instattr_3 = 'new on-the-fly attribute'
mt.instprint(myinst)

cls = VeryHandyClass
mt.sectprint("Testing {}".format(cls))
mt.clsprint(cls)
print("Let us call a class method.")
cls.help()

cls = TotallyUsefulClass
mt.sectprint("Testing {}".format(cls))
mt.clsprint(cls)
print("Let us call a static method.")
cls.donothing()

cls = BestClassEver
mt.sectprint("Testing {}".format(cls))
mt.clsprint(cls)
print("Let us declare a new class attribute.")
cls.on_the_fly_attr = 'Not empty anymore!'
mt.clsprint(cls)


# CONCLUSIONS:
# When defining a class in Python, there is not any mandatory member.
# In addition to usual Object Oriented Programming (as in C++ and JAVA),
# a class can also serve as:
#   - a collection of variables and functions in a namespace,
#   - a basic data structure (like 'struct' in C).
# Also it is worth noting that it is possible to declare new class attributes
# or instance attributes outside of class definition (which is not allowed in
# other languages).