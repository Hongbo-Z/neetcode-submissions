"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
            
        intervals.sort(key = lambda x:x.start)
        preEnd = intervals[0].end
        for interval in intervals[1:]:
            if preEnd > interval.start:
                return False
            preEnd = interval.end
        return True