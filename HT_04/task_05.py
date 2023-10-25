# Create a Python program that repeatedly prompts the user for a number until a valid integer is provided. Use a
# try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered.
# Display the final valid integer.

while True:
    try:
        number = input("input number ")
        if not number.isdigit():
            raise ValueError
        else:
            print("number", int(number))
            break
    except ValueError:
        print("number is not int ")
        continue
