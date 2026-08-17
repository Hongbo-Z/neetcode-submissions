class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # while n:
        #     count += n & 1
        #     n = n >> 1 # equals n >>=1
        # return count

        while n:
            n = n & (n-1)
            count += 1
        return count