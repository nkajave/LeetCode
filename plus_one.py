from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 9]))


""" 
commands to run this code:
check directory : pwd
verifying file existance : ls -l plus_one.py
run file : python ./plus_one.py

"""