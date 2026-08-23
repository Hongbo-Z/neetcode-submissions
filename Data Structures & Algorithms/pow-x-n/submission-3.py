class Solution:
    def myPow(self, x: float, n: int) -> float:
        #  Binary Exponentiation
        if n == 0:
            return 1
        if x == 0:
            return 0
        
        power = abs(n)
        res = 1
        while power:
            if power & 1 :
                res *= x
            x *= x
            power >>= 1 
        return res if n > 0 else 1/res

# n & 1 checks the least significant bit:

# even: ...0 & 1 = 0
# odd: ...1 & 1 = 1