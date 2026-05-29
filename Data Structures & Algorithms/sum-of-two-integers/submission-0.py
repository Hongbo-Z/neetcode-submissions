class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # 32-bit mask
        MAX_INT = 0x7FFFFFFF   # max positive 32-bit int

        while b != 0:
            # sum without carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # if a is negative in 32-bit signed int
        return a if a <= MAX_INT else ~(a ^ MASK)
