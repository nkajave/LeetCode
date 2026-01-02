from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start = nums[i]

        # Adding last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result


if __name__ == "__main__":
    # Take input from terminal
    user_input = input("Enter numbers separated by space: ")
    if user_input.strip() == "":
        nums = []
    else:
        nums = list(map(int, user_input.split()))

    sol = Solution()
    result = sol.summaryRanges(nums)

    print("Summary Ranges:", result)

"""
to run: python ./summary_ranges.py
enter numbers

git status
git add summary_ranges.py
git commit -m "summarizing continue ranges of numbers"
git push

"""