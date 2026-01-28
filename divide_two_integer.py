class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_min = -2**31
        int_max = 2**31 - 1

        # Handle overflow case
        if dividend == int_min and divisor == -1:
            return int_max

        # Check sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quo = 0

        # Subtract divisor using bit shifting
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while (temp << 1) <= dividend:
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quo += multiple

        # Apply sign
        if negative:
            quo = -quo

        # Clamp to 32-bit signed integer range
        return min(max(quo, int_min), int_max)


# ---------- Main Driver Code ----------

if __name__ == "__main__":
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))

    sol = Solution()
    result = sol.divide(dividend, divisor)

    print("Quotient:", result)


"""
to run: python divide_two_integer.py

git status
git add divide_two_integer.py
git commit -m 'Divide Two Integer'
git push
"""