# Write a script that combines three dictionaries by updating the first one.

dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

values = [dict_2, dict_3]

for i in values:
    dict_1.update(i)

print(dict_1)
