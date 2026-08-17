class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = [[1,5],[2,4],[6,7]]
        intervals.sort()
        temp = intervals[0]
        res = []
        for i, interval in enumerate(intervals[1:]):
            if temp[1] < interval[0]:
                res.append(temp)
                temp = interval
            else:
                temp = [min(temp[0], interval[0]), max(temp[1], interval[1])]
        res.append(temp)
        return res        