class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        m = len(s1)
        n = len(s2)
        if m > n : return False

        target = [0]*26
        for chr in s1:
            target[ord(chr) - ord('a')] += 1
        
        window = [0]*26
        for chr in s2[:m]:
            window[ord(chr) - ord('a')] += 1

        if target == window:
            return True
        
        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i-m]) - ord('a')] -= 1
            if target == window:
                return True
        return False 