class Solution:
    def climbStairs(self, n: int) -> int:
        # DFS with recursion (Binary tree)
        # def dfs(i):
        #     if i > n:
        #         return False
        #     elif i == n:
        #         return True
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0)

        # DP (Bottom-Up)
        if n <= 2:
            return n
        # dp[i] = number of distinct ways to reach step i
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            # Number of ways to reach step i = ways to reach i-1 + ways to reach i-2
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

        # Optimized Dynamic programming
        # one, two = 1, 1
        # for i in range(n-1):
        #     one, two = one + two, one
        # return one

        