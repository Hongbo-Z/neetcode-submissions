class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic programming bottom up

        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0
        # dp[i] means the minimum amount of coins to make up amount
        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount]!= amount + 1 else -1
