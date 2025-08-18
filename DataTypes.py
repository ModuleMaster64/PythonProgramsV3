# Number data types
import random

# Subroutine to demonstrate casting and operators
def MathsDemo(X, Y):
    DivisionResult = X / Y
    print("{} divided by {} is {}".format(X, Y, DivisionResult))
    IntDivisionResult = X // Y
    print("{} interger divison by {} is {}".format(X, Y, IntDivisionResult))
    ModResult = X % Y
    print("{} modulus {} is {}".format(X, Y, ModResult))
    ExpResult = X ** Y
    print("{} to the power of {} is {}".format(X, Y, ExpResult))

# Main program
MathsDemo(25,6)