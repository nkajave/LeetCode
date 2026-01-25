class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create list to store characters for each row
        rows = [""] * numRows

        r = 0          # current row
        step = 1       # direction: 1 = down, -1 = up

        for ch in s:
            rows[r] += ch

            # Change direction at top or bottom
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1

            r += step

        return "".join(rows)


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    s = input("Enter string: ")
    numRows = int(input("Enter number of rows: "))

    sol = Solution()
    result = sol.convert(s, numRows)

    print("Zigzag Conversion Output:", result)

"""
to run: python zigzag_conversion.py

git status
git add zigzag_conversion.py
git commit -m "Zigzag Conversion"
git push
"""