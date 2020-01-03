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
              and the remainder is 1
              Bonus: Can you do it in O(log n) time?
'''

import sys


class Division():
    def __init__(self, product, divisor):
        self.product = product
        self.divisor = divisor
        print(f"\n{self.product} {self.divisor}\n")

    def divide(self):
        pass
        # return tuple_result


if __name__ == "__main__":
    product = 10
    divisor = 3
    instance = Division(product, divisor)
    # tuple_result = instance.divide()
    # print(tuple_result)
