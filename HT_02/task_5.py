# Write a script which accepts decimal number from user and converts it to hexadecimal.

hexadecimal_dict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}
residues = []

number = int(input("input positive number: "))

if number < 10:
    print(number)
elif 10 <= number <= 15:
    print(hexadecimal_dict[number])
else:
    while number > 0:
        residues.insert(0, str(hexadecimal_dict.get(number % 16, number % 16)))
        number = number//16
    print(''.join(residues))
