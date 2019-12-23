#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       20.12.2019
Description : Question: Find second greatest value of a given list
'''


class Greatnesss():
    def __init__(self, list_input):
        self.list_input = list_input
        self.length_list = len(self.list_input)
        print(f"\n\nList => {self.list_input}")
        print(f"List Length => {self.length_list}\n")

    def find_second_greatest_element(self):
        pass
        # TODO - Find and print here second greatest value


if __name__ == "__main__":
    list_input = [5, 6, 13, 7, 10, 45, 3, 1, 71, 21, 5, 9, 1, 15]
    instance = Greatnesss(list_input)
    instance.find_second_greatest_element()
