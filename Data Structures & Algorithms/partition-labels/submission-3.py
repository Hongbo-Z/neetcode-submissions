class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastCharIndex = {}
        for i, char in enumerate(s):
            lastCharIndex[char] = i
        
        res = []
        start, end = 0, 0

        for i, char in enumerate(s):
            end = max(end, lastCharIndex[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res