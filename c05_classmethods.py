# =============================================================================
#                                CLASS METHODS
# =============================================================================

# This tutorial gives an application example for class methods.
# We will use them to monitor instances of the class Rabbit.

# -------------------------------- DEFINITIONS --------------------------------


import copy


class Rabbits():
    """Class for studying evolution of rabbit couples. Fibonacci loves it."""


    stock = [] # stock of rabbit couples (class attribute)


    def __init__(self): # Initializer
        """Creates a couple of rabbits."""

        self.grownup = False # newborn
        self.stock.append(self) # adds itself to the stock


    def __repr__(self): # String representation
        """Simple string representation of Rabbits."""

        if self.grownup:
            return 'grownup'
        else:
            return 'newborn'


    @classmethod
    def grow(cls):
        """Makes Rabbits in the stock either grow up or reproduce."""

        curpop = copy.copy(cls.stock)
        for couple in curpop:
            if couple.grownup:
                # Grownups reproduce (1 grownup couple yields 1 newborn couple)
                cls() # call class initializer
            else:
                # Newborns grow up
                couple.grownup = True
    

    @classmethod
    def kill(cls):
        """Resets Rabbits stock."""

        cls.stock.clear()


    @classmethod
    def number(cls):
        """Returns number of Rabbits object."""

        return len(cls.stock)



# -------------------------------- TEST SCRIPT --------------------------------


import misctest as mt # custom functions to make tests easier


mt.stepprint("Rabbits population (3 steps)")
Rabbits() # create a couple of rabbits
print("STEP\tPOPULATION (couples)")
print("0\t{}".format(Rabbits.stock))
Rabbits.grow()
print("1\t{}".format(Rabbits.stock))
Rabbits.grow()
print("2\t{}".format(Rabbits.stock))
Rabbits.grow()
print("3\t{}".format(Rabbits.stock))

iterations = 10
mt.stepprint("Rabbits population ({} steps)".format(iterations))
Rabbits.kill() # fresh start
Rabbits()
print("STEP\tNUMBER (couples)")
print("0\t{}".format(Rabbits.number()))
for step in range(1, 1 + iterations):
    Rabbits.grow()
    print("{}\t{}".format(step, Rabbits.number()))