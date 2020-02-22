#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       23.02.2020
Description : This problem was asked by Ahmet Gungor;
              n is a parameter with 1 < n < 10 condition;
              Below figure should be printed as output according to n value.

              e.g. n = 4 needs to be as;

              4 4 4 4 4 4 4
              4 3 3 3 3 3 4
              4 3 2 2 2 3 4
              4 3 2 1 2 3 4
              4 3 2 2 2 3 4
              4 3 3 3 3 3 4
              4 4 4 4 4 4 4
'''


class DanceOfNumbers():
    def __init__(self, n):
        '''
        Assigment values
        '''
        self.n = n

    def print_shape(self):
        '''
        Print figure
        '''
        pass


if __name__ == "__main__":
    n = input("Please input n value: ")
    instance = DanceOfNumbers(n)
    instance.print_shape()
