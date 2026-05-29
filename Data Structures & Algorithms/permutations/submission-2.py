class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Iteration
        # perms = [[]]
        # for num in nums:
        #     new_perm = []
        #     for perm in perms:
        #         for idx in range(len(perm) + 1):
        #             p = perm.copy()
        #             p.insert(idx, num)
        #             new_perm.append(p)
        #     perms = new_perm
        # return perms

        # Recursion
        if len(nums) == 0:
            return [[]]
    
        perms = self.permute(nums[1:])
        res = []
        for perm in perms:
            for i in range(len(perm) + 1):
                p_copy = perm.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res



