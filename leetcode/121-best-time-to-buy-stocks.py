# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy+1
        bestProfit = 0
        lowestBuy = prices[buy]

        # Only need 1 pointer for sell time
        # Observation: max profit must come from buying one of the dips
        # For buying, keep updating bottom price (potentially max profit, need to compare with current best)
        while sell < len(prices):
            spotProfit = prices[sell] - lowestBuy
            bestProfit = max(bestProfit, spotProfit)
            lowestBuy = min(lowestBuy, prices[sell])
            sell += 1

        return bestProfit