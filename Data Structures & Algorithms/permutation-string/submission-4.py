class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        target = collections.defaultdict(int)
        window = collections.defaultdict(int)
        
        for i in range(m):
            target[s1[i]] += 1
            window[s2[i]] += 1
        if target == window:
            return True

        for j in range(m, n):
            window[s2[j]] += 1
            window[s2[j-m]] -= 1
            if window[s2[j-m]] == 0:
                del window[s2[j-m]]
            if target == window:
                return True
        return False