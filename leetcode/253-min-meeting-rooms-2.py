# https://leetcode.com/problems/meeting-rooms-ii/submissions/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        currentRooms = 0
        final = 0
        events = []
        
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1], -1))
        
        #events.sort(key = lambda x: x[0])
        events.sort()
        
        #print(events)
        
        for event in events:
            currentRooms += event[1]
            final = max(final, currentRooms)
            
        return final