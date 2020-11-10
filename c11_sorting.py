# =============================================================================
#                      SORTING ITEMS IN ORDERED CONTAINERS
# =============================================================================

# This tutorial is about sorting items.
# Normally all container classes should be implemented so that the function
# sorted() is effective.
# Some container classes may also implement their own methods, such as 
# list.sort().


import misctest as mt # custom functions to make tests easier


#%% ============================= SORTING LISTS ===============================

mt.headprint("SORTING LISTS")

# ------------------------------ LIST OF STRINGS ------------------------------

mt.sectprint("LIST OF STRINGS")

str_list = ["Bernie", "Albert", "Alice", "Caleb", "Aaron"]
print("Original state:", str_list)

print("\nOutput of sorted(list):", sorted(str_list))
print("Current state:", str_list)

print("\nOutput of sorted(list, reverse=True):", sorted(str_list,reverse=True))
print("Current state:", str_list)

print("\nOutput of list.sort():", str_list.sort())
print("Current state:", str_list)

print("\nOutput of list.sort(reverse=True):", str_list.sort(reverse=True))
print("Current state:", str_list)

# ------------------------------ LIST OF NUMBERS ------------------------------

mt.sectprint("LIST OF NUMBERS")

num_list = [56, -7, 93.44, 93.23, -42]
print("Original state:", num_list)

print("\nOutput of sorted(list):", sorted(num_list))
print("Current state:", num_list)

print("\nOutput of sorted(list, reverse=True):", sorted(num_list,reverse=True))
print("Current state:", num_list)

print("\nOutput of list.sort():", num_list.sort())
print("Current state:", num_list)

print("\nOutput of list.sort(reverse=True):", num_list.sort(reverse=True))
print("Current state:", num_list)



# CONCLUSIONS:
# - For strings, the default sorting method is alphabetical order.
# - For numbers, the default sorting method is ascending order.
# - Function sorted() returns sorted output and does NOT modify the input.
# - Method list.sort() returns *None* and DOES modify the input.
# - Order can be reversed using optional argument 'reverse=True'.



#%% ============================ SORTING TUPLES ===============================

mt.headprint("SORTING TUPLES")

num_tup = (56, -7, 93.44, 93.23, -42)
print("Original state:", num_tup)

print("\nOutput of sorted(tuple):", sorted(num_tup))
print("Current state:", num_tup)
try:
    print("\nOutput of tuple.sort():", num_tup.sort())
except AttributeError as err:
    print("\nERROR:", err)
print("Current state:", num_tup)



# CONCLUSIONS:
# - Function sorted() works for tuples, but also returns a list.
# - Tuple object has no attribute sort (as class tuple is immutable!)



#%% ========================= SORTING CUSTOM OBJECTS ==========================

import operator

mt.headprint("SORTING CUSTOM OBJECTS")


# ----------------------- CUSTOM OBJECT: LIST OF LISTS ------------------------

mt.sectprint("LIST OF LISTS")

purchase = [
    # Item, Unit price, Quantity
    ["hammer", 10, 1],
    ["nail", 0.1, 50],
    ["saw", 40, 1],
    ["brush", 5, 2],
    ["paint", 20, 3]
]

print("Original state:\n", purchase)
print("Standard sorting:\n", sorted(purchase))
print("Sorting using column #1 as key:")
print(sorted(purchase, key=operator.itemgetter(1)))
print("Sorting using column #2 as key:")
print(sorted(purchase, key=lambda record:record[2]))


# CONCLUSIONS:
# - By default, the sorting key is the first column (column #0).
# - The sorting key can be changed with optional argument 'key=...'.
#   The key is a function that retrieves the items from the object.
#   Here we can use 'operator.itemgetter(idx)' or 'lambda record:record[idx]',
#   where 'idx' is the index of the column we want to use for sorting.



# ----------------- CUSTOM OBJECT: LIST OF CUSTOM CONTAINERS ------------------

mt.sectprint("LIST OF CUSTOM CONTAINERS")


class Entry:

    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return "{}: {}$ x {}".format(
                self.item, self.price, self.quantity)


purchase = [ # List of Entry object
    Entry("hammer", 10, 1),
    Entry("nail", 0.1, 50),
    Entry("saw", 30, 1),
    Entry("brush", 5, 2),
    Entry("paint", 30, 3)
]


# >> SORT WITH ONE KEY:
mt.stepprint("SORT WITH ONE KEY")

print("Original state:")
print(purchase)

print("Standard sorting:")
try:
    print(sorted(purchase))
except TypeError as err:
    print("ERROR:", err)

print("Sorting using attribute 'item' as key (attrgetter):")
print(sorted(purchase, key=operator.attrgetter("item")))

print("Sorting using attribute 'price' as key (lambda):")
print(sorted(purchase, key=lambda entry:entry.price))


# >> SORT WITH MULTIPLE KEYS:
mt.stepprint("SORT WITH MULTIPLE KEYS")

print("Original state:")
print(purchase)

print("Sorting (attrgetter):") # List keys by descending order of importance
print(sorted(purchase, key=operator.attrgetter("price", "quantity")))

print("Sorting (lambda):") # Process keys by ascending order of importance
print(sorted(sorted(purchase, key=lambda entry:entry.quantity), 
    key=lambda entry:entry.price))



# CONCLUSIONS:
# - Custom objects do NOT have a default sorting method (the __lt__ method
#   must be defined).
# - The sorting key may be defined with optional argument 'key=...'.
#   Here we can use 'lambda obj:obj.attr' or 'operator.attrgetter(attr)', 
#   provided attribute attr does have a default sorting method.
# - Sorting multiple keys is straightforward with operator.attrgetter, but for
#   mixed orders sorting we have to chain one-key sorts.



#%% =========================== ADVANCED SORTING ==============================

# We may also sort by ascending order of images by given lambda function.
# Here let us try with x -> 1/x.

mt.headprint("ADVANCED SORTING")

num_list = [56, -7, 93.44, 93.23, -42]

print("Original state:", num_list)
print("Output of sorted(list) ; key x:1/x :", sorted(num_list, key=lambda x:1/x))