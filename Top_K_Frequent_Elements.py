#Top_K_Frequent_Elements.py
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count frequency
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # create buckets
        bucket = []

        for _ in range(len(nums) + 1):
            bucket.append([])

        # put numbers into bucket based on frequency
        for num, freq in count.items():
            bucket[freq].append(num)

        # collect top k frequency
        final_result = []

        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                final_result.append(num)

                if len(final_result) == k:
                    return final_result


# -------- User Input --------

nums = list(map(int, input("Enter numbers separated by space: ").split()))

k = int(input("Enter k value: "))

solution = Solution()

result = solution.topKFrequent(nums, k)

print("Top K Frequent Elements:", result)

"""
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""