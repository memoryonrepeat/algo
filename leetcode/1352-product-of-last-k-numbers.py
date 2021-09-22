# https://leetcode.com/problems/product-of-the-last-k-numbers/

import math

class ProductOfNumbers:

    def __init__(self):
        self.prefixSum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixSum = [1]
        else:
            self.prefixSum.append(self.prefixSum[-1]*num)
            
            
    def getProduct(self, k: int) -> int:
        # print(k, len(self.prefixSum), self.prefixSum)
        if k >= len(self.prefixSum):
            return 0
        # print(self.prefixSum, -k-1)
        return int(self.prefixSum[-1] / self.prefixSum[-k-1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)