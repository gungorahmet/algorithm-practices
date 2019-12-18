#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       18.12.2019
Description : Question => Find all of subsets of a given set.

'''


class SubSet():
    def __init__(self, set_input):
        self.set_input = set_input

    def print_subset(self):
        pass


if __name__ == "__main__":
    set_input = [1, 2, 3, 4]
    instance = SubSet(set_input)
    instance.print_subset()
