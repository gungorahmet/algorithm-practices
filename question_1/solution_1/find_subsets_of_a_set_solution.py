#!/usr/bin/python3
'''
Applied PEP8 (pycodestyle)

Author:       Ahmet Gungor
Date  :       18.12.2019
Description : Find all of possible subset of given set.
'''
import itertools


class SubSet():
    def __init__(self, set_input):
        self.set_input = set_input
        self.length_set = len(self.set_input)
        # Below line cartesian multiplication; 
        # if n = 2  ->  [0, 1] x [0, 1]  -> [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.binary_list = list(itertools.product([0, 1], repeat=self.length_set))
        print(f"\n\nBinary List Filter => {self.binary_list}\n\n")
        print(f"Now we can map Binary Filter with {self.set_input} set to have subsets\n")
        print(f"If 1 -> print index of set, if 0 -> no print")

    def print_subset(self):
        print(f"\nSubsets of {self.set_input}")
        print("-"*35)

        for idx, val in enumerate(self.binary_list):
            tmp_subset = "{"
            for i in range(0, self.length_set):
                if val[i] == 1:
                    tmp_subset = f"{tmp_subset}, {self.set_input[i]}"
            tmp_subset += " }"
            tmp_subset = tmp_subset.replace(",", "", 1)
            tmp_subset = f"{idx + 1} -> {tmp_subset}"

            print(tmp_subset)


if __name__ == "__main__":
    set_input = [1, 2, 3, 4]
    instance = SubSet(set_input)
    instance.print_subset()
