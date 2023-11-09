#  Напишіть функцію,яка прймає рядок з декількох слів і повертає
#  довжину найкоротшого слова. Реалізуйте обчислення за допомогою
#  генератора.

def get_smallest_length(word_text):
    words = word_text.split()

    return min(len(word) for word in words)


