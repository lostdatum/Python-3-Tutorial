# =============================================================================
#                                TEST FUNCTIONS
# =============================================================================


# --------------------------------- FUNCTIONS ---------------------------------


def stepprint(string):
    """Prints string formatting it as a test step."""

    print("\n>> " + string + ":\n")



def sectprint(string):
    """Prints string formatting it as a section title."""

    print("\n" + (" " + string + " ").center(80, "-") + "\n")



def headprint(string):
    """Prints string formatting it as a header."""

    print("\n\n" + (" " + string + " ").center(80, "=") + "\n")



def dictprint(dictionary):
    """Prints dictionary with improved readability."""

    for (key, value) in dictionary.items():
        print("{}: {}".format(repr(key), repr(value)))



def instprint(inst):
    """Standardized instance printer. Independant from instance methods."""

    formstr = "Instance (ID={}) of {} has attributes:"
    print(formstr.format(hex(id(inst)), type(inst)))
    dictprint(vars(inst))



def classname(obj):
    """Returns name of object's class as string."""

    return type(obj).__name__



def clsmembers(cls, include=[], exclude=[]):
    """
    Returns class members as dictionary, optionally filtering special (and
    mangled) members or/and methods.

    Optional arguments:

        include: List which should contain 1 or 2 string keywords. Supported
                keywords are: 'special', 'non-special', 'method', 'non-method'.
                Each keyword is a constraint for including an attribute.
                If two keywords are given, then the attribute must meet both
                constraints at the same time (logical AND) to be included.

        exclude: Works as described above, except that when constraints are
                met, then the attribute is excluded.

    NB: Only one of the optional arguments may be used at a time.
    """
    
    # List of supported options
    OPTIONS = ['special', 'non-special', 'method', 'non-method']

    # Get all members
    allmembers = vars(cls).items()
   
    # Check optional arguments
    if include and exclude:
        raise AttributeError("cannot both include and exclude")
    elif include: # inclusion mode
        mustbe = dict.fromkeys(OPTIONS, False)
        if len(include) > 2:
            raise AttributeError("too many constraints (maximum 2)")
        for option in include:
            if option not in OPTIONS:
                raise ValueError("invalid constraint '{}'".format(option))
            mustbe[option] = True
    elif exclude: # exclusion mode
        mustnotbe = dict.fromkeys(OPTIONS, False)
        if len(exclude) > 2:
            raise AttributeError("too many constraints (maximum 2)")
        for option in exclude:
            if option not in OPTIONS:
                raise ValueError("invalid constraint '{}'".format(option))
            mustnotbe[option] = True
    else: # no filtering
        return allmembers

    # Filter and print
    members = {}
    for (attr, value) in allmembers:

        isspecial = attr.startswith("__")
        ismethod = callable(getattr(cls, attr))
        
        if include: # inclusion mode
            if len(include) == 1:
                
                isincluded = (mustbe['special'] and isspecial
                            or mustbe['non-special'] and not isspecial
                            or mustbe['method'] and ismethod
                            or mustbe['non-method'] and not ismethod)

            elif len(include) == 2:

                isincluded = ((mustbe['non-special'] and mustbe['non-method']
                                and not isspecial and not ismethod)
                            or (mustbe['non-special'] and mustbe['method']
                                and not isspecial and ismethod)
                            or (mustbe['special'] and mustbe['non-method']
                                and isspecial and not ismethod)
                            or (mustbe['special'] and mustbe['method']
                                and isspecial and ismethod))

            if isincluded:
                members[attr] = value

        elif exclude: # exclusion mode

            if len(exclude) == 1:
                
                isexcluded = (mustnotbe['special'] and isspecial
                            or mustnotbe['non-special'] and not isspecial
                            or mustnotbe['method'] and ismethod
                            or mustnotbe['non-method'] and not ismethod)

            elif len(exclude) == 2:

                isexcluded = ((mustnotbe['non-special'] and mustnotbe['non-method']
                                    and (not isspecial and not ismethod))
                                or (mustnotbe['non-special'] and mustnotbe['method']
                                    and (not isspecial and ismethod))
                                or (mustnotbe['special'] and mustnotbe['non-method']
                                    and (isspecial and not ismethod))
                                or (mustnotbe['special'] and mustnotbe['method']
                                    and (isspecial and ismethod)))

            if not isexcluded:
                members[attr] = value  

    return members




def clsprint(cls, include=[], exclude=[]):
    """Prints class members, optionnally excluding
    mangled and special members or/and methods."""
    
    members = clsmembers(cls, include, exclude)
    if include: 
        formstr = "Members of class '{}' including INTER{}:"
        print(formstr.format(cls.__name__, include))
    elif exclude:
        formstr = "Members of class '{}' excluding INTER{}:"
        print(formstr.format(cls.__name__, exclude))

    dictprint(members)





# ----------------------------------- TESTS -----------------------------------


def test_clsmembers():
    test_clsprint()


def test_clsprint():
    clsprint(list, include=['special'])
    print()
    clsprint(list, include=['method'])
    print()
    clsprint(list, include=['special', 'non-method'])
    print()
    clsprint(list, include=['non-special', 'method'])
    print()
    clsprint(list, exclude=['non-special'])
    print()
    clsprint(list, exclude=['special', 'method'])
    print()