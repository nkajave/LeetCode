from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        actual_sum = sum(nums)
        expected_sum = a * (a + 1) // 2
        missing_number = expected_sum - actual_sum
        return missing_number


if __name__ == "__main__":
    # Take input from terminal
    user_input = input("Enter numbers separated by space: ")
    nums = list(map(int, user_input.split()))

    sol = Solution()
    result = sol.missingNumber(nums)

    print("Missing number is:", result)


"""
to run: python ./missing_number.py
enter numbers

git status
git add missing_number.py
git commit -m "finding missing number"
git push

"""