class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount + 1) # +1 for 0
        dp[0] = 0 # for the amount 0 use zero coin

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] != float('inf') else -1