# Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple
# with those numbers.

sequence = input("input comma separated numbers sequence without spaces: ")
sequence_list = list(map(int, sequence.split(",")))

print("list:", sequence_list)
print("tuple:", tuple(sequence_list))
