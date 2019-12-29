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

Status = In Progress..
'''

import sys


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

        self.find_less_unknown_equation()
        self.solve_equation()

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

        print(self.min_key, self.min_val)
        # if self.min_key == -1:
        #     print("Program is completed")
        #     print("TODO write result")
        #     sys.exit(0)

    def solve_equation(self):
        print(self.list_equation[self.min_key])
        equation_divide = self.list_equation[self.min_key].replace(" ", "").split("=")

        left_equation = self.calculate_side(equation_divide[0])
        right_equation = self.calculate_side(equation_divide[1])
        print(left_equation)
        print(right_equation)

        if left_equation['values'][1] is not None:
            unknown_result = right_equation['values'][0] - left_equation['values'][0]
            self.unknown_values[left_equation['values'][1]] = unknown_result
        elif right_equation['values'][1] is not None:
            unknown_result = left_equation['values'][0] - right_equation['values'][0]
            self.unknown_values[right_equation['values'][1]] = unknown_result
        else:
            print("???")
            sys.exit(0)

        print(self.unknown_values)

    def update_equations(self):
        pass

    def calculate_equations(self):
        pass

    def calculate_side(self, value):
        total = 0
        unknown = None
        for i in value:
            if self.is_number(i) is True:
                total = total + int(i)
            elif self.is_number(i) is False and not i == "+":
                unknown = i
                print(f"{i} is unknown")
        return {'values': [total, unknown]}

    def is_number(self, input_str):
        try:
            float(input_str)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    # equation_input = "y = x + 1\n5 = x + 3\n10 = z + y + 2"
    equation_input = "10 = z + y + 2\ny = x + 1\n5 = x + 3"
    instance = Equation(equation_input)
    instance.main_handler_of_equations()


'''
    Ginger Equation Algorithm Scratch;

Order equations from with less unknown to most unknown values.
Iterate all equations and solve.
Then update all equations and calculate new sum.
iterate cumulatively again FROM THE BEGINNING of equations till you complete all.
If resolve return dict, else return null.

As psedo code below;

Do below steps till you resolve all of equations.
----------------------------------------------

find_less_unknown_equation()

for equation in all-equations:
    def solve() # Solve iteration with 1 unknown value.
        if solved:
            def update_equations_with_found_value()
            def calculate_new_sum_of_equations()
            go to find_less_unknown_equation() to re-check from the beginning.


------------------
If cannot resolve;
Not enough input. return null
'''
