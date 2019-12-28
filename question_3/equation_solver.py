#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       29.12.2019
Description : Solve given equations and return unknown values.

Such as;

y = x + 1
5 = x + 3
10 = z + y + 2

return dict as {'x': 2, 'y' : 3, 'z' : 5}
'''


class Equation():
    def __init__(self, equation_input):
        self.equation_input = equation_input
        print(f"\n{self.equation_input}\n")

    def main_handler_of_equations(self):
        pass


if __name__ == "__main__":
    equation_input = "y = x + 1\n5 = x + 3\n10 = z + y + 2"
    instance = Equation(equation_input)
    instance.main_handler_of_equations()
