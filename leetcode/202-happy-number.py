class Solution:
    def __init__(self):
        # Need to init variables in constructor
        # Otherwise previous testcase's variables will be reused
        self.processed = set()

    def isHappy(self, n: int) -> bool:
        self.processed.add(n)
        nextSum = 0
        while n // 10 > 0:
            nextSum += (n%10)**2
            n = n // 10
        nextSum += n**2
        # print(self.processed, nextSum)
        if nextSum == 1:
            return True
        if nextSum in self.processed:
            return False
        return self.isHappy(nextSum)