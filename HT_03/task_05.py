# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

my_dict = {'1': 1, '2': 2, '3': 'value3', '4': 'value4', '5': 'value4', '6': 2, '7': 'value7'}
new_dict = {}

for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(new_dict)
