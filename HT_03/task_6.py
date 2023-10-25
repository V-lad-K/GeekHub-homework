# Write a script to get the maximum and minimum value in a dictionary.

my_dict = {
    'key1': 42,
    'key2': 1,
    'key3': 2.44,
    'key4': 10.85,
    'key5': [1, 2, 3],
    'key6': [88, -5, 9],
    'key7': (5, 2),
    'key8': (4, 5, 6),
    'key9': "banana",
    'key10': "apple"
}

number_values = [value for value in my_dict.values() if isinstance(value, (int, float))]
string_values = [value for value in my_dict.values() if isinstance(value, str)]
collections_values = [value for value in my_dict.values() if isinstance(value, (list, tuple, set))]

for element in [number_values, string_values, collections_values]:
    if len(element) > 0:
        minimum = min(element, key=lambda x: min(x)) if isinstance(element[0], (list, tuple, set)) else min(element)
        maximum = max(element, key=lambda x: max(x)) if isinstance(element[0], (list, tuple, set)) else max(element)

        print(f"{type(maximum)}, {maximum}")
        print(f"{type(minimum)}, {minimum}")
