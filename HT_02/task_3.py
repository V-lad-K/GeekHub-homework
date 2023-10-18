# Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input("input number: "))
suma = 0

if number >= 0:
    for i in range(number + 1):
        suma += i

print(suma)
