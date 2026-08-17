class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        
        res = 0
        intervals.sort()
        preEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if preEnd <= intervals[i][0]:
                preEnd = intervals[i][1]
            else:
                preEnd = min(preEnd, intervals[i][1])
                res += 1
        return res