from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        abc = []

        for a in range(numRows):
            line = [1] * (a + 1)

            for b in range(1, a):
                line[b] = abc[a - 1][b - 1] + abc[a - 1][b]

            abc.append(line)

        return abc


if __name__ == "__main__":
    # Take input from terminal
    numRows = int(input("Enter number of rows: "))

    sol = Solution()
    result = sol.generate(numRows)

    print("Output:")
    for row in result:
        print(row)


"""
to run code : python ./pascals_traingle.py
enter number of rows

git status
git add pascals_triangle.py
git commit -m "Pascal's Triangle"
git push


"""