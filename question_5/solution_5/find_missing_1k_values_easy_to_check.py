#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       13.01.2020
Description : Easier version of 1K missing values question.
              This script is searching 5 missing values from 20 values in 15 list size.
'''

import sys


class MissingNumbers():
    def __init__(self):
        print(f"\n\n")
        self.main_list = [1, 5, 7, 2, 10, 6, 16, 19, 11, 8, 13, 18, 3, 17, 14]

    def find_missing_values(self):
        self.my_dict = dict()
        self.solution_list = []
        for value in self.main_list:
            if value not in self.my_dict:
                self.my_dict[value] = True

        for element in range(1, 21):
            if element not in self.my_dict:
                self.solution_list.append(element)

        print(self.solution_list)


if __name__ == "__main__":
    instance = MissingNumbers()
    instance = instance.find_missing_values()
