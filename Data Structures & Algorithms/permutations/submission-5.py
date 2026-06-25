class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSet = []

        used = [False]*len(nums)
        def dfs():
            if len(subSet) == len(nums):
                res.append(subSet.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                subSet.append(nums[i])
                used[i] = True
                dfs()
                subSet.pop()
                used[i] = False        
        dfs()
        return res