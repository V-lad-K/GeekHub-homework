# Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end
# script must print out result of concatenating all <number> strings.

number = int(input("input number: "))
string_list = [input("input string: ") for element in range(number)]

print(''.join(string_list))
