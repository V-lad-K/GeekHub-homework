# Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all
# the colors from color_list_1 which are not present in color_list_2.

string_color_list_1 = input("input colors for list number 1 without spaces: ")
string_color_list_2 = input("input colors for list number 1 without spaces: ")

color_1_list = string_color_list_1.split(",")
color_2_list = string_color_list_2.split(",")

print(set(color_1_list) - set(color_2_list))
