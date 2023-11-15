#  Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та
#  кількість символів. Файл також додайте в репозиторій. На екран
#  повинен вивестись список із трьома блоками - символи з початку, із
#  середини та з кінця файлу. Кількість символів в блоках - та, яка
#  введена в другому параметрі. Придумайте самі, як обробляти помилку,
#  наприклад, коли кількість символів більша, ніж є в файлі або,
#  наприклад, файл із двох символів і треба вивести по одному символу,
#  то що виводити на місці середнього блоку символів?). Не забудьте
#  додати перевірку чи файл існує.

def get_join_file_string(file):
    text_list = []

    for line in file:
        text_list.append(line.strip())

    return "".join(text_list)


def get_middle(string, count):
    diff = len(string) - count

    start = int(diff / 2) if diff % 2 == 0 else int(diff / 2) + 1
    end = start + count if diff % 2 == 0 else start + count - 1

    return string[start:end]


def get_blocks(file_name, count):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            file_text = get_join_file_string(f)
            file_length = len(file_text)

            if count >= file_length:
                print("The number of characters exceeds the file length.")
                return

            start_block = file_text[:count]
            middle_block = get_middle(file_text, count)
            end_block = file_text[-count:]

            print("start:", start_block)
            print("middle:", middle_block)
            print("end:", end_block)

    except FileNotFoundError:
        print("File not found")


get_blocks("task_02_test_1.txt", 3)
get_blocks("task_02_test_1.txt", 4)
get_blocks("task_02_test_1.txt", 5)
