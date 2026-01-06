from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        a = len(matrix)
        b = len(matrix[0])

        result = [[0] * a for _ in range(b)]

        for i in range(a):
            for j in range(b):
                result[j][i] = matrix[i][j]

        return result


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    print("Enter matrix row by row (space separated):")

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"❌ Please enter exactly {cols} values")

    sol = Solution()
    result = sol.transpose(matrix)

    print("Transposed Matrix:")
    for row in result:
        print(row)


"""
to run : python ./matrix_transpose.py

git status
git add matrix_transpose.py
git commit -m "Matrix Transpose"
git push

"""