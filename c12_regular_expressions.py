# =============================================================================
#                              REGULAR EXPRESSIONS
# =============================================================================

# This tutorial is about using module 're' to search for regular expressions in
# strings or files.


import re # see https://docs.python.org/3/library/re.html

import misctest as mt # custom functions to make tests easier



# REGEX CODING:
# -------------
# Control characters: ^ $ . * + ? \ ( ) [ ] { } |
# And also depending on context: - < = !
#  
# r".." : Declares string '..' as regex.
#         Escapes usual control characters (e.g. "\n").
#
# ^.. : Start of string '..'. Declare exception set.
# ..$ : End of string '..'
# _* : Any number of occurences (0, 1, 2, ...) of previous character '_'
# _+ : At least one occurence (1, 2, ...) of previous character '_'.
# _? : At most one occurence (0 or 1) of previous character '_'
#      If used after {*, +, ?}, matches in a non-greedy (minimal) mode
# \_ : Escape sequence for control character '_' (e.g. "\.", "\(")
# _{n} : Exactly 'n' occurences of previous character '_'
# _{n, m} : From 'n' to 'm' occurences (inclusive) of previous character '_'
# . : Any character (wildcard) except '\n'
# [aZf] : Any letter in case-sensitive set {'a', 'Z', 'f'}
# [^aZf] : Any letter NOT in case-sensitive set {'a', 'Z', 'f'}. 
#          The '^' has to be in first position.
# [F-P] : Any letter in case-sensitive interval [F,P]
# [0-7] : Any decimal digit interval [0,7]
# \w : Any alphanumerical character or underscore '_'.
# \W : Any character EXCEPT alphanumerical characters and underscore '_'.
# \s : Any whitespace character (e.g. ' ', '\t', '\n').
# \S : Any character EXCEPT whitespace characters.
# (..)_ : Set '..' as numbered group. Apply next operator '_' to group.
# \g<num>: Back reference to numbered group (short version: \num).
# \g<name> : Back reference to named group.
# (?__..) : Extension notation. Various effects on '..' depending on control
#           characters '__'. Usual supported extensions are:
#           ?P<name>.. : named group '..'
#           ?P=name : reference to previously named group
#           And also: ?:, ?=, ?!, ?<=, ?<!
# ..|... : Match expression '..' OR expression '...'




#%% ============================= MATCH OBJECTS ===============================

mt.headprint("MATCH OBJECTS")

mt.stepprint("Text")
TEXT = ("If this lady weighs the same as a duck, then she is made of wood," 
       + "and therefore... she is a witch!")
print(repr(TEXT))

mt.stepprint("Regular expression")
regex = r"then (\w*)( \w*)*[.,;]"
    # EXPLANATION:
    # Prefix 'r' makes it a regex.
    # Pattern '\w*' matches any alphanumeric word (spaces excluded).
    # Matches 'then', followed by any number of words, followed by punctuation.
    # Makes two numbered groups, marked by pairs of brackets '()'.
print(repr(regex))

# Let us look for a match using re.search()
mo = re.search(regex, TEXT) # this is a Match Object

# Using Match Objects
mt.stepprint("Basic Match information")
print("Match found:", bool(mo)) # checks if 'mo' is not 'None'
print("Match content: '{}'".format(mo.group(0))) # returns matched string
    # NB: mo.group(0) is the whole matched string
print("Match (start, end) positions in string:", mo.span(0))

mt.stepprint("Groups matched")
for idx in range(1, len(mo.groups())+1):
    print("Group #{}: '{}'".format(idx, mo.group(idx)))
        # NB: mo.groups() is the list of all groups (plus the whole match at 
        # index #0) and mo.group(idx) returns the same as mo.groups()[idx].
        # NB: pattern '( \w*)*' has saved only last word.
        
mt.stepprint("Use groups with backreferences")
print("'{}'".format(mo.expand(r"\g<1> loves\g<2>")))
    # NB: The '\\g<num>' pattern references numbered group #num.



#%% ========================= FIRST MATCH IN STRING ===========================


mt.headprint("FIRST MATCH IN STRING")


TESTS = ["Be quiet!", "Be quiet, you chatterbox!", "I said be quiet, kid!"]


# First part
regex = r"[bB]e quiet!?"
mt.sectprint("Regular expression = '{}'".format(regex))

mt.stepprint("Using SEARCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.search(regex, stg))))

mt.stepprint("Using MATCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.match(regex, stg))))

mt.stepprint("Using FULLMATCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.fullmatch(regex, stg))))


# Second part
regex = r"^[bB]e quiet!?"
mt.sectprint("Regular expression = '{}'".format(regex))

mt.stepprint("Using SEARCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.search(regex, stg))))

mt.stepprint("Using MATCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.match(regex, stg))))

mt.stepprint("Using FULLMATCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.fullmatch(regex, stg))))


# Third part
regex = r"^[bB]e quiet!?$"
mt.sectprint("Regular expression = '{}'".format(regex))

mt.stepprint("Using SEARCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.search(regex, stg))))

mt.stepprint("Using MATCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.match(regex, stg))))

mt.stepprint("Using FULLMATCH")
for stg in TESTS:
    print("Match in '{}': {}".format(stg, bool(re.fullmatch(regex, stg))))




# CONCLUSIONS:
#   - search: finds first substring, starting ANYWHERE in 'string', which
#     matches regex 'pattern'.
#   - match: finds first substring, starting at BEGINNING of 'string', which
#     matches regex 'pattern'. It is like searching for ('^' + regex).
#   - fullmatch: finds if whole string matches regex 'pattern'. It is like
#     searching for ('^' + regex + '$').


#%% =========================== MULTIPLE MATCHES ==============================

mt.headprint("MULTIPLE MATCHES")

mt.stepprint("Text")
TEXT = ("Fear leads to anger; anger leads to hatred; hatred leads to conflict;"
       + " conflict leads to suffering.")
print(repr(TEXT))

mt.stepprint("Find all matches")
regex = r"\w* leads to \w*"
print("Regular expression: {}".format(repr(regex)))
matches = re.findall(regex, TEXT)
delimiters = re.split(regex, TEXT)
print("Matches:", matches)
print("Delimiters:", delimiters)

mt.stepprint("Find all matches and extract substring")
regex = r"(\w*) leads to \w*" # one numbered group
print("Regular expression: {}".format(repr(regex)))
matches = re.findall(regex, TEXT)
print("Matches:", matches)
print("Summary:", repr(" implies ".join(matches) + '.'))



#%% ============================= SUBSTITUTION ================================

# Syntax: re.sub(pattern, repl, string, count, flags)
# Returns the string obtained by replacing all matches of regex 'pattern' in
# 'string' by string 'repl', or by the output of function 'repl' (which takes
# only one Match Object as argument).

mt.headprint("SUBSTITUTION")

mt.stepprint("Original text")
TEXT = ("They were close. We were sitting ducks. We had to find a way to duck"
       + " and dive this. As we kept ducking in the duct, Alice said: 'Let's"
       + " not be lame ducks. If it looks like a duck, swims like a duck, and"
       + " quacks like a duck, then it probably is a duck.'.")
print(repr(TEXT))

# In the Unitef Kingfom, words containing "duck" are considered swearwords.
# We do not want to offend anyone, so let us redact 'duck' compound words.

mt.stepprint("Regular expression")
regex = r"(duck[a-z]*)([ .,])"
print(repr(regex))

mt.stepprint("Redacted text")
repl = lambda mo: "*"*len(mo.group(1)) + mo.group(2)
    # mo.group(1) is the compound word to be redacted and mo.group(2) is
    # space or punctuation
redacted = re.sub(regex, repl, TEXT)
print(repr(redacted))



#%% ============================ COMPILED REGEX ===============================

mt.headprint("COMPILED REGEX")

mt.stepprint("Text")
TEXT = ("We shall fight on the beaches, we shall fight on the landing grounds,"
       + " we shall fight in the fields and in the streets, we shall fight in"
       + " the hills. We shall never surrender!")
print(repr(TEXT))

mt.stepprint("Regular expression")
regex = r"(fight) (?P<place>\w* \w* \w*)"
print(repr(regex))
repl = r"HAVE TEA \g<place>" # uses backreference to named group

# Compile
reo = re.compile(regex) # this is a Regular Expression Object

# Testing
mt.stepprint("Test Regular Expression Object methods")
print("SEARCH:", repr(reo.search(TEXT).group(0)))
print("\nFINDALL:", repr(reo.findall(TEXT)))
print("\nSUB:", repr(reo.sub(repl, TEXT)))


#%% ============================= APPLICATIONS ================================

mt.headprint("APPLICATIONS")

# ----------------------------- CHECK STRING FORMAT ---------------------------

mt.sectprint("CHECK STRING FORMAT")

# Let us check whether string is a mobile phone number (French format).

TESTS = ["07 63 82 96 09", "06.63.82.96.09", "07-63-82-96-09", "+33763829609",
        "+33 6 63 82 96 09", "0959538523", "065953852", "06595385234"]

mt.stepprint("Regular expression")
regex = r"(0|\+33 ?)[67](( ?[0-9]{2}){4}|(\.?[0-9]{2}){4}|(\-?[0-9]{2}){4})"
# EXPLANATION:
# Start followed by '0' OR '+33' (or '+33 '), followed by 6 or 7.
# Then this pattern : 
#       any separator in set {' ', '.', '-'}, followed by 2 numbers...
# ...repeated 4 more times.
print(repr(regex))

mt.stepprint("Checking whether string is mobile phone number")
reo = re.compile(regex) # compile before using inside loop
for stg in TESTS:
    print("'{}': {}".format(stg, bool(reo.fullmatch(stg))))


# ------------------------------ PARSE CSV FILE -------------------------------

mt.sectprint("PARSE CSV FILE")

mt.stepprint("File content")
FILE = ("Alice, Wonders, 7, female\n"
       + "Bob, Sponge, 13, male\n"
       + "Charlie, Bucket, 11, male")
print(repr(FILE))

mt.stepprint("Regular expression")
regex = (r"(?P<FirstName>[A-Z][a-z]+), ?(?P<LastName>[A-Z][a-z]+), ?"
        + r"(?P<Age>[0-9]+), ?(?P<Gender>[A-Za-z]+)") # pattern for one line
print(repr(regex))

matches = re.finditer(regex, FILE) 
    # NB: Variant of re.findall(). Returns all matches as iterator object.

for (idx, mo) in enumerate(matches):
    mt.stepprint("Match #{}".format(idx+1))
    mt.dictprint(mo.groupdict())