#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)
Author:       Ahmet Gungor
Date  :       29.08.2020
Description : In mathematics, the look-and-say sequence is the sequence of
          integers beginning as follows;
              1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
              To generate a member of the sequence from the previous member,
          read off the digits of the previous member, counting the number of
          digits in groups of the same digit.For example:
              1 is read off as "one 1" or 11.
              11 is read off as "two 1s" or 21.
              21 is read off as "one 2, then one 1" or 1211.
              1211 is read off as "one 1, one 2, then two 1s" or 111221.
              111221 is read off as "three 1s, two 2s, then one 1" or 312211.

              So the question is calculate look and say number and find
          30th element length.
'''


class Calculation:
    '''
    Calculation class of look and say number
    '''
    def __init__(self):
        pass

    def calculate_look_and_say_number_by_index(self, idx):
        '''
        Calculation of look and say number function till the given index
        '''
        pass


if __name__ == "__main__":
    '''
    Main function to call Calculation class and find 30th look and say number
    '''

    ins_calc = Calculation()
    look_and_say_num = ins_calc.calculate_look_and_say_number_by_index(30)

    print(f"len(30) is {len(look_and_say_num)}")
