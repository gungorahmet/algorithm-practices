#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)
Author:       Ahmet Gungor
Date  :       28.02.2022
'''


class Water:
    def __init__(self):
        self.height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
        self.total_water = 0
        # self.height = [4, 2, 0, 3, 2, 5]  # 9
        # self.height = [4, 3, 2]  # 0
        # self.height = [3, 0, 1, 4, 2, 1, 4, 2, 4, 3, 3]  # To Test
        # self.height = [4, 0, 0, 1, 2, 5, 3, 1, 0, 4, 3, 2, 5]  # To Test

        # self.height = [0, 0, 3, 3, 2, 5, 4, 4, 5]  # To Test
        # self.height = [0, 7, 1, 4, 6]  # 7

    def process_the_water(self, height):
        left_wall_val = height[0]

        start_to_collect = False

        max_num = 0
        max_last_index = 0

        for idx, val in enumerate(height, 0):
            if val >= max_num:
                max_num = val
                max_last_index = idx

        i = 0
        while i < max_last_index:
            if height[i] > 0:
                start_to_collect = True

            if height[i] >= left_wall_val:
                left_wall_val = height[i]
                if not start_to_collect:
                    i += 1
                    continue

            if start_to_collect:
                for j in range(i + 1, max_last_index + 1):
                    if height[i] > height[j]:
                        self.total_water += (height[i] - height[j])
                    else:
                        left_wall_val = height[j]
                        i = j
                        break

    def calculate_total_water(self):
        max_num = 0
        max_last_index = 0

        for idx, val in enumerate(self.height, 0):
            if val >= max_num:
                max_num = val
                max_last_index = idx

        self.process_the_water(self.height[0:max_last_index + 1])
        self.process_the_water(self.height[max_last_index::][::-1])

        print(self.height)
        print("")
        print(f"self.total_water: {self.total_water}")

        return self.total_water


if __name__ == "__main__":

    ins_water = Water()
    ins_water.calculate_total_water()
