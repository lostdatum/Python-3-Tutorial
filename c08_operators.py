# =============================================================================
#                             REDEFINING OPERATORS
# =============================================================================

# This tutorial is about redefining usual operators (like +, -, *, <, etc.) for 
# custom classes. 
# NB: This is called operator overloading in some other languages (e.g. C++).

# -------------------------------- DEFINITIONS --------------------------------


class Time:
    """ Represents times and durations in H:M:S format."""


    def __init_0(self, hours, mins=None, secs=None):
        """Creates Time instance."""

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



    def __init__(self, *args):
        """Creates Time instance."""

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
            
        elif len(args) > 0: # decimal time (in hours)

            if (not isinstance(args[0], (int, float)) # check type
                    or isinstance(args[0], bool)):
                msg = "argument must be a real number to use decimal format"
                raise TypeError(msg)
            (self._hours, self._mins, self._secs) = self.dec2hms(args[0])



    def __repr__(self):
        """Returns string representation of calling Time instance."""

        formstr = "{:02}:{:02}:{:02}"
        return formstr.format(self._hours, self._mins, self._secs)



    @staticmethod
    def dec2hms(number):
        """Converts decimal time (in hours) to Time object."""

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
        """Converts Time object to decimal time."""

        return (self._hours + self._mins/60 + self._secs/3600)



    def __add__(self, decimal):
        """Adds given decimal time to calling Time instance."""
        # Called by 'instance + decimal', which is equivalent under
        # the hood to 'instance.__add__(decimal)'.

        if (not isinstance(decimal, (int, float)) # check type
                or isinstance(decimal, bool)):
                raise TypeError("operand must be a decimal number")
        
        # Conversion
        time = type(self)(*self.dec2hms(decimal))
            # type(self) gives class, then it can be used to call initializer
        
        # Computation (easier with decimal times, but this is fun)
        total_secs = self._secs + time._secs
        secs = total_secs % 60

        total_mins = self._mins + time._mins + total_secs//60
        mins = total_mins % 60

        hours = self._hours + time._hours + total_mins//60

        return type(self)(hours, mins, secs)
    


    def __radd__(self, decimal):
        """Adds calling Time instance to given Time instance."""
        # Called by 'decimal + instance', which is equivalent under
        # the hood to 'instance.__iadd__(decimal)'.
        # As operator '+' is commutative, we can just use __add__ (it will also
        # handle the argument checks).

        return self + decimal # equivalent to calling 'self.__add__(decimal)'



    def __sub__(self, decimal):
        """Substracts given Time from calling Time instance."""
        # Called by 'instance - decimal', which is equivalent under
        # the hood to 'instance.__sub__(decimal)'.

        if (not isinstance(decimal, (int, float)) # check type
                or isinstance(decimal, bool)):
                raise TypeError("operand must be a decimal number")

        # Conversion
        time = type(self)(*self.dec2hms(decimal))
        
        # Computation (easier with decimal times, but this is fun)
        total_secs = self._secs - time._secs
        secs = total_secs % 60

        total_mins = self._mins - time._mins + total_secs//60
        mins = total_mins % 60

        hours = self._hours - time._hours + total_mins//60

        return type(self)(hours, mins, secs)



    def __rsub__(self, decimal):
        """Substracts calling Time instance from given Time instance."""
        # Called by 'decimal - instance', which is equivalent under
        # the hood to 'instance.__isub__(decimal)'.
        
        return (self - decimal) * (-1)
            # Equivalent to calling self.__sub__(decimal).__mul__(-1).
            # Even though operator '-' is not commutative, we can use a trick.



    def __mul__(self, decimal):
        """Multiplies calling Time instance by given decimal time."""

        if (not isinstance(decimal, (int, float)) # check type
                or isinstance(decimal, bool)):
                raise TypeError("operand must be a decimal number")
        
        # Computation (in decimal, its cheating, but you know...)
        product = self.hms2dec() * decimal

        return type(self)(product) # use initializer with decimal value



    def __rmul__(self, decimal):
        """Multiplies given decimal time by calling Time instance."""
        # Called by 'decimal * instance', which is equivalent under
        # the hood to 'instance.__rmul__(decimal)'.

        return self * decimal # equivalent to 'instance.__mul__(decimal)'
            # As operator '*' is commutative, we can just use __mul__.
            # It will also handle the argument checks.



    def __eq__(self, time):
        """Asserts whether calling Time instance is equal to
        given Time instance."""

        if not isinstance(time, type(self)): # check input
            raise TypeError("both operands must be Time objects")

        return (self._hours == time._hours      # This expression is evaluated
                and self._mins == time._mins    # as boolean (class 'bool').
                and self._secs == time._secs)   # Value is 'True' or 'False'.



    def __gt__(self, time):
        """Asserts whether calling Time instance is strictly greater than
        given Time instance."""

        if not isinstance(time, type(self)): # check input
            raise TypeError("both operands must be Time objects")

        return (self._hours > time._hours
                or (self._hours == time._hours and self._mins > time._mins)
                or (self._mins == time._mins and self._secs > time._secs))



    def __ge__(self, time):
        """Asserts whether calling Time instance is greater or equal to
        given Time instance."""

        if not isinstance(time, type(self)): # check input
            raise TypeError("both operands must be Time objects")

        return (self > time or self == time)
    

    # About comparison
    # ----------------
    # Python can infer __ne__, __lt__ and __le__ methods from previously
	# defined __eq__, __gt__ and __ge__ methods (or the other way around), so
    # we do not need to define them here.
	
	
	
# -------------------------------- TEST SCRIPT --------------------------------
time_1 = Time(13, 15)
dur_1 = time_1.hms2dec()
dur_2 = 2.425
time_2 = Time(dur_2)
print("TIME\tHOURS\tHH:MM:SS")
print("time_1\t{}\t{}".format(dur_1, time_1))
print("time_2\t{}\t{}".format(dur_2, time_2))
print("Addition: ", time_1 + dur_2)
print("Addition (reversed): ", dur_1 + time_2)
print("Subtraction: ", time_1 - dur_2)
print("Subtraction (reversed): ", dur_1 - time_2)
print("Multiplication x 2': ", time_1 * 2)
print("Multiplication x 2 (reversed): ", 2 * time_1)
print("Comparison 'time_1 == time_1: ", time_1 == time_1)
print("Comparison 'time_1 != time_1: ", time_1 != time_1)
print("Comparison 'time_1 >= time_1: ", time_1 >= time_1)
print("Comparison 'time_1 <= time_1: ", time_1 <= time_1)
print("Comparison 'time_1 >= time_2: ", time_1 >= time_2)
print("Comparison 'time_1 <= time_2: ", time_1 <= time_2)
