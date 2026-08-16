class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Backward
        # goal = len(nums) -1 
        # for i in range(len(nums)-2, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0

        # Forward
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) -1:
                return True