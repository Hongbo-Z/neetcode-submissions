class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x:x[0])
        temp = intervals[0]
        res = []
        for i in range(1,len(intervals)):
            if temp[1] < intervals[i][0]:
                res.append(temp)
                temp = intervals[i]
            else:
                temp = [min(temp[0], intervals[i][0]), max(temp[1],intervals[i][1])]
        res.append(temp)
        return res


        