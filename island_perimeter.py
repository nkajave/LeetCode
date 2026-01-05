from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = []
    print("Enter grid values row by row (0 or 1, space-separated):")

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) == cols:
                grid.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values")

    sol = Solution()
    print("Island Perimeter:", sol.islandPerimeter(grid))


"""
to run : python ./island_perimeter.py

git status
git add island_perimeter.py
git commit -m "Island Perimeter"
git push

"""