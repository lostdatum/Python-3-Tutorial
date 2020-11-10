# =============================================================================
#                           ITERATORS & GENERATORS
# =============================================================================

# This tutorial is about iterators and generators. These are classes of objects
# which are used to iterate through sequence-like container objects (such as
# lists or dictionaries) using FOR ... IN ... loops.


import misctest as mt # custom functions to make tests easier


#%% =========================== ITERATORS: LISTS ==============================


mt.headprint("ITERATORS: LISTS")

mylist = ["Mark", "Roger", "Sally", "Kate"]
print("List:")
print(mylist)

mt.stepprint("Iteration through list (default):")
for elt in mylist:
    print(elt)

mt.stepprint("Iteration through enumerate(list):")
for (idx, elt) in enumerate(mylist):
    print("({}, {})".format(idx, elt))



#%% ======================== ITERATORS: DICTIONARIES ==========================


mt.headprint("ITERATORS: DICTIONARIES")

mydict = {"Simpson":500, "Jones":300, "Smith":1000}
print("Dictionary:")
mt.dictprint(mydict)

mt.stepprint("Iteration through dictionary (default)")
for key in mydict:
    print(key)

mt.stepprint("Iteration through dictionary keys")
for key in mydict.keys():
    print(key)

mt.stepprint("Iteration through dictionary values")
for value in mydict.values():
    print(value)

mt.stepprint("Iteration through dictionary items")
for item in mydict.items():
    print(item)



#%% =========================== ITERATORS: CUSTOM =============================


# -------------------------------- DEFINITIONS --------------------------------

class Vehicule:
    """Base class for all types of vehicules."""

    def __init__(self, vehicule_id, passengers_nb=0):
        self._vehicule_id = vehicule_id # serial number of the equipment
        self._passengers_nb = passengers_nb # number of passengers onboard



class Wagon(Vehicule):
    """Element in the Train container class. Inherits from class Vehicule."""

    def __repr__(self):
        return "Wagon #{} carrying {} passengers.".format(
                self._vehicule_id, self._passengers_nb)



class Train(Vehicule):
    """Container class to be iterated through. Inherits from class Vehicule."""

    def __init__(self, vehicule_id, *wagons_list):
        self._vehicule_id = vehicule_id
        self._wagons_list = list(wagons_list)
        self._wagons_nb = len(self._wagons_list) # number of wagons
        self._passengers_nb = sum(wagon._passengers_nb 
                                  for wagon in self._wagons_list) # using generator

    def __repr__(self):
        return "Train #{} composed of {} wagons carrying {} passengers total.".format(
                self._vehicule_id, self._wagons_nb, self._passengers_nb)

    def __iter__(self):
        return TrainIterator(self) # simply return an Train-iterator object
    
    def add_wagon(self, new_wagon): # just to flesh it out
        self._wagons_list.append(new_wagon)
        self._wagons_nb += 1
        self._passengers_nb += new_wagon._passengers_nb



class TrainIterator:
    """Train-iterator class to iterate through Train objects."""

    def __init__(self, train):
        """Iterator constuctor. To store data needed to iterate."""

        self._wagons_list = train._wagons_list # copy of object data we want to access
        self._wagons_nb = train._wagons_nb # information used to stop iteration
        self._wagon_idx = 0 # current element

    def __next__(self):
        """Iterator incrementation process and stopping condition."""

        if self._wagon_idx == self._wagons_nb: 
            raise StopIteration # Stops immediately
        else:
            self._wagon_idx += 1 # Next index
            return self._wagons_list[self._wagon_idx-1] # Next wagon



# -------------------------------- TEST SCRIPT --------------------------------

mt.headprint("ITERATORS: CUSTOM")

# Create Train object
train = Train(8567, Wagon(678, 20), Wagon(342, 40))
train.add_wagon(Wagon(832, 15))
print(train)

# Iterate through a Train object - How it's done under the hood
mt.stepprint("Iteration through Train object (hard way)")
for idx in [0, 1, 2]:
    train_iter = iter(train)
    print(train_iter._wagons_list[idx])
    try:
        next(train_iter)
    except StopIteration:
        pass

# Iterate through a Train object - How it's meant to be done
mt.stepprint("Iteration through Train object (easy way)")
for wagon in train:
    print(wagon)



#%% =========================== GENERATORS: RANGE =============================


mt.headprint("GENERATORS: RANGE")

(a, b) = (4, 10)

mt.stepprint("Iterating through generator 'range({})'".format(b))
for k in range(b): # starts at 0, stops at b-1
    print("{}\t".format(k), end="")
print("\n")

mt.stepprint("Iterating through generator 'range({}, {})'".format(a, b))
for k in range(a, b): # starts at a, stops at b-1
    print(k, "\t", end="")
print("\n")



#%% ================== GENERATORS: ITEM-WISE PROCESSING #1 ====================


mt.headprint("GENERATORS: ITEM-WISE PROCESSING #1")

mylist = [("lemon", 10), ("apple", 4), ("orange", 7), ("cherry", 16)]
print("Original list:\n", mylist)

mt.stepprint("Using syntax 'f(item) for item in mylist'")
mygen = ((price, fruit) for (fruit, price) in mylist)
print(mygen)
mt.stepprint("Reordered list (casting generator into list)")
print(list(mygen))


#%% ================== GENERATORS: ITEM-WISE PROCESSING #2 ====================


mt.headprint("GENERATORS: ITEM-WISE PROCESSING #2")

scores_1 = {"John": 600, "Bob": -200, "Terry": 500}
scores_2 = {"John": 400, "Bob": -300, "Terry": 1000}
scores_3 = {"John": -700, "Bob": 400, "Terry": -100}

scoreboard = [scores_1, scores_2, scores_3]

mt.stepprint("Scoreboard")
for line in scoreboard:
    print(line)
list_of_John_scores = [score["John"] for score in scoreboard]
step = "John's scores (using syntax 'record[key] for record in scoreboard')"
mt.stepprint(step)
print(list_of_John_scores)
mt.stepprint("John's total score (summing them)")
print(sum(list_of_John_scores))



#%% =========================== CUSTOM GENERATORS =============================

# -------------------------------- DEFINITIONS --------------------------------


def interval(lower, upper, step=1):
    """Generator to emulate intervals."""

    if lower > upper:
        raise ValueError("Upper bound must be higher than lower bound.")

    val = lower
    while val <= upper:
        yield val # use of "yield" keyword casts function as generator object
        val += step


# -------------------------------- TEST SCRIPT --------------------------------

mt.headprint("GENERATORS: CUSTOM")

(a, b, d) = (-3, 7, 2)

formstr = "Iterating though custom generator 'interval({}, {}, {})'"
mt.stepprint(formstr.format(a, b, d))
for x in interval(a, b, d):
    print(x, "\t", end="")
print("\n")