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
    'key10': "apple",
}

int_values = [value for value in my_dict.values() if isinstance(value, int)]
float_values = [value for value in my_dict.values() if isinstance(value, float)]
string_values = [value for value in my_dict.values() if isinstance(value, str)]
list_values = [value for value in my_dict.values() if isinstance(value, list)]
tuple_values = [value for value in my_dict.values() if isinstance(value, tuple)]
set_values = [value for value in my_dict.values() if isinstance(value, set)]

general = [int_values, float_values, string_values, list_values, tuple_values, set_values]

for element in general:
    if len(element) > 0:
        print(f"max {type(max(element))} ", max(element))
        print(f"min {type(min(element))} ", min(element))
