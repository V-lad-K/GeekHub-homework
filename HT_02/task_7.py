# Write a script to concatenate all elements in a list into a string and print it. List must be include both strings and
# integers and must be hardcoded.

values_list = [1, 5, "hello", 4, "Vlad", 4545]
result_string = ""

for value in values_list:
    result_string += str(value)

print(result_string)
