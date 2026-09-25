class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if temp[1] < intervals[i][0]:
                res.append(temp)
                temp = intervals[i]
            else:
                temp[1] = max(temp[1], intervals[i][1])
        res.append(temp)
        return res