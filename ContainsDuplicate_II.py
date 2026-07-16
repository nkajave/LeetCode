from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = {}

        for i, num in enumerate(nums):
            if num in x:
                if i - x[num] <= k:
                    return True

            x[num] = i

        return False


nums = list(map(int, input("Enter nums: ").split()))
k = int(input("Enter k: "))

solution = Solution()

print(solution.containsNearbyDuplicate(nums, k))