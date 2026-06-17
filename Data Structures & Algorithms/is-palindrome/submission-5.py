class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if self.isalNum(c):
                new_s += c.lower()
        return new_s == new_s[::-1]
    

    def isalNum(self, c: chr):
        if (
            ord("a") <= ord(c) <= ord("z") or
            ord("A") <= ord(c) <= ord("Z") or
            ord("0") <= ord(c) <= ord("9")
        ):
            return True
        