class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Two windows
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        window1 = [0]*26
        window2 = [0]*26
        
        for i in range(n1):
            window1[ord(s1[i]) - ord('a')] += 1
            window2[ord(s2[i]) - ord('a')] += 1
        if window1 == window2:
            return True
        
        for j in range(n1, n2):
            window2[ord(s2[j]) - ord('a')] += 1
            window2[ord(s2[j - n1]) - ord('a')] -= 1
            if window2 == window1:
                return True
        return False
