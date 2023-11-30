# Напишіть програму, де клас «геометричні фігури» (Figure) містить
# властивість color з початковим значенням white і метод для зміни
# кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square)
# містять методи __init__ для завдання початкових розмірів об'єктів
# при їх створенні.

class Figure:
    color = "white"
    all_colors = ["blue", "orange", "brown", "purple", "yellow", "white"]

    def change_color(self):
        while True:
            new_color = input(f"input one of the color: {*self.all_colors, } ")

            if new_color not in self.all_colors:
                print(f"color {new_color} does not exist")
            elif new_color == self.color:
                print(f"color {new_color} is already like this does not exist")
            else:
                self.color = new_color
                break


class Oval(Figure):
    def __init__(self, radius_1, radius_2):
        self.radius_1 = radius_1
        self.radius_2 = radius_2


class Square(Figure):
    def __init__(self, side):
        self.side = side
