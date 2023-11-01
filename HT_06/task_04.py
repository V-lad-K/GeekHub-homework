# Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і
# кінець діапазона, і вертатиме список простих чисел всередині цього
# діапазона. Не забудьте про перевірку на валідність введених даних та
# у випадку невідповідності - виведіть повідомлення.

def is_prime(number):
    if number <= 1:
        return False

    for item in range(2, number):
        if number % item == 0:
            return False
    return True


def prime_list(start, end):
    prime_numbers_list = [item for item in range(start, end+1) if is_prime(item)]
    return prime_numbers_list


try:
    start_range = int(input("input start of range "))
    end_range = int(input("input end of range "))
    print(prime_list(start_range, end_range))
except ValueError:
    print("Number is not an integer")
