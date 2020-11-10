# =============================================================================
#                             SIMPLE INHERITANCE
# =============================================================================

# This tutorial is about simple inheritance.
# See: https://docs.python.org/3/tutorial/classes.html#inheritance
# I use the vocabulary of trees because I believe it makes things clearer. So 
# 'parent class' means 'base class' and 'child class' means 'derived class'.
# Simple inheritance means a class may have only one parent. Regardless, a class
# may still have several children (which are then siblings).
# Inheritance may be multilevel, which is when children also have children.
# In this example, class Animal has a child class Fish, which also has a child 
# class Megalodon.
# We will compare several implementations and see what works.


# --- COMMON DEFINITIONS --- (for everything that follows)


import misctest as mt # simple functions I made for testing



class Animal: # the base class
    """Living being which eats and sleeps."""


    is_extinct = False # class attribute


    def __init__(self): # instance method
        self.has_body = True


    def __repr__(self):
        string = "Representation of {} instance:\n".format(type(self).__name__)
        for (key, value) in vars(self).items():
            string += ("{}: {}\n".format(repr(key), repr(value)))
        return string


    def sleep(self):
        print("Sleeping...")




def testroutine(clsseq, metseq): # the test routine we will use
    """
    Description of arguments:
        clsseq: Sequence containing classes to be tested.
        metseq: Sequence containing methods to be tested for each class. Methods
                must not take any arguments (except caller object).
    """

    for cls in clsseq:
        mt.sectprint("Testing {}".format(cls))
        mt.stepprint("Class attributes")
        mt.clsprint(cls, exclude=['special', 'non-method'])
        mt.stepprint("Accessing class attributes")
        try:
            print("{}.is_extinct = {}".format(cls.__name__, cls.is_extinct))
        except AttributeError as err:
                print("ERROR:", err)
        mt.stepprint("Instance attributes")
        creature = cls()
        mt.instprint(creature)
        mt.stepprint("Accessing instance attributes")
        try:
            print("creature.has_body = {}".format(creature.has_body))
        except AttributeError as err:
                print("ERROR:", err)
        try:
            print("creature.has_scales = {}".format(creature.has_scales))
        except AttributeError as err:
                print("ERROR:", err)
        try:
            print("creature.has_teeth = {}".format(creature.has_teeth))
        except AttributeError as err:
                print("ERROR:", err)
        mt.stepprint("Testing instance methods")
        print(creature)
        for action in metseq:
            try:
                method = getattr(creature, action)
                method()
            except AttributeError as err:
                print("ERROR: {}".format(err))



# ============================= IMPLEMENTATION #1 =============================
#
# Here we will just try something candid and see how it goes.


# --- DEFINITIONS ---


class Fish(Animal):
    """Animal which lives underwater."""
    # NB: We redefine neither __repr__ method nor attribute 'is_extinct' here.

    def __init__(self): # redefinition
        self.has_scales = True


    def swim(self): # new definition
        print("Swimming...")



class Megalodon(Fish):
    """Ancient and huge predator fish."""
    # NB: We redefine neither __repr__ method nor attribute 'is_extinct' here.

    is_extinct = True # redefinition


    def __init__(self): # redefinition
        self.has_teeth = True


    def hunt(self): # new definition
        print("Hunting...")



# NB: In both cases, we did NOT redefine __repr__ method...
# Let us see what happens.



# --- TEST SCRIPT ---


mt.headprint("Implementation #1")
testroutine([Animal, Fish, Megalodon], ['sleep', 'swim', 'hunt'])


# CONCLUSIONS: This is not quite it.
# - Unless redefined in child class, class attributes (including methods) are
#   called from the first (in MRO order) parent class that has them defined.
# - However, unless redefined in child class, attributes of parent classes are 
#   considered as attributes of the child class.
# - In particular, if child's __init__ method is redefined it just plainly 
#   overwrites the parent's version, therefore parent's instance attributes
#   are not accessible. By default, instance attributes do not cumulate through 
#   inheritance.



# ============================= IMPLEMENTATION #2 =============================
#
# This time we will try to implement merging of inherited instance attributes
# by ourselves. To do this, we will make sure the child's __init__ method calls 
# its parent's version of __init__ method.
# Everything else is the same.


# --- DEFINITIONS ---


class Fish(Animal):
    """Animal which lives underwater."""


    def __init__(self):
        Animal.__init__(self) # static call to parent's method
        self.has_scales = True


    def swim(self):
        print("Swimming...")



class Megalodon(Fish):
    """Ancient and huge predator fish."""


    is_extinct = True


    def __init__(self):
        Fish.__init__(self) # static call to parent's method
        self.has_teeth = True


    def hunt(self):
        print("Hunting...")


# --- TEST SCRIPT ---

mt.headprint("Implementation #2")
testroutine([Animal, Fish, Megalodon], ['sleep', 'swim', 'hunt'])


# CONCLUSIONS: This works.
# - By calling the the parent's version of __init__ method inside child's 
#   __init__ method, we can cumulate instance attributes through inheritance.
# - More generally, if we have an inherited method that we want to upgrade,
#   we may redefine it and then call parent's version inside its body.



# ============================= IMPLEMENTATION #3 =============================

# Same as previous implementation, but uses super() method to call parent's
# __init__ method instead of referencing it by name.
# See: https://docs.python.org/3/library/functions.html#super
# Everything else is the same.


# --- DEFINITIONS ---


class Fish(Animal):
    """Animal which lives underwater."""


    def __init__(self):
        super().__init__() # dynamic call to parent's method
        self.has_scales = True


    def swim(self):
        print("Swimming...")



class Megalodon(Fish):
    """Ancient and huge predator fish."""

    is_extinct = True


    def __init__(self):
        super().__init__() # dynamic call to parent's method
        self.has_teeth = True


    def hunt(self):
        print("Hunting...")


# TEST SCRIPT

mt.headprint("Implementation #3")
testroutine([Animal, Fish, Megalodon], ['sleep', 'swim', 'hunt'])



# CONCLUSIONS: This also works.
# - Systematically calling super().__init__() inside __init__ is a way of
#   changing default inheritance behavior for instances without having to
#   think too much about it.
# - Another advantage of using super() is that it automatically finds the
#   names of parents classes. This should make code maintenance easier.
