class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Option 1: reverse string
        # new_s = ""
        # for c in s:
        #     if self.isalNum(c):
        #         new_s += c.lower()
        # return new_s == new_s[::-1]

        # Option 2: Two pointers
        l_p = 0
        r_p = len(s) - 1
        while l_p < r_p:
            while l_p < r_p and not self.isalNum(s[l_p]):
                l_p += 1
            while l_p < r_p and not self.isalNum(s[r_p]):
                r_p -= 1
            if s[l_p].lower() != s[r_p].lower():
                return False
            l_p += 1
            r_p -= 1
        return True


    def isalNum(self, c: chr):
        if (
            ord("a") <= ord(c) <= ord("z") or
            ord("A") <= ord(c) <= ord("Z") or
            ord("0") <= ord(c) <= ord("9")
        ):
            return True
        