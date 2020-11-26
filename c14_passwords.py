# =============================================================================
#                              MANAGING PASSWORDS
# =============================================================================


# This tutorial is about managing passwords. We will prompt user to enter their
# password and store it safely.


import getpass # to get user input without displaying it
import hashlib # to hash passwords
import pickle # to serialize the hash in a file

import misctest as mt  # custom functions to make tests easier


#%% ----------------------------- DEFINE PASSWORD -----------------------------

mt.sectprint("DEFINE PASSWORD")


mt.stepprint("Choose new password")
pwd_str = getpass.getpass("Enter new password: ")

mt.stepprint("Hash password (with SHA3-256)")
pwd_bytes = pwd_str.encode()
pwd_hash = hashlib.sha3_256(pwd_bytes).hexdigest()
print("Hash:", pwd_hash)

# NB 1: The hashing technique used here is a simple example, as this tutorial
# is not about cryptography, but be aware that it is not really secure.
# See: https://docs.python.org/3/library/hashlib.html#key-derivation.

mt.stepprint("Save hash")
with open('pwdfile', 'wb') as myfile:
    pickler = pickle.Pickler(myfile)
    pickler.dump(pwd_hash)

# NB 2: We could save the password as a string in a text file, instead of
# of serializing it in a binary file.


#%% ------------------------------ CHECK PASSWORD -----------------------------

mt.sectprint("CHECK PASSWORD")

MAX_ATTEMPTS = 3
attempts = MAX_ATTEMPTS

while True:

    mt.stepprint("Enter password")
    pwd_str = getpass.getpass("Enter your password: ")

    mt.stepprint("Hash password (with SHA3-256)")
    pwd_bytes = pwd_str.encode()
    pwd_hash = hashlib.sha3_256(pwd_bytes).hexdigest()
    print("Hash:", pwd_hash)

    mt.stepprint("Compare to saved hash")

    with open('pwdfile', 'rb') as myfile:
        unpickler = pickle.Unpickler(myfile)
        hash_saved = unpickler.load()

    if pwd_hash == hash_saved:
        print("Correct password. Access granted.")
        break
    else:
        print("Wrong password. Access denied.")
        attempts -= 1
        if attempts > 0:
            print("You have {} attempts left.".format(attempts))
        else:
            print("Too many failed attempts. Access is now locked down.")
            break