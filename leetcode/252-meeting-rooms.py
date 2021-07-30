# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i: i[0])
        prevEnd = None
        for start,end in intervals:
            if not prevEnd:
                prevEnd = end
            else:
                if start < prevEnd:
                    return False
                prevEnd = end
        return True