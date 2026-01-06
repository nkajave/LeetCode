from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    nums_input = input("Enter numbers separated by space: ")
    nums = list(map(int, nums_input.split()))

    sol = Solution()
    result = sol.threeSum(nums)

    print("Triplets that sum to zero:")
    for triplet in result:
        print(triplet)


"""
to run: python ./3sum.py

git status
git add 3sum.py
git commit -m "3SUM"
git push

"""