class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if self.isAlNum(c):
                newS += c.lower()
        return newS == newS[::-1]

    def isAlNum(self, c:chr) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9") 
        ) 
