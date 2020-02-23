#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle) - max_line = 120

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
from os import system, name
from time import sleep


class DanceOfNumbers():
    def __init__(self, n):
        '''
        Assigment values
        '''
        self.n = n
        self.center = self.n - 1
        row_and_column_length = self.n * 2 - 1
        self.base_list = [[0 for x in range(row_and_column_length)] for x in range(row_and_column_length)]

    def handler(self):
        for depth_level in range(0, self.n):
            self.cover_square(depth_level)

    def cover_square(self, level):
        '''
        Cover around from the center with level by level
        '''
        iter_row_column_length = (level + 1) * 2 - 1
        for i in range(0, iter_row_column_length):
            self.base_list[self.center - level][self.center - level + i] = level + 1
            self.base_list[self.center + level][self.center - level + i] = level + 1

        for i in range(1, iter_row_column_length - 1):  # no need 2 times so from 1 and to -1
            self.base_list[self.center - level + i][self.center - level] = level + 1
            self.base_list[self.center - level + i][self.center + level] = level + 1

        self.simulate_code()

    def simulate_code(self):
        '''
        Simulation with sleep to see steps of handler
        '''
        if name == "nt":
            system("cls")
        else:  # posix for Linux and MacOS
            system("clear")

        self.print_shape()
        sleep(1)

    def print_shape(self):
        '''
        Print figure
        '''
        for element in self.base_list:
            print(element)


if __name__ == "__main__":
    n_range = False
    while not n_range:
        try:
            n = int(input("Please input n value (0 < n < 10): "))
            if n > 0 and n < 10:
                n_range = True
        except ValueError:
            pass

    instance = DanceOfNumbers(n)
    instance.handler()
