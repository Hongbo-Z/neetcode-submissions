class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0/1 背包问题（每个数只能用一次，看能不能"装满"容量为 target 的背包）
        # dp[i] represent if there is a subset that they can make up to i
        
        total = sum(nums)
        if total % 2!= 0:
            return False
        target = total // 2
        dp = [False]*(target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num -1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]
