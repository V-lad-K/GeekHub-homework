# Write a script to check whether a value from user input is contained in a group of values.
#     e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

values_list = [1, 2, 'u', 'a', 4, True]
value = input("input value: ")

print(value in list(map(str, values_list)))
