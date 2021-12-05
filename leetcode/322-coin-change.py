# https://leetcode.com/problems/coin-change/

class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in dp:
                return dp[amount]

            candidates = [coin for coin in coins if coin <= amount]

            if not candidates:
                dp[amount] = -1
                return -1

            result = [1+solve(amount - c) for c in candidates]

            if all([r == 0 for r in result]):
                dp[amount] = -1
                return -1
            
            # print(result)

            dp[amount] = min([r for r in result if r>0])

            return dp[amount]
        
        return solve(amount)
        
        