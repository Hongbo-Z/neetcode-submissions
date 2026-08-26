class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        n1, n2 = len(s1), len(s2)
        counts_s1 = Counter(s1)
        while l < n2 - n1 + 1:
            if Counter(s2[l:l+n1]) == counts_s1:
                return True
            l += 1
        return False