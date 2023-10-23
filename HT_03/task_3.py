# Write a script to concatenate following dictionaries to create a new one.
#     dict_1 = {'foo': 'bar', 'bar': 'buz'}
#     dict_2 = {'dou': 'jones', 'USD': 36}
#     dict_3 = {'AUD': 19.2, 'name': 'Tom'

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

values = [dict_1, dict_2, dict_3]

new_dict = {key: value for i in values for key, value in i.items()}

print(new_dict)
