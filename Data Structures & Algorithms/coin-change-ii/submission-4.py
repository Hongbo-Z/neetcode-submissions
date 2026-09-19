class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) # dp[a] means the number of distinct conbination that total up to a
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = dp[a] + dp[a - coin]
        return dp[amount]