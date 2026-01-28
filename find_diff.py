class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        # XOR all characters in s
        for ch in s:
            result ^= ord(ch)

        # XOR all characters in t
        for ch in t:
            result ^= ord(ch)

        # Convert ASCII value back to character
        return chr(result)


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    s = input("Enter string s: ")
    t = input("Enter string t: ")

    sol = Solution()
    diff = sol.findTheDifference(s, t)

    print("The extra character is:", diff)


"""
to run : python find_diff.py

git status
git add find_diff.py
git commit -m 'Find Difference'
git push
"""