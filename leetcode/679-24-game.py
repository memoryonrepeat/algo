# https://leetcode.com/problems/24-game/

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1 and abs(cards[0]-24) <= 0.01:
            return True
        for i, a in enumerate(cards):
            for j, b in enumerate(cards):
                if i != j:
                    rest = [cards[k] for k in range(len(cards)) if k != i and k != j]
                    if self.judgePoint24(rest + [a+b]):
                        return True
                    if self.judgePoint24(rest + [a*b]):
                        return True
                    if self.judgePoint24(rest + [a-b]):
                        return True
                    if self.judgePoint24(rest + [b-a]):
                        return True
                    if a != 0 and self.judgePoint24(rest + [b/a]):
                        return True
                    if b != 0 and self.judgePoint24(rest + [a/b]):
                        return True
        return False