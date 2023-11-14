# Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів. Після
#    запуска програми на екран виводиться в лівій половині - колір
#    автомобільного, а в правій - пішохідного світлофора. Кожну 1
#    секунду виводиться поточні кольори. Через декілька ітерацій -
#    відбувається зміна кольорів - логіка така сама як і в звичайних
#    світлофорах (пішоходам зелений тільки коли автомобілям червоний).
#    Приблизний результат роботи наступний:
#       Red        Green
#       Red        Green
#       Red        Green
#       Red        Green
#       Yellow     Red
#       Yellow     Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Green      Red
#       Yellow     Red
#       Yellow     Red
#       Red        Green

import time

colours = ["Red", "Yellow", "Green"]


def emulator():
    while True:
        for colour in colours:
            if colour == "Yellow":
                iteration = 2
            else:
                iteration = 4
            for item in range(iteration):
                if colour == "Red":
                    print(colour, "Green")
                else:
                    print(colour, "Red")
                time.sleep(1)


emulator()
