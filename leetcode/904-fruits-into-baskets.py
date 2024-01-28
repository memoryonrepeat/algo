class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Find length of longest substring having at most 2 different elements
        # Meta: Model the problem --> solve with least redundant core info / derivative info
        right = 0
        left = 0
        basket = {} # key = fruit, val = index of last appearance of fruit
        maxFruits = 0
        while right < len(fruits):
            current = fruits[right]
            basket[current] = right
            # print("before", left, right, basket)
            if len(basket) > 2:
                toRemove = min(basket.keys(), key = lambda f: basket[f])
                left = basket[toRemove]+1
                del basket[toRemove]
            # print("after", left, right, basket)
            maxFruits = max(maxFruits, right-left+1)
            right += 1
        return maxFruits