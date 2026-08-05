class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(c.lower() for c in s if c.isalnum())
        return newS == newS[::-1]