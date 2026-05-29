class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # Method 1 with Backtracking
        # res = []
        # subset = []
        # # i is the searching index corresponding to the nums arr
        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return 
        #     # decision to include nums[i]
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     # decision NOT to include nums[i]
        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)
        # return res

        # Method 2 with Iteration
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
