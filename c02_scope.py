# =============================================================================
#                              SCOPE OF OBJECTS
# =============================================================================


# This tutorial is about the scope of objects in Python.
# Basicly, the scope of an object is the domain in which it can be referered to
# by name (without having to do anything special).
# Namespaces define the scope of the objects declared inside them. For example, 
# these create their own namespace:
#   - modules (i.e. files)
#   - classes
#   - functions/methods
# For now, we will only cover the case of functions in the same module.
# In Python, when a script is being executed, it is refered to by special
# name '__main__', which is the top-level namespace.


#%% ========================= SCOPE INSIDE FUNCTION ===========================

# Here we try to read and overwrite an object defined in the module from inside
# functions.

# -------------------------------- DEFINITIONS --------------------------------


def myobj_print(): # try to read only
    try:
        print("myobj_print: 'myobj' =", myobj)
    except NameError as err:
        print("myobj_print:ERROR:", err)


def myobj_set(value): # try to read and overwrite
    try:
        print("myobj_set(start): 'myobj' =", myobj)
    except NameError as err:
        print("myobj_set(start):ERROR:", err)
    myobj = value # direct assignment (overwrite)
    print("myobj_set(end): 'myobj' =", myobj)


# -------------------------------- TEST SCRIPT --------------------------------

import misctest as mt # custom functions to make tests easier

mt.headprint("SCOPE INSIDE FUNCTION")

mt.stepprint("Set 'myobj' to 0")
myobj = 0
print("main: 'myobj' =", myobj)

mt.stepprint("Calling 'myobj_print()'")
myobj_print()

mt.stepprint("Calling myobj_set(42)")
myobj_set(42)
print("main: 'myobj' =", myobj)


# CONCLUSIONS:
# 1/ A function can read an object from caller namespace *IF & ONLY IF*
#    it does NOT attempt to OVERWRITE it (i.e. directly assign it a new value).
# 2/ When a function tries to OVERWRITE an object 'myobj' from caller namespace:
#     a/ A new object also named 'myobj' is created locally within the function.
#     b/ The original 'myobj' object from caller namespace is masked within
#        the function and cannot be accessed.
#     c/ Any reference to 'myobj' inside the function redirects to the new
#        local object. This is called shadowing (or shading).
#     d/ The original 'myobj' object from caller namespace will be left
#        unchanged by the function.



#%% ============================ GLOBAL KEYWORD ===============================

# This time we declare 'myobj' as global object inside the function, using
# keyword 'global'.

# -------------------------------- DEFINITIONS --------------------------------


def myobj_glob_set(value): # try to read and overwrite
    global myobj # ADDED: declare 'myobj' as global object
    try:
        print("myobj_glob_set(start): 'myobj' =", myobj)
    except NameError as err:
        print("myobj_glob_set(start):ERROR:", err)
    myobj = value # direct assignment (overwrite)
    print("myobj_glob_set(end): 'myobj' =", myobj)


# -------------------------------- TEST SCRIPT --------------------------------

mt.headprint("GLOBAL KEYWORD")

mt.stepprint("Set 'myobj' to 0")
myobj = 0
print("main: 'myobj' =", myobj)

mt.stepprint("Calling 'myobj_glob_set(42)'")
myobj_glob_set(42)
print("main: 'myobj' =", myobj)



# CONCLUSIONS:
# 3/ A function can OVERWRITE an object from caller namespace *IF & ONLY IF*
#    this object is declared as global inside the function.



#%% =================== MODIFYING MUTABLES INSIDE FUNCTION ====================

# Previously we used the functions with an immutable object (integer).
# This time, we try with a mutable object (list), and check what happens when
# we try to mutate the object inside the function instead of overwriting it.

# -------------------------------- DEFINITIONS --------------------------------


def myobj_set_elt(idx, value): # try to read and modify
    try:
        print("myobj_set_elt(start): 'mylist' =", mylist)
    except NameError as err:
        print("myobj_set_elt(start):ERROR:", err)
    mylist[idx] = value # mutation with list.__setattr__()
    print("myobj_set_elt(end): 'mylist' =", mylist)


def myobj_add_elt(value): # try to read and modify
    try:
        print("myobj_add_elt(start): 'mylist' =", mylist)
    except NameError as err:
        print("myobj_add_elt(start):ERROR:", err)
    mylist.append(value) # mutation with list.append()
    print("myobj_add_elt(end): 'mylist' =", mylist)



# -------------------------------- TEST SCRIPT --------------------------------


mt.headprint("MODIFYING MUTABLES INSIDE FUNCTION")

mt.stepprint("Set 'mylist' to [0]")
mylist = [0]
print("main: 'mylist' =", mylist)

mt.stepprint("Calling 'myobj_set([42, 666])'")
myobj_set([42, 666])
print("main: 'mylist' =", mylist)

mt.stepprint("Calling 'myobj_set_elt(0, 42)'")
myobj_set_elt(0, 42)
print("main: 'mylist' =", mylist)

mt.stepprint("Calling 'myobj_add_elt(666)'")
myobj_add_elt(666)
print("main: 'mylist' =", mylist)


# CONCLUSIONS:
# 4/ We can use methods inside a function to MODIFY a mutable object from
#    caller namespace (without having to do anything special).