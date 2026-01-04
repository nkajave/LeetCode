from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()

        cookie = 0
        child = 0
        count = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                count += 1
                child += 1
                cookie += 1
            else:
                cookie += 1

        return count


if __name__ == "__main__":
    g_input = input("Enter greed factors (space separated): ")
    s_input = input("Enter cookie sizes (space separated): ")

    g = list(map(int, g_input.split()))
    s = list(map(int, s_input.split()))

    sol = Solution()
    result = sol.findContentChildren(g, s)

    print("Maximum content children:", result)


"""
to run: python ./assign_cookie.py

git status
git add assign_cookie.py
git commit -m "Assigning Cookies to children"
git push

"""