#ProductOfArrayExceptSelf.py
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [1] * n

        # Prefix
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix = prefix * nums[i]

        # Suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]

        return answer
    
nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
solution = Solution()
result = solution.productExceptSelf(nums)

print("Output:", result)

"""
Test Cases
solution = Solution()

print(solution.productExceptSelf([1, 2, 3, 4]))        # Expected: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))   # Expected: [0, 0, 9, 0, 0]
print(solution.productExceptSelf([2, 3]))              # Expected: [3, 2]
print(solution.productExceptSelf([5, 1, 4, 2]))        # Expected: [8, 40, 10, 20]
"""

"""
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""