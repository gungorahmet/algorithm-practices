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

        self.list_equation = self.equation_input.split("\n")
        self.count_equation = len(self.list_equation)
        self.unknown_values = dict()  # To hold answers
        self.unknown_value_count = dict()
        self.equation_unknown_map = dict()

    def main_handler_of_equations(self):
        self.find_unknown_values()

    def find_unknown_values(self):
        for idx, val in enumerate(self.list_equation):
            val = val.replace(" ", "").replace("+", "-").replace("=", "-")
            list_val = val.split("-")
            tmp_list = []
            for element in list_val:
                if element.isdigit() is False:
                    if element not in self.unknown_value_count:
                        self.unknown_value_count[element] = 1
                    else:
                        self.unknown_value_count[element] += 1

                    if element not in self.unknown_values:
                        self.unknown_values[element] = None

                    tmp_list.append(element)
            self.equation_unknown_map[idx] = tmp_list

        print("\n")
        print(f"Unknown values for each equation  =>  {self.equation_unknown_map}")
        print(f"Unknown values counts             =>  {self.unknown_value_count}")
        print(f"Unknown values                    =>  {self.unknown_values}")

    def order_equations(self):
        pass

    def solve_equation(self):
        pass

    def update_equations(self):
        pass

    def calculate_equations(self):
        pass


if __name__ == "__main__":
    equation_input = "y = x + 1\n5 = x + 3\n10 = z + y + 2"
    instance = Equation(equation_input)
    instance.main_handler_of_equations()
