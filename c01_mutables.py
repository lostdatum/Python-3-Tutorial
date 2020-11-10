# =============================================================================
#                        MUTABLE AND IMMUTABLE OBJECTS
# =============================================================================

# This tutorial is about mutable and immutable objects in Python.
# Basicly, all assignments result in creating a REFERENCE to an object.


#%% ============================ Mutable objects ==============================
# These objects can have their value modified or overwritten.
# Instances of user-defined classes are normally mutable.
# The most frequent built-in mutable classes are: 'set', 'list', 'dict'.


import misctest as mt # custom functions to make tests easier


mt.headprint("Mutable classes")

# ------------------------------- Class 'list' --------------------------------
mt.sectprint("Class 'list'")

mt.stepprint("Do a = [1, 2] and b = a")
a = [1, 2]
b = a
print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))

mt.stepprint("Do a[0:2] = [3, 4]")
a[0:2] = [3, 4]
print("a =", a)
print("b =", b)

mt.stepprint("Do b.append(5)")
b.append(5)
print("a =", a)
print("b =", b)

mt.stepprint("Do a = [0, 0, 0]")
a = [0, 0, 0]
print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))



# CONCLUSIONS:
# For mutable objects, when using instruction 'b = a', variable 'b' is an ALIAS of 'a':
#   1/ Nametags 'a' and 'b' point to the same object in memory.
#   2/ Directly setting 'a' breaks the association between 'a' and 'b'. It links the nametag
#      'a' to a new object, different from the old one, which 'b' keeps pointing to. 



#%% =========================== Immutable objects =============================
# These objects cannot have their value modified, only overwritten.
# Most common built-in immutable classes are:
# 'int', 'float', 'decimal', 'bool', 'str', 'tuple'

mt.headprint("Immutable classes")

# -------------------------------- Class 'int' --------------------------------

mt.sectprint("Class 'int'")

mt.stepprint("Do a = 0 and b = a")
a = 0
b = a
print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))

mt.stepprint("Do a = 1")
a = 1
print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))

# -------------------------------- Class 'str' --------------------------------

mt.sectprint("Class 'str'")

mt.stepprint("Do a ='ninja' and b = a")
a = "ninja"
b = a
print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))

mt.stepprint("Do a = 'warrior'")
a = "warrior"
print("a =", a)
print("b =", b)
print("id(a) =", id(a))
print("id(b) =", id(b))



# CONCLUSIONS:
#   1/ For immutable objects, since the referenced object cannot be modified,
#      one can only assign another object to the nametag.
#   2/ When using instruction 'b = a', for all practical purposes, variable 'b'
#      may be considered as a COPY of 'a'.
#   3/ As soon as 'a' or 'b' is modified, those nametags will point to 
#          different objects in memory.
#   4/ As opposed to other languages (e.g. C/C++) a string is not considered as
#      an array of characters (there is no built-in character type in Python).



#%% ========================== COPY MUTABLE OBJECTS ===========================

# We will use the copy() and deepcopy() functions from module copy, to create a 
# static copy of a custom object (a dictionary of lists).
# To make things clearer, item nametags will be prefixed with 'Ln_', 'n' being
# the depth level of the item with respect to top-level object.
# With this convention, the higher 'n' is, the deeper/lower level the item is.
# So L0 is the top-level, and for 'n > 1', L(n) objects are items of a L(n-1) 
# object, i.e. a L(n-1) object is a container for L(n) objects.

import copy

mt.headprint("Copying mutable objects")

mt.stepprint("Create L2 item")
L2_item = [1,2,3]
print("L2_item =", L2_item)
print("id(L2_item) =", id(L2_item))

mt.stepprint("Create L0 object and add L1 item containing previous L2 item")
L0_original = {"L1_item_1":L2_item}
print("L0_original =", L0_original)
print("id(L0_original) =", id(L0_original))

mt.stepprint("Create L0 alias: L0_alias = L0_original")
L0_alias = L0_original
print("L0_alias =", L0_alias)
print("id(L0_alias) =", id(L0_alias))

mt.stepprint("Create L0 copy: L0_copy = copy.copy(L0_original)")
L0_copy = copy.copy(L0_original)
print("L0_copy =", L0_copy)
print("id(L0_copy) =", id(L0_copy))

mt.stepprint("Create L0 deepcopy: L0_deepcopy = copy.deepcopy(L0_original)")
L0_deepcopy = copy.deepcopy(L0_original)
print("L0_deepcopy =", L0_deepcopy)
print("id(L0_deepcopy) =", id(L0_deepcopy))

mt.stepprint("Add new L1 item: 'L1_item_2':[4,5,6]")
L0_original["L1_item_2"] = [4,5,6]
print("L0_original =", L0_original)
print("L0_alias =", L0_alias)
print("L0_copy =", L0_copy)
print("L0_deepcopy =", L0_deepcopy)

mt.stepprint("Modify 'L1_item_1'")
L2_item[0:3] = [0, 0, 0]
print("L0_original =", L0_original)
print("L0_alias =", L0_alias)
print("L0_copy =", L0_copy)
print("L0_deepcopy =", L0_deepcopy)

mt.stepprint("Let's see ID of 'L1_item_1'")
print("id(L0_original['L1_item_1']) =", id(L0_original['L1_item_1']))
print("id(L0_alias['L1_item_1']) =", id(L0_alias['L1_item_1']))
print("id(L0_copy['L1_item_1']) =", id(L0_copy['L1_item_1']))
print("id(L0_deepcopy['L1_item_1']) =", id(L0_deepcopy['L1_item_1']))


# CONCLUSIONS:
# 1/ Both copy() and deepcopy() return a new L0 object.
# 2/ Function copy() only creates copies of L1 items. If those items are 
#    references to L2 items, then they will be common to both objects (and same
#    for lower levels).
# 3/ Function deepcopy() recursively copies items from top to deepest level.