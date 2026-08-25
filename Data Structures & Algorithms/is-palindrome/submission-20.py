class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(char.lower() for char in s if self.isAlNum(char))
        return string == string[::-1] 
    

    def isAlNum(self,char):
        if (
            ord('a') <= ord(char) <= ord('z') or
            ord('A') <= ord(char) <= ord('Z') or
            ord('0') <= ord(char) <= ord('9') 
            ):
            return True
        else:
            return False