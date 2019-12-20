#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       20.12.2019
Description : Question: Find second greatest value of a given list
'''


class Greatnesss():
    def __init__(self, set_input):
        self.set_input = set_input
        self.length_set = len(self.set_input)
        print(f"\n\nList => {self.set_input}")
        print(f"List Length => {self.length_set}\n")

    def find_second_greatest_element(self):
        pass
        # TODO


if __name__ == "__main__":
    set_input = [5, 6, 13, 7, 10, 45, 3, 1, 71, 21, 5, 9, 1, 15]
    instance = Greatnesss(set_input)
    instance.find_second_greatest_element()
