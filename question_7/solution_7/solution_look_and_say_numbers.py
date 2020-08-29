#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)
Author:       Ahmet Gungor
Date  :       29.08.2020
Description : In mathematics, the look-and-say sequence is the sequence
            of integers beginning as follows;
              1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
              To generate a member of the sequence from the previous member,
            read off the digits of the previous member,
              counting the number of digits in groups of the same digit.

              1 is read off as "one 1" or 11.
              11 is read off as "two 1s" or 21.
              21 is read off as "one 2, then one 1" or 1211.
              1211 is read off as "one 1, one 2, then two 1s" or 111221.
              111221 is read off as "three 1s, two 2s, then one 1" or 312211.

              So the question is how to calculate look and say number
            and find 30th element length?
'''


class Calculation:
    '''
    Calculation of look and say number class
    '''

    def __init__(self):
        pass

    def calculate_look_and_say_number_by_index(self, idx):
        '''
        Calculation look and say number function till given index
        '''
        # 0th element of look and say serie
        look_and_say_num = self.generate_look_and_say_number("1")

        for _ in range(1, idx):
            look_and_say_num = self.generate_look_and_say_number(look_and_say_num)

        return look_and_say_num

    def generate_look_and_say_number(self, str_num):
        '''
        Generates look and say number with a given number
        '''
        last_num = ""
        count = 0
        look_and_say_number = ""

        for num in str_num:
            if num == last_num or last_num == "":
                count = count + 1
                last_num = num
            else:
                look_and_say_number = f"{look_and_say_number}{count}{last_num}"
                last_num = num
                count = 1

        # To find last serie count.
        look_and_say_number = f"{look_and_say_number}{count}{last_num}"

        return look_and_say_number


if __name__ == "__main__":
    '''
    Main function to call Calculation class and find 30th look and say number
    '''

    ins_calc = Calculation()
    look_and_say_num = ins_calc.calculate_look_and_say_number_by_index(30)

    print(f"len(30) is {len(look_and_say_num)}")
