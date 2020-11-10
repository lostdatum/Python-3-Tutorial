# =============================================================================
#                             MULTIPLE INHERITANCE
# =============================================================================


# This tutorial is about multiple inheritance.
# See: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
# I use the vocabulary of trees because I believe it makes things clearer. So 
# 'parent class' means 'base class' and 'child class' means 'derived class'.
# Multiple inheritance means a class may have multiple parents.
# In this example, class Griffin has parent classes Eagle and Lion. For those
# who do not know: https://en.wikipedia.org/wiki/Griffin
# We will compare several implementations and see what works.


# ---------------------------- COMMON DEFINITIONS -----------------------------


import misctest as mt # simple functions I made for testing


class Eagle:
    """Large bird."""


    nests = True


    def __init__(self):
        self.has_wings = True
        self.has_rear_legs = True


    def fly(self):
        if self.has_wings:
            print("Flying...")
        else:
            print("No wings to fly!")



class Lion:
    """Large cat."""


    nests = False


    def __init__(self):
        self.has_wings = False
        self.has_rear_legs = True
        self.has_front_legs = True


    def run(self):
        if self.has_rear_legs and self.has_front_legs:
            print("Running...")
        else:
            print("Not enough legs to run!")




def testroutine(clsseq, metseq): # the test routine we will use
    """
    Description of arguments:
        clsseq: Sequence containing classes to be tested.
        metseq: Sequence containing methods to be tested for each class. Methods
                must not take any arguments (except caller object).
    """

    for cls in clsseq:
        mt.sectprint("Testing {}".format(cls))
        print("MRO: ", cls.__mro__)
        mt.stepprint("Class attributes")
        mt.clsprint(cls, exclude=['special', 'non-method'])
        mt.stepprint("Accessing class attributes")
        try:
            print("{}.nests = {}".format(cls.__name__, cls.nests))
        except AttributeError as err:
                print("ERROR:", err)
        mt.stepprint("Instance attributes")
        creature = cls()
        mt.instprint(creature)
        mt.stepprint("Testing instance methods")
        for action in metseq:
            try:
                method = getattr(creature, action)
                method()
            except AttributeError as err:
                print("ERROR: {}".format(err))





#%% =========================== IMPLEMENTATION #1 =============================
#
# Here we will just try something candid and see how it goes.


# -------------------------------- DEFINITIONS --------------------------------


class Tryin(Lion, Eagle): # do the order of parent classes matter?
    """Mix of an Lion and an Eagle."""
    
    pass



class Testin(Eagle, Lion): # let's try the other way around
    """Mix of an Eagle and a Lion."""
    
    pass



# -------------------------------- TEST SCRIPT --------------------------------


mt.headprint("Implementation #1")
testroutine([Tryin, Testin], ['fly', 'run'])



# CONCLUSIONS:
#   - Both definitions do not work, but the second is better as the class
#     attribute 'nests' is correct at least.
#   - Inheritance priority for class attributes is defined by the Method Reso-
#     lution Order (MRO).
#     See: https://www.python.org/download/releases/2.3/mro/
#     Basicly, inheritance priority is: down to top, then left to right.
#     So here we need (Eagle, Lion) to have 'nests = True'.
#   - Here, the __init__ method is inherited only from the highest priority 
#     parent, so instance attributes are not merged by default. This is the
#     main issue in this implementation.



#%% =========================== IMPLEMENTATION #2 =============================
#
# This time we will try to implement merging of inherited instance attributes
# by ourselves. To do this, we will make sure the child's __init__ method calls 
# all parents's versions of __init__ method.
# Everything else is the same.


# -------------------------------- DEFINITIONS --------------------------------


class Failin(Eagle, Lion): # order does matter here
    """Mix of an Lion and an Eagle."""
    
    def __init__(self): # does order also matter here?
        Eagle.__init__(self) # static call to parent's method
        Lion.__init__(self)



class Griffin(Eagle, Lion):
    """Mix of an Eagle and an Lion."""

    def __init__(self): # let's try the other way around
        Lion.__init__(self) 
        Eagle.__init__(self)



# -------------------------------- TEST SCRIPT --------------------------------

mt.headprint("Implementation #2")
testroutine([Failin, Griffin], ['fly', 'run'])



# CONCLUSIONS: This works if we pay attention.
# - For instance attributes, inheritance priority obviously depends on the
#   order parents's methods are called. Successive calls to different versions
#   of __init__ may overwrite previously defined attributes, so last calls have
#   highest priority.
# - Merging of instance attributes may be manually defined with different
#   priority from inheritance of class attributes (which follows MRO).



#%% =========================== IMPLEMENTATION #3 =============================

# Same as previous implementation, but uses super() method to call parent's
# __init__ method instead of referencing it by name.
# See: https://docs.python.org/3/library/functions.html#super
# Everything else is the same.


# -------------------------------- DEFINITIONS --------------------------------


class Eagle:
    """Large bird."""


    nests = True


    def __init__(self):
        super().__init__() # dynamic call to next in MRO (i.e. Lion)
        self.has_wings = True
        self.has_rear_legs = True


    def fly(self):
        if self.has_wings:
            print("Flying...")
        else:
            print("No wings to fly!")



class Griffin(Eagle, Lion):
    """Mix of an Eagle and an Lion."""
    

    def __init__(self):
        super().__init__() # dynamic call to next in MRO (i.e. Eagle)



# -------------------------------- TEST SCRIPT --------------------------------

mt.headprint("Implementation #3")
testroutine([Griffin], ['fly', 'run'])


# CONCLUSIONS: This works just fine.
# - With the super() approach, both class and instance attributes inheritance
#   merge automatically, and priority depends only on the MRO.
# - Parent classes must also call super().__init__ to pass it on to the next
#   sibling or parent in the MRO.