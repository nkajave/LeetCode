class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first = 1
        second = 2

        for i in range(3, n+1):
            current = first + second
            first = second
            second = current

        return second


if __name__ == "__main__":
    n = int(input("Enter number of stairs: "))
    sol = Solution()
    print("Ways to climb:", sol.climbStairs(n))

"""
to run: python climbing_stairs.py

git status
git add climbing_stairs.py
git commit -m "counting number of ways to reach given numbers by 1 or 2 steps"
git push

"""