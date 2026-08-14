class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP bottom up
        n = len(cost)
        dp = [0]*(n + 1) # dp[n] is the top
        # dp[0], dp[1] = 0, 0 #  As we are chose to start at index 0 or index 1 floor 
        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[n]
