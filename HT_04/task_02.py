# Create a custom exception class called NegativeValueError. Write a Python program that takes an integer as input and
# raises the NegativeValueError if the input is negative. Handle this custom exception with a try/except block and
# display an error message.

class NegativeValueError(Exception):
    pass


try:
    number = int(input("input number "))
    if number < 0:
        raise NegativeValueError
except NegativeValueError:
    print("was input negative number")
except ValueError as e:
    print(str(e))
