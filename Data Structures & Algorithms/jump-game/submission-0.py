class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # goal is the goal index
        for idx in range(len(nums)-2, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx
        return goal == 0
        