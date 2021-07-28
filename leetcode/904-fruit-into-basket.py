# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        ans = 0
        types = {}
        while right < len(fruits):
            current = fruits[right]
            if current not in types:
                types[current] = 1
            else:
                types[current] += 1
            while len(types) > 2 and right < len(fruits):
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                left += 1
                if left > right:
                    right += 1
                    current = fruits[right]
                    if current not in types:
                        types[current] = 1
                    else:
                        types[current] += 1
            if right - left + 1 > ans:
                # print('found new high', right, left)
                ans = right - left + 1
            right += 1
        return ans