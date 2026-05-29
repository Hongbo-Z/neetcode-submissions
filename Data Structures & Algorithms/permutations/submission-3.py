class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Backtrack
        res = []
        subSet = []
        used = [False]*len(nums)

        def backtrack():
            if len(subSet) == len(nums):
                res.append(subSet.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                subSet.append(nums[i])
                used[i] = True
                backtrack()
                subSet.pop()
                used[i] = False           
        backtrack()
        return res
