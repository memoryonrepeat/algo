# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack = []
        for i,num in enumerate(result):
            # print(stack, num)
            while stack and num <= prices[stack[-1]]:
                top = stack.pop()
                result[top] -= num
            stack.append(i)
                
        return result