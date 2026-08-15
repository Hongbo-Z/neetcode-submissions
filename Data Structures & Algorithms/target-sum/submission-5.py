class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # total = P + N
        # target = P - N
        # P = (total + target)/2
        # The reformulate the problem of finding the number of difference ways to make up P
        total = sum(nums)
        if (total + target)%2 != 0:
            return 0
        if abs(target) > total:
            return 0

        P = (total + target)//2
        dp = [0]*(P+1)
        dp[0] = 1

        for num in nums:
            for j in range(P, num-1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[P]
