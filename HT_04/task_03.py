# Create a Python script that takes an age as input. If the age is less than 18 or greater than 120, raise a custom
# exception called InvalidAgeError. Handle the InvalidAgeError by displaying an appropriate error message.

class InvalidAgeException(Exception):
    pass


try:
    number = int(input("input your age "))
    if not (18 <= number <= 120):
        raise InvalidAgeException
except InvalidAgeException:
    print("Invalid Age")
except ValueError as e:
    print(e)
