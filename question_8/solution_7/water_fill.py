#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)
Author:       Ahmet Gungor
Date  :       28.02.2022
'''


class Water:
    def __init__(self):
        self.height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        # self.height = [4, 2, 0, 3, 2, 5]  #  To Test
        # self.height = [3, 0, 1, 4, 2, 1, 4, 2, 4, 3, 3]  #  To Test

    def calculate_total_water(self):
        total_water = 0

        for row in range(max(self.height), 0, -1):
            tmp_add_water = 0
            first_wall_found = False

            for val in self.height:
                if val >= row:
                    first_wall_found = True
                    total_water += tmp_add_water
                    tmp_add_water = 0
                    continue  # Passing the wall

                if first_wall_found:
                    tmp_add_water += 1

        print(f"Total Water: {total_water}")


if __name__ == "__main__":

    ins_water = Water()
    ins_water.calculate_total_water()
