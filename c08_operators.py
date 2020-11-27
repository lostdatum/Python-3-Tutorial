# =============================================================================
#                             REDEFINING OPERATORS
# =============================================================================

# This tutorial is about redefining usual operators (like +, -, *, <, etc.) for 
# custom classes. NB: The equivalent in C++ is called operator overloading.
# In order to showcase more use cases, I decided that comparison operators 
# would be internal (both operands have the same type) and arithmetic operators
# would be external (the operands have different types).
# For example, Time objects in h:m:s format will be added to a time expressed
# a decimal number of hours (refered to as "decimal time" below). NB: from a
# practical point of view we should also be able to add two Time objects, but
# I want to keep this simple (and this class is not really useful anyway !).


# -------------------------------- DEFINITIONS --------------------------------


class Time:
    """ Represents times and durations in h:m:s format."""


    def __init__(self, hours, mins, secs):
        """Creates Time instance."""

        for arg in (hours, mins, secs):
            if (not isinstance(arg, int) # check type
                    or isinstance(arg, bool)):
                msg = "all arguments must be integers"
                raise TypeError(msg)
            
        self._hours = hours
        self._mins = mins
        self._secs = secs



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
        
        # Get class (to call initializer)
        cls = type(self)

        # Conversion
        hms = self.dec2hms(decimal)
        time = cls(*hms)
        
        # Secs
        total_secs = self._secs + time._secs
        secs = total_secs % 60
        # Mins
        total_mins = self._mins + time._mins + total_secs//60
        mins = total_mins % 60
        # Hours
        hours = self._hours + time._hours + total_mins//60

        return cls(hours, mins, secs)
    


    def __radd__(self, decimal):
        """Adds calling Time instance to given decimal time."""
        # Called by 'decimal + instance', which is equivalent under
        # the hood to 'instance.__iadd__(decimal)'.
        # As operator '+' is commutative, we can just use __add__ (it will also
        # handle the argument checks).

        return self + decimal # equivalent to calling 'self.__add__(decimal)'



    def __sub__(self, decimal):
        """Substracts given decimal time from calling Time instance."""
        # Called by 'instance - decimal', which is equivalent under
        # the hood to 'instance.__sub__(decimal)'.

        if (not isinstance(decimal, (int, float)) # check type
                or isinstance(decimal, bool)):
            raise TypeError("operand must be a decimal number")

        # Get class (to call initializer)
        cls = type(self)

        # Conversion
        hms = self.dec2hms(decimal)
        time = cls(*hms)
        
        # Secs
        total_secs = self._secs - time._secs
        secs = total_secs % 60
        # Mins
        total_mins = self._mins - time._mins + total_secs//60
        mins = total_mins % 60
        # Hours
        hours = self._hours - time._hours + total_mins//60

        return cls(hours, mins, secs)



    def __rsub__(self, decimal):
        """Substracts calling Time instance from given decimal time."""
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
        
        # Get class (to call initializer)
        cls = type(self)
        
        # Computation (in decimal -it's cheating, but you know...)
        prod_dec = self.hms2dec() * decimal
        prod_hms = self.dec2hms(prod_dec)

        return cls(*prod_hms)



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
	# defined __eq__, __gt__ and __ge__ methods (or the other way around),
    #  so we do not need to define them here.
	
	
	
# -------------------------------- TEST SCRIPT --------------------------------

import misctest as mt  # custom functions to make tests easier

mt.stepprint("Constructing Time objects")
dur_1 = 3.75
dur_2 = 2.425
hms_1 = Time.dec2hms(dur_1)
hms_2 = Time.dec2hms(dur_2)
time_1 = Time(*hms_1)
time_2 = Time(*hms_2)
print("NUM\tDUR (h)\t\tTIME (hh:mm:ss)")
print("1\t{}\t\t{}".format(dur_1, time_1))
print("2\t{}\t\t{}".format(dur_2, time_2))

mt.stepprint("Testing arithmetic operators")
print("Addition 'time_1 + dur_2': ", time_1 + dur_2)
print("Addition (reversed) 'dur_1 + time_2': ", dur_1 + time_2)
print("Subtraction 'time_1 - dur_2': ", time_1 - dur_2)
print("Subtraction (reversed) 'dur_1 - time_2': ", dur_1 - time_2)
print("Multiplication 'time_1 * 2': ", time_1 * 2)
print("Multiplication (reversed) '2 * time_1': ", 2 * time_1)

mt.stepprint("Testing comparison operators")
print("Comparison 'time_1 == time_1': ", time_1 == time_1)
print("Comparison 'time_1 != time_1': ", time_1 != time_1)
print("Comparison 'time_1 >= time_1': ", time_1 >= time_1)
print("Comparison 'time_1 <= time_1': ", time_1 <= time_1)
print("Comparison 'time_1 >= time_2': ", time_1 >= time_2)
print("Comparison 'time_1 <= time_2': ", time_1 <= time_2)