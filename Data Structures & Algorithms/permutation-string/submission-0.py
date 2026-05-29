class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = collections.Counter(s1)
        
        for l in range(0, len(s2)-len(s1)+1):
            curr = s2[l: l+len(s1)]
            count_curr = collections.Counter(curr)
            if count_s1 == count_curr:
                return True
        return False

