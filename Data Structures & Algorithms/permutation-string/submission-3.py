class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Two window
        m, n = len(s1), len(s2)
        if m > n: return False
        # create two freq array
        target = [0]*26
        window = [0]*26

        for i in range(m):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        if target == window: return True

        for j in range(m, n):
            window[ord(s2[j]) - ord('a')] += 1
            window[ord(s2[j - m]) - ord('a')] -=1
            if window == target: return True
        return False
