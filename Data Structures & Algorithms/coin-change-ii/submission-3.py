class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)  # dp[i] represent the number of distinct combinations to make up i
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[amount] 