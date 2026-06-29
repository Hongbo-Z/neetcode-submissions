class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Brute force
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        power = abs(n)
        res = x
        for i in range(power - 1):
            res *= x
        return res if n > 0 else 1/res 
            