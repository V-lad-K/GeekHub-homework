# Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end
# script must print out result of concatenating all <number> strings.

number = int(input("input number: "))
string = ""

for i in range(number):
    input_string = input("input string: ")
    string += input_string

print(string)
