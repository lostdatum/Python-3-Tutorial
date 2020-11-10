# =============================================================================
#                          DEFINING CONTAINER CLASSES
# =============================================================================

# This tutorial is about special instance methods for containers.
# In this example, we will design a wrapper for the 'dict' container class.

# -------------------------------- DEFINITIONS --------------------------------


class WDict:
    """Basic dictionary wrapper class."""

    # About container classes
    # -----------------------
    # In addition to usual special methods, container classes should also
    # redefine container-specific special methods such as:
    # __contains__, __len__, __getitem__, __setitem__, __delitem__, etc.


    def __init__(self): # Initializer
        """Creates WDict instance."""

        print("DEBUG: creating WDict instance.") # DEBUG
        self._dictattr = dict() # object contains only a dictionary
            # Uses dict() method of class *dict*.


    def __del__(self): # Finalizer
        """Deletes WDict instance."""
        # Educational but not very useful here.

        print("DEBUG: deleting WDict instance.") # DEBUG
        self._dictattr.clear() # deletes all items. 
            # Uses clear() method of class *dict*.


    def __repr__(self): # Representation
            """Returns a detailed string representation of the WDict."""
            # We could define __str__ as well, but it is not mandatory.

            return "WDict: _dictattr = {}".format(repr(self._dictattr))
                # Uses __repr__() method of class *dict*.


    def __getitem__(self, key): # Item getter
        """Returns item which key is given."""
        # Called, for instance, by *obj = instance[key]* statements.

        print("DEBUG: getting item '{}'.".format(key)) # DEBUG
        return self._dictattr[key]
            # Uses __getitem__ method of class *dict*.
            # Equivalent to self._dictattr.__getitem__(key).


    def __setitem__(self, key, value): # Item setter
        """Sets item which key is given to given value."""
        # Called by *instance[key] = value* statements.

        print("DEBUG: setting item '{}'.".format(key)) # DEBUG
        self._dictattr[key] = value
            # Uses __setitem__ method of class *dict*.
            # Equivalent to self._dictattr.__setitem__(key, value).


    def __delitem__(self, key): # Item deleter
        """Deletes item whick key is given."""
        # Called by *del instance[key]* statements.

        print("DEBUG: deleting item '{}'.".format(key)) # DEBUG
        del self._dictattr[key]
            # Uses __delitem__ method of class *dict*.
            # Equivalent to dict.__delitem__(self._dictattr, key).


    def __contains__(self, key): # Item finder
        """Returns True if given key exists, else False."""
        # Called by *key in instance* statements.

        print("DEBUG: looking for key '{}'.".format(key)) # DEBUG
        return (key in self._dictattr)
            # Uses __contains__ method of class *dict*.
            # Equivalent to dict.__contains__(self._dictattr, key).


    def __len__(self): # Length
        """Returns the length of the calling WDict instance."""
        
        return len(self._dictattr)
            # Uses __len__ method of class *dict*.
            # Equivalent to dict.__len__(self._dictattr)



# -------------------------------- TEST SCRIPT --------------------------------


import misctest as mt


mt.sectprint("Create instance")
mydict = WDict()
mt.instprint(mydict)
mt.sectprint("Set item")
mydict["devil"] = 666
mydict["truth"] = 42
mt.instprint(mydict)
mt.sectprint("Print instance")
print(mydict)
mt.sectprint("Get length")
print("Number of elements: {}".format(len(mydict)))
mt.sectprint("Get item")
key = "truth"
print("Item '{}' = {}".format(key, mydict[key]))
mt.sectprint("Look for item")
print("Key '{}' exists: {}".format(key, (key in mydict)))
mt.sectprint("Delete item")
del mydict[key]
print("Key '{}' exists: {}".format(key, (key in mydict)))
print(mydict)
mt.sectprint("Delete instance")
content = mydict._dictattr
del mydict