import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = [] 
        self.high = []
        heapq.heapify(self.low) # max heap, stores smaller half
        heapq.heapify(self.high) # min heap, stores bigger half

    # Idea: Keep balancing 2 heaps to make sure their cardinal difference
    # is always <= 1, and all numbers in low heap are smaller than all numbers
    # in high heap (less expensive then keeping whole thing sorted all the time) 
    # --> result lies in their intersection. 
    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -self.low[0])
        heapq.heappop(self.low)
        
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -self.high[0])
            heapq.heappop(self.high)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0]+self.high[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()