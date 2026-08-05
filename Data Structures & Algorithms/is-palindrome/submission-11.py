class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in range(len(s)):
            if self.isAlNum(s[i]):
                res += s[i].lower()
        return res == res[::-1]

    def isAlNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')):
            return True
        else:
            return False