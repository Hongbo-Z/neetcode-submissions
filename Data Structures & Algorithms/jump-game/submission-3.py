class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Backward
        # goal = len(nums) - 1 # goal is the goal index
        # for idx in range(len(nums)-2, -1, -1):
        #     if idx + nums[idx] >= goal:
        #         goal = idx
        # return goal == 0

        # Forward way
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
            if maxReach > len(nums) -1:
                return True
        return True 
        
        