class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        # 32-bit signed integer range check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    x = int(input("Enter an integer: "))

    sol = Solution()
    result = sol.reverse(x)

    print("Reversed integer:", result)


"""
to run: python reverse_integer.py
"""
