#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       30.12.2019
Description : Solve given equations and return unknown values.

Such as;

y = x + 1
5 = x + 3
10 = z + y + 2

return dict as {'x': 2, 'y' : 3, 'z' : 5}

Status = Completed
'''

import sys


class Equation():
    def __init__(self, equation_input):
        self.equation_input = equation_input
        print(f"\n{self.equation_input}")

        self.list_equation = self.equation_input.split("\n")
        self.count_equation = len(self.list_equation)
        self.unknown_values = dict()  # To hold answers
        self.unknown_value_count = dict()
        self.equation_unknown_map = dict()

    def main_handler_of_equations(self):
        self.find_unknown_values()

        while 1:
            self.find_less_unknown_equation()
            self.solve_equation()
            self.update_equations()

    def find_unknown_values(self):
        for idx, val in enumerate(self.list_equation):
            val = val.replace(" ", "").replace("+", "-").replace("=", "-")
            list_val = val.split("-")
            tmp_list = []
            for element in list_val:
                if self.is_number(element) is False:
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

    def find_less_unknown_equation(self):
        self.min_key = -1  # If min_key will not be assigned after loop, it means that program should finish.
        for key, value in self.equation_unknown_map.items():
            if len(value) == 1:
                self.min_key = key
                self.min_val = value
                break
        if self.min_key == -1:
            for key, value in self.unknown_values.items():
                if value is None:
                    print("\n\nThere is no solution with given inputs.'\n")
                    sys.exit(1)
            print(f"\n\nEquation Solution Set => {self.unknown_values}")
            sys.exit(0)

    def solve_equation(self):
        print("-"*50)
        print(f"Current Equation      => {self.list_equation[self.min_key]}")
        equation_divide = self.list_equation[self.min_key].replace(" ", "").split("=")

        left_equation = self.calculate_side(equation_divide[0])
        right_equation = self.calculate_side(equation_divide[1])
        print(left_equation)
        print(right_equation)

        if left_equation['values'][1] is not None:
            unknown_result = right_equation['values'][0] - left_equation['values'][0]
            self.unknown_values[left_equation['values'][1]] = unknown_result
            self.latest_unknown_value = left_equation['values'][1]
        elif right_equation['values'][1] is not None:
            unknown_result = left_equation['values'][0] - right_equation['values'][0]
            self.unknown_values[right_equation['values'][1]] = unknown_result
            self.latest_unknown_value = right_equation['values'][1]
        else:
            print("Unexpected case has occured!")
            sys.exit(1)

        print(f"Unknown Values Results => {self.unknown_values}")

    def update_equations(self):
        for idx, val in enumerate(self.list_equation):
            val = val.replace(self.latest_unknown_value, str(self.unknown_values[self.latest_unknown_value]))
            self.list_equation[idx] = val
            tmp_equation = self.list_equation[idx].replace(" ", "").replace("=", "").replace("+", "")

        for idx, val in enumerate(self.equation_unknown_map):
            if self.latest_unknown_value in self.equation_unknown_map[idx]:
                self.equation_unknown_map[idx].remove(self.latest_unknown_value)
        
        # TODO - Remove solved equation to increase efficiency
        print(f"Unknown Values Map     => {self.equation_unknown_map}")
        print(f"Remained Equations     => {self.list_equation}")

    def calculate_equations(self):
        pass

    def calculate_side(self, value):
        unknown = None

        if self.is_number(value) is True:
            return {'values': [int(value), unknown]}

        total = 0
        for i in value:
            if self.is_number(i) is True:
                total = total + int(i)
            elif self.is_number(i) is False and not i == "+":
                unknown = i
                print(f"Unknown Value to Find  => {i}")
        return {'values': [total, unknown]}

    def is_number(self, input_str):
        try:
            float(input_str)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    equation_input = "y = x + 1\n5 = x + 3\n10 = z + y + 2"
    # equation_input = "10 = z + y + 2\ny = x + 1\n5 = x + 3"
    # equation_input = "x + y = 5\nz = 3\nx + z = 10\nw = 5"
    instance = Equation(equation_input)
    instance.main_handler_of_equations()
