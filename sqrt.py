class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            mid_sq = mid * mid

            if mid_sq == x:
                return mid
            elif mid_sq < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    x = int(input("Enter number: "))
    sol = Solution()
    print("Integer Square Root:", sol.mySqrt(x))
