class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Iteration
        perms = [[]]
        for num in nums:
            new_perm = []
            for perm in perms:
                for idx in range(len(perm) + 1):
                    p = perm.copy()
                    p.insert(idx, num)
                    new_perm.append(p)
            perms = new_perm
        return perms
