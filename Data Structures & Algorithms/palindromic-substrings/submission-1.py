class Solution:
    def countSubstrings(self, s: str) -> int:
        # Method1 :Brute force
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l, r = i, j
        #         while l < r and s[l] == s[r]:
        #             l += 1
        #             r -= 1
        #         if l >= r:
        #             count += 1
        # return count

        # Method2, Two pointers
        count = 0
        for i in range(len(s)):
            # for odd case
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # for even case
            l, r = i, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count 
 

        
