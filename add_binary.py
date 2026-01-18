class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))


if __name__ == "__main__":
    a = input("Enter first binary number: ")
    b = input("Enter second binary number: ")

    sol = Solution()
    result = sol.addBinary(a, b)

    print("Binary Sum:", result)


"""
python add_binary.py

git status
git add add_binary.py
git commit -m "Add Binary"
git push

"""