class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit mask (optimal)
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
        
        # # Bit mask normal
        # res = 0
        # for i in range(32):
        #     if n & (1 << i):
        #         res += 1
        # return res