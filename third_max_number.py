from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = set(nums)

        if len(distinct_nums) < 3:
            return max(distinct_nums)

        sorted_nums = sorted(distinct_nums, reverse=True)
        return sorted_nums[2]


if __name__ == "__main__":
    nums_input = input("Enter numbers separated by space: ")
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.thirdMax(nums)

    print("Third maximum:", result)


"""
to run: python ./third_max_number.py
enter numbers

git status
git add third_max_number.py
git commit -m "Finding Third Maximum Number in List"

"""