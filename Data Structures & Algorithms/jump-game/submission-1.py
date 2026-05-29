class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # Greedy
        # goal = len(nums) - 1 # goal is the goal index
        # for idx in range(len(nums)-2, -1, -1):
        #     if idx + nums[idx] >= goal:
        #         goal = idx
        # return goal == 0
        
        # DP Bottom up
        dp = [False]*len(nums) # dp[i]==True means from index i you can reach the end
        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            end = min(i + nums[i], len(nums)-1)
            for j in range(i+1, end+1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
