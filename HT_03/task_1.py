# Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples
# can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

values = [(1, 2, 3), (4, 5, 6), (7, 8), (9, ), ("a", "b")]
change_value = input("input value: ")

values = [values[element][:-1] + (change_value, ) for element in range(len(values))]

print(values)
