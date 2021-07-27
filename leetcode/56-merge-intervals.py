# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # sort by start to ensure ordering
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            else:
                if interval[0] > merged[-1][1]: # non overlapping -> add to the right
                    merged.append(interval)
                else: # overlapping -> merged
                    merged[-1][1] = max(merged[-1][1], interval[1])
        return merged