# =============================================================================
#                        OVERLOADING & VARIABLE ARGUMENTS
# =============================================================================

# This tutorial is about implementing one method in one class which can
# process multiple sets of arguments to achieve the same purpose.
# In some other languages, this may be achieved is through function/method 
# overloading. In C++, for example, the same function name may have multiple 
# definitions and the language identifies the one to use by checking the number
# and types of passed arguments (the fuction/method "signature").
# This functionnality is not supported by default in Python, as multiple 
# definitions will just override the previous ones.
# However we will see here how to achieve similar results.


# NOTES: 
# - Basicly, the only case we want two functions/methods to have the same name
#   is when they have the same purpose (to achieve polymorphism).
# - Method overloading is different from having two methods with the same name 
#   but which are from different classes (or namespaces). For example, the 
#   __len__ method is defined differently inside each container class.


# -------------------------------- DEFINITIONS --------------------------------


# import overloading


class Duration:
    """Represents durations in H:M:S format."""
    

    def initialize_1(self, hours, mins=None, secs=None): # WITH OPTIONAL ARGUMENTS
        """Initializes Duration instance. Must be able to process either integer
        H:M:S format or decimal number of hours as inputs. Implementation #1."""

        if mins or secs: # H:M:S format

            if (not isinstance(hours, int) # check type
                    or isinstance(hours, bool)):
                msg = "arguments must be integers to use H:M:S format"
                raise TypeError(msg)
            self._hours = hours
        
            if mins:

                if (not isinstance(mins, int) # check type
                        or isinstance(mins, bool)):
                    msg = "arguments must be integers to use H:M:S format"
                    raise TypeError(msg)
                self._mins = mins
            
            else:

                self._mins = 0

            if secs:

                if (not isinstance(secs, int) # check type
                        or isinstance(secs, bool)):
                    msg = "arguments must be integers to use H:M:S format"
                    raise TypeError(msg)
                self._secs = secs
            
            else:

                self._secs = 0

        else: # decimal format

            if (not isinstance(hours, (int, float)) # check type
                    or isinstance(hours, bool)):
                msg = "argument must be a real number to use decimal format"
                raise TypeError(msg) 
            (self._hours, self._mins, self._secs) = self.dec2hms(hours)



    def initialize_2(self, *args): # WITH VARIABLE LENGTH ARGUMENT
        """Initializes Duration instance. Must be able to process either integer
        H:M:S format or decimal number of hours as inputs. Implementation #2."""

        # Create canvas
        self._hours = None
        self._mins = None
        self._secs = None

        # Parse arguments
        if len(args) > 3:

            raise TypeError("expected 1 to 3 arguments")
        
        elif len(args) > 1: # H:M:S format

            for (idx, field) in enumerate(vars(self)):
                
                if idx < len(args): # argument was provided

                    if (not isinstance(args[idx], int) # check type
                            or isinstance(args[idx], bool)):
                        msg = "arguments must be integers to use H:M:S format"
                        raise TypeError(msg)
                    vars(self)[field] = args[idx] # self.field does not work,
                                                  # as field is a string
                
                else:

                    vars(self)[field] = 0
            
        elif len(args) > 0: # decimal duration (in hours)

            if (not isinstance(args[0], (int, float)) # check type
                    or isinstance(args[0], bool)):
                msg = "argument must be a real number to use decimal format"
                raise TypeError(msg)
            (self._hours, self._mins, self._secs) = self.dec2hms(args[0])


    
    # @overloading
    # def initialize_3(self, hours): # WITH OVERLOADING
    #     pass



    def __repr__(self):
        """Returns string representation of calling Duration instance."""

        formstr = "{:02}:{:02}:{:02}"
        return formstr.format(self._hours, self._mins, self._secs)



    @staticmethod
    def dec2hms(number):
        """Converts decimal number of hours to Duration object."""

        if (not isinstance(number, (int, float)) # check type
                or isinstance(number, bool)):
                raise TypeError("argument must be a decimal number")
        
        # Handle sign separately
        if number < 0:
            sign = -1
            number = -number
        else:
            sign = 1
            
        # Compute (% and // operators expect positive numbers)
        hours = sign * round(number // 1)
        mins = sign * round(((number % 1) * 60) // 1)
        secs = sign * round((((number % 1) * 60) % 1) * 60)

        return (hours, mins, secs)



    def hms2dec(self):
        """Converts Duration object to decimal number of hours."""

        return (self._hours + self._mins/60 + self._secs/3600)



   
	
	
	
# -------------------------------- TEST SCRIPT --------------------------------


import misctest as mt


duration_1 = Duration()
duration_2 = Duration()
decimal_1 = 13.25
decimal_2 = 2.425

mt.headprint("Implementation #1")
duration_1.initialize_1(decimal_1)

print(Duration.dec2hms(decimal_2))

duration_2.initialize_1(*Duration.dec2hms(decimal_2))
print("TIME\tHOURS\tHH:MM:SS")
print("duration_1\t{}\t{}".format(decimal_1, duration_1))
print("duration_2\t{}\t{}".format(decimal_2, duration_2))

mt.headprint("Implementation #2")
duration_1.initialize_2(decimal_1)
duration_2.initialize_2(*Duration.dec2hms(decimal_2))
print("TIME\tHOURS\tHH:MM:SS")
print("duration_1\t{}\t{}".format(decimal_1, duration_1))
print("duration_2\t{}\t{}".format(decimal_2, duration_2))