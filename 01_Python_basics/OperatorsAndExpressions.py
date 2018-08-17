#####################################################
#  Operators and Expressions in Python:
# From: Jun 20, 2018 , https://realpython.com/python-operators-expressions/
#####################################################
#  the arithmetic operators supported by Python:
#####################################################
# Operator	    Example	        Meaning	        Result
# + (unary)	    +a	            Unary Positive	        a . In other words, it doesn’t really do anything.
#                                       It mostly exists for the sake of completeness, to complement Unary Negation.
# + (binary)	a + b	        Addition	    Sum of a and b
# - (unary)	    -a	            Unary Negation	Value equal to a but opposite in sign
# - (binary)	a - b	        Subtraction	    b subtracted from a
# *	            a * b	        Multiplication	Product of a and b
# /	            a / b	        Division	    Quotient when a is divided by b. The result always has type float.
# %	            a % b	        Modulus	        Remainder when a is divided by b
# //	        a // b	        Floor Division (also called Integer Division)	Quotient when a is divided by b,
#                                                                          rounded to the next smallest whole number
# **	        a ** b	        Exponentiation	a raised to the power of b

######################################
print("\nThe / and // operands:")
a = 5
b = -2
print("a/b: ", a, "/", b, "=", a/b, " , type:", type(a/b))
print("a//b: ", a, "//", b, "=", a//b, " , type:", type(a//b))

########################################
# Evaluation of Non-Boolean Values in Boolean Context
########################################
# In Python all the following are considered false when evaluated in Boolean context:
#   * The Boolean value False
#   * Any value that is numerically zero (0, 0.0, 0.0+0.0j)
#   * An empty string
#   * An object of a built-in composite data type which is empty (see below)
#   * The special value denoted by the Python keyword None

print("\nEmpty String is False:")
print("bool(\"\"):", bool(''), bool(""), bool(""""""))  # False False False
print("bool(\"foo\"):", bool('foo'), bool(" "), bool(''' '''))  # True True True

########################################
# Built-In Composite Data Object
########################################
# Python provides built-in composite data types called list, tuple, dict, and set.
# These are “container” types that contain other objects.
# An object of one of these types is considered false if it is empty and true if it is non-empty.
# The examples below demonstrate this for the list type. (Lists are defined in Python with square brackets.)
print("\nBuilt-In Composite Data Object")
print("type([]) =", type([]))  # <class 'list'>
print("bool([]) =", bool([]))  # False
print("type([1, 2, 3]) =", type([1, 2, 3]))  # <class 'list'>
print("bool([1, 2, 3]) =", bool([1, 2, 3]))  # True

print("\nThe 'None' Keyword:")
print("None is always false: bool(None) =", bool(None))  # False


######################################
def f(value):
    print("  value is", bool(value))
    return bool(value)

print("\nShort-circuit evaluation (also McCarthy evaluation)")
print("chain of OR: (evaluates until the first True)")
f(0) or f(False) or f(1) or f(2) or f(3)
print("chain of AND: (evaluates until the first False)")
f(0) and f(False) and f(1) and f(2) and f(3)

print("\nAvoid division by Zero (using Short-circuit evaluation):")
print("How? before division by zero - check if zero:")
a = 0
b = 1
# (b / a) > 0   --> ZeroDivisionError
print(" first check a!=0 : (a != 0) and (b / a) > 0", "  --> ", (a != 0) and (b / a) > 0)
print(" or simply check a: a and (b / a) > 0", "  --> ", a and (b / a) > 0)

######################################################################
# Bitwise Operators
######################################################################
# Bitwise operators treat operands as sequences of binary digits and operate on them bit by bit.
# The following operators are supported:
#
# Operator   Example	    Meaning	                    Result: Each bit position in the result is the logical...:
#    &       a & b	        bitwise AND	                ...AND of the bits in the corresponding position of the operands.
#                                                           (1 if both are 1, otherwise 0.)
#    |	     a | b	        bitwise OR	                ...OR of the bits in the corresponding position of the operands.
#                                                           (1 if either is 1, otherwise 0.)
#    ~	     ~a	            bitwise negation	        ...negation of the bit in the corresponding position of the
#                                                           operand. (1 if 0, 0 if 1.)
#    ^       a ^ b	        bitwise XOR (exclusive OR)	...XOR of the bits in the corresponding position of the operands.
#                                                           (1 if the bits in the operands are different, 0 if they are
#                                                           the same.)
#    >>	     a >> n	        Shift right n places	    Each bit is shifted right n places.
#    <<	     a << n	        Shift left n places	        Each bit is shifted left n places.

print("\nBitwise Operators")
print("0b1100 & 0b1010 =>", '0b{:04b}'.format(0b1100 & 0b1010))  # '0b1000'
print("0b1100 | 0b1010 =>", '0b{:04b}'.format(0b1100 | 0b1010))  # '0b1110'
print("0b1100 ^ 0b1010 =>", '0b{:04b}'.format(0b1100 ^ 0b1010))  # '0b0110'
print("0b1100 >> 2 =>", '0b{:04b}'.format(0b1100 >> 2))  # '0b0011'
print("0b0011 << 2 =>", '0b{:04b}'.format(0b0011 << 2))  # '0b1100'
print("0b0011 << 3 =>", '0b{:04b}'.format(0b0011 << 3))  # '0b11000'
print("0b0011 >> 3 =>", '0b{:04b}'.format(0b0011 >> 3))  # '0b0000'


######################################################################
# Identity Operators
######################################################################
# Python provides two operators, is and is not, that determine whether the given operands have the same identity
# —that is, refer to the same object. This is not the same thing as equality,
# which means the two operands refer to objects that contain the same data but are not necessarily the same object.

print("\nIdentity Operators")
print("example of two object that are equal but not identical:")
print("x = 1001")
print("y = 1000 + 1")
x = 1001
y = 1000 + 1
print("x==y :", x == y)  # True
print("x is y :", x is y)  # False
print("  since: id(x)!=id(y):  id(x)=", id(x), "and id(y)=", id(y))

a = 'I am'
b = a
print("\ncomparing same pointed object")
print("a = 'I am'")
print("b = a")
print("a==b :", a == b)  # True
print("a is b :", a is b)  # True
print("  since: id(a)==id(b):  id(a)=", id(a) ,"and id(b)=", id(b))
