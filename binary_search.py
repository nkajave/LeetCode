from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    nums_input = input("Enter sorted numbers (space separated): ")
    nums = list(map(int, nums_input.split()))

    target = int(input("Enter target value: "))

    sol = Solution()
    result = sol.search(nums, target)

    print("Target index:", result)


"""
to run: python ./binary_search.py

git status
git add binary_search.py
git commit -m "Binary Search"
git push

"""