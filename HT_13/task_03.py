# Створіть клас в якому буде атребут який буде рахувати кількість
# створених екземплярів класів.

class MyClass:
    count = 0

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.count += 1
        return instance


a = MyClass()
b = MyClass()
c = MyClass()
d = MyClass()

print("the number of class instances created: ", d.count)
