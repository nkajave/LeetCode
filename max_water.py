"""
to run : python max_water.py

git status
git add max_water.py
git commit -m 'Container With Most Water'
git push
"""

class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    height = list(map(int, input("Enter heights: ").split()))

    sol = Solution()
    result = sol.maxArea(height)

    print("Maximum water area:", result)
