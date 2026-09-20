class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maxReach = 0
        # for i in range(len(nums)):
        #     if i > maxReach:
        #         return False
        #     maxReach = max(maxReach, i + nums[i])
        # return maxReach >= len(nums) - 1

        # BackWard
        goal = len(nums) - 1
        for i in range(len(nums) -2 , -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0 