from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_length = 0

        for num in nums:
            if num == 1:
                current += 1
                if current > max_length:
                    max_length = current
            else:
                current = 0

        return max_length


if __name__ == "__main__":
    nums_input = input("Enter 0s and 1s separated by space: ")
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.findMaxConsecutiveOnes(nums)

    print("Max consecutive ones:", result)


"""
to run: python ./max_consecutive_once.py
enter  numbers

git status
git add max_consecutive_once.py
git commit -m "Finding Number of Maximum Consecutive Once"
git push

"""