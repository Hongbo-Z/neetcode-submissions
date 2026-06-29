class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquare(n)
            if n == 1:
                return True
        return False
        

    def sumOfSquare(self, n):
        sum = 0
        while n:
            digit = n % 10
            sum += digit**2
            n = n // 10
        return sum
                