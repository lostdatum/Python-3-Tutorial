# =============================================================================
#                                HANDLING FILES
# =============================================================================


# This tutorial is about handling files. We will cover the basics, and get a
# look at object serialization with module 'pickle'.


#%% ============================ CLASSICAL HANDLING ===========================


import misctest as mt  # custom functions to make tests easier


mt.headprint("CLASSICAL FILE HANDLING")

print("Writing to file 'txtfile1'...")
myfile = open("txtfile1", "w")
myfile.write("This is a test.")
myfile.close()

print("Reading file 'txtfile1'...")
myfile = open("txtfile1", "r")
mycontent = myfile.read()
myfile.close()
print("Read content:", repr(mycontent))

# CONCLUSIONS:
# 1/ Files opened in 'w' or 'r' mode have type '_io.TextIOWrapper'.
# 2/ We need to remember to close the file after using it.


#%% ========================== CONTEXTUAL HANDLING ============================

mt.headprint("CONTEXTUAL FILE HANDLING")

print("Writing to file 'txtfile2'...")
with open("txtfile2", "w") as myfile: # keyword 'with' creates a context
    myfile.write("This is also a test.")
    # File automatically closes here (even if an exception occurs before)

print("Reading file 'txtfile2'...")
with open("txtfile2", "r") as myfile: # 'myfile' is <class '_io.TextIOWrapper'>
    mycontent = myfile.read()
    # File automatically closes here (even if an exception occurs before)
print("Read content:", repr(mycontent))

# CONCLUSIONS:
# 1/ The context is created with syntax 'with ... as ...'.
# 2/ We do NOT need to remember to close the file after using it, this is handled
#    inside the context.


#%% ========================== MODES 'w+' AND 'a+' ============================

mt.headprint("MODES 'w+' AND 'a+'")

mt.stepprint("Opening file in mode 'w+' mode")
with open("textfile3", "w+") as myfile: 
    print("Writing to file 'textfile3'...")
    myfile.write("Another test!")
    print("Reading file 'textfile3'...")
    mycontent = myfile.read()
print("Read content:", repr(mycontent))

mt.stepprint("Opening file in 'a+' mode")
with open("textfile3", "a+") as myfile:
    print("Writing to file 'textfile3'...")
    myfile.write(" ... Still nothing?")
    print("Reading file 'textfile3'...")
    mycontent = myfile.read()
print("Read content:", repr(mycontent))

mt.stepprint("Opening file in 'a+' mode")
with open("textfile3", "a+") as myfile:
    print("Writing to file 'textfile3'...")
    myfile.write(" ... And now?")
    print("REWINDING file 'textfile3'...")
    myfile.seek(0) # moving file pointer to the beginning of file
    print("Reading file 'textfile3'...")
    mycontent = myfile.read()
print("Read content:", repr(mycontent))


# CONCLUSIONS:
# 1/ Files opened in 'w+' or 'a+' mode also have type '_io.TextIOWrapper'.
# 2/ In 'w' and 'w+' modes, the file pointer will be positionned at EOF
#    at first (as file is empty), and after any write operation.
# 3/ In 'a' and 'a+' modes, the file pointer will be positionned at EOF
#    at first (to append), and after any write operation.
# 4/ Both in 'w+' and 'a+' modes, the file pointer must be moved with seek()
#    in order to be able to read anything from the stream.


#%% =========================== SERIALIZE OBJECTS =============================

# Serializz: translate a data structure or object into a format that can be
#            stored or transmitted, and reconstructed later.
# Python module 'pickle' allows to serialize objects in binary files.
# We are going to try it on a simple 'dict' object.


import pickle


mt.headprint("SERIALIZE OBJECTS")

score = {"player1":5 , "player2":35 , "player3":20 , "player4":2}
mt.stepprint("Data to be stored:")
print(score)

mt.stepprint("Open 'picklefile' in 'wb' mode")
with open("picklefile", "wb") as myfile:
    print("Creating Pickler...")
    mypickler = pickle.Pickler(myfile)
    print("Dumping data in Pickler...")
    mypickler.dump(score)

mt.stepprint("Open 'picklefile' in 'rb' mode")
with open("picklefile", "rb") as myfile:
    print("Creating Unpickler...")
    myunpickler = pickle.Unpickler(myfile)
    print("Loading data from Unpickler...")
    data = myunpickler.load()

mt.stepprint("Read data:")
print(data)


# CONCLUSIONS:
# 1/ Binary file opened in 'wb' or 'rb' mode have type '_io.BufferedReader'.
# 2/ We need to create Picker and Unpickler objects to configure the
#    serialization protocol before we can dump or load objects.