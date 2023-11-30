# Create 'list'-like object, but index starts from 1 and index of 0
# raises error. Тобто це повинен бути клас, який буде поводити себе так
# , як list (маючи основні методи), але індексація повинна
# починатись із 1

class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError("Indexing starts from 1")
        return super().__getitem__(index - 1)
