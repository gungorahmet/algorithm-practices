#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       13.01.2020
Description : This problem was asked by Two Sigma;
              You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000.
              Find the missing 1000 numbers.
              What is the computational and space complexity of your solution?
'''

import sys


class MissingNumbers():
    def __init__(self):
        '''
        Assigment values for testing;
        It is assignd from 400 to 990399 values in total 99000 unique values.
        So from 1 to 399 and 990400 to 1,000,000 values are missing to test.
        '''
        print(f"\n\n")
        main_list = [None] * 999000
        for i in range(400,990400):
            main_list[i-1] = i

    def find_missing_values(self):
        pass


if __name__ == "__main__":
    instance = MissingNumbers()
    instance = instance.main()