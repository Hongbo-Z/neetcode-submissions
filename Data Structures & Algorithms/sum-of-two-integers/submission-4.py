class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b:
            a, b = (a ^ b) & mask, ((a & b) <<1) & mask
        return a if a <= maxInt else ~(a ^ mask) 
        