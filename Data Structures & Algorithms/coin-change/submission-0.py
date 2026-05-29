class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming - Bottom up
        dp = [amount+1]*(amount+1) # The length of dp arrar is "amount+1"
        dp[0] = 0
        # dp[a] means the minimum number of coins to make amount "a"
        for a in range(1, amount+1):
            for c in coins:
                # check if the remaining amount is positive, otherwise dp[a-c] does't exist
                if a - c >= 0: 
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount]!= amount+1 else -1


        