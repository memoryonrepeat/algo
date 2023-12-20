class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                profit += prices[i-1] - prices[buy]
                buy = i

        # Sell if got bull run till the end while still holding
        if prices[-1] > prices[buy]:
            profit += prices[-1] - prices[buy]

        return profit