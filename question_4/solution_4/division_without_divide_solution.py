#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       03.01.2020
Description : This problem was asked by Nextdoor.
              Implement integer division without using the 
              division operator. Your function should return a tuple of (dividend, remainder)
              and it should take two numbers, the product and divisor.
              For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 
              and the remainder is 1.
              Bonus: Can you do it in O(log n) time? --> Bitwise solution is O(log n) but slower.
Status = Completed
'''

import sys


class Division():
    def __init__(self, product, divisor):
        self.product = product
        self.divisor = divisor
        print(f"\n{self.product} {self.divisor}\n")

    def divide(self):
        self.dividend = 0
        self.remainder = 0

        if self.divisor == 0:
            print("0 division error")
            sys.exit(1)
        if self.product == 0:
            tuple_result = (self.product, self.remainder)
            return tuple_result

        multiply_of_values = self.find_value_sign(self.product) * self.find_value_sign(self.divisor)

        self.product = abs(self.product)
        self.divisor = abs(self.divisor)

        while self.product > 0:
            if self.product < self.divisor:
                self.remainder = self.product
                break
            self.product -= self.divisor
            self.dividend += 1

        tuple_result = (self.dividend * multiply_of_values, self.remainder)
        return tuple_result

    def find_value_sign(self, num):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0


if __name__ == "__main__":
    product = 22
    divisor = -3
    instance = Division(product, divisor)
    tuple_result = instance.divide()
    print(tuple_result)
