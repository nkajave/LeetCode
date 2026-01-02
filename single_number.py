from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for b in nums:
            a ^= b
        return a


if __name__ == "__main__":
    # Input from terminal
    user_input = input("Enter numbers separated by space: ")
    nums = list(map(int, user_input.split()))

    sol = Solution()
    result = sol.singleNumber(nums)

    print("Single number is:", result)

"""
to run : python ./single_number.py
enter numbers

git status
git add single_number.py
git commit -m "finding exactly one number appears once"
git push

"""