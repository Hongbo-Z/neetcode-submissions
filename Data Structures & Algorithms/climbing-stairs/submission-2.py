class Solution:
    def climbStairs(self, n: int) -> int:
        # DP (Bottom-Up)
        # if n <= 2:
        #     return n
        # # dp[i] = number of distinct ways to reach step i
        # dp = [0] * (n+1)
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n + 1):
        #     # Number of ways to reach step i = ways to reach i-1 + ways to reach i-2
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        
        # Space optimized
        prev, curr = 1, 1
    
        for _ in range(n-1):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr



        