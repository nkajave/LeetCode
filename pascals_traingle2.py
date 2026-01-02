from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle[rowIndex]


if __name__ == "__main__":
    # Take input from terminal
    rowIndex = int(input("Enter row index: "))

    sol = Solution()
    result = sol.getRow(rowIndex)

    print("Output:", result)


"""
to run : python pascals_traingle2.py
enter row index

git status
git add pascals_traingle2.py
git commit - m "Pascal's Triangle : to getting that particular row not whole traingle"
git push

"""