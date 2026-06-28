class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort()
        preEnd = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            if preEnd <= interval[0]:
                preEnd = interval[1]
            else:
                preEnd = min(preEnd, interval[1]) # always keep the one end first
                res += 1
        return res   