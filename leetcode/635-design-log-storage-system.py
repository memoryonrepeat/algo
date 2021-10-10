from bisect import bisect_left, bisect_right ,insort_left

class LogSystem:

    def __init__(self):
        self.timestamps = []
        self.logs = {}
        # position to cut off timestamp string based on granularity
        self.cutOffs = {
            'Year': 4,
            'Month': 7,
            'Day': 10,
            'Hour': 13,
            'Minute': 16,
            'Second': 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs[timestamp] = id
        insort_left(self.timestamps, timestamp)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        cutOff = self.cutOffs[granularity]
        start, end = start[:cutOff], end[:cutOff]
        timestamps = list(map(lambda t: t[:cutOff], self.timestamps))
        lowerBound = bisect_left(timestamps, start)
        upperBound = bisect_right(timestamps, end)
        
        return list(map(lambda timestamp: self.logs[timestamp], self.timestamps[lowerBound:upperBound]))

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)