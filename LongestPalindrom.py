class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    if len(sub) > len(longest):
                        longest = sub

        return longest


# ---------- main Driver Code ----------

if __name__ == "__main__":
    s = input("Enter a string: ")

    sol = Solution()
    result = sol.longestPalindrome(s)

    print("Longest Palindromic Substring:", result)


"""
to run: python LongestPalindrom.py

git status
git add LongestPalindrom.py
git commit -m "Longest Palindromic Substring"
git push
"""