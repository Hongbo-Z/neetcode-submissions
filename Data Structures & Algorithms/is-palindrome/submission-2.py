class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1, two pointer
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphNum(s[l]):
                l += 1
            while l < r and not self.isAlphNum(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def isAlphNum(self, c:chr) -> bool:
        return ((ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or (ord("0") <= ord(c) <= ord("9")))
    
