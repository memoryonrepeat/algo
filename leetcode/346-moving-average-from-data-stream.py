# https://leetcode.com/problems/moving-average-from-data-stream/

from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.q = deque([])

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.q.popleft()
        self.q.append(val)
        # print(self.q)
        return sum(self.q)/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

