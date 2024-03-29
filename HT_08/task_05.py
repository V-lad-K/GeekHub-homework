# Напишіть функцію,яка приймає на вхід рядок та повертає кількість
# окремих регістро-незалежних букв та цифр, які зустрічаються в рядку
# більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих
# і малих). Реалізуйте обчислення за допомогою генератора.
#     Example (input string -> result):
#     "abcde" -> 0            # немає символів, що повторюються
#     "aabbcde" -> 2          # 'a' та 'b'
#     "aabBcde" -> 2   # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
#     "indivisibility" -> 1   # 'i' присутнє 6 разів
#     "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
#     "aA11" -> 2             # 'a' і '1'
#     "ABBA" -> 2             # 'A' і 'B' кожна двічі

def get_unique_symbols(text):
    lower_elements_list = [i.lower() for i in text]
    unique_elements = set(i for i in lower_elements_list
                          if lower_elements_list.count(i) > 1)

    return len(unique_elements)


print(get_unique_symbols("ABBA"))
