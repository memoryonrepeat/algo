# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        nonEmptyBoxes = []
        for i,box in enumerate(boxes):
            if box == '1':
                nonEmptyBoxes.append(i)
        for i in range(len(boxes)):
            # print(nonEmptyBoxes, sum(b for b in nonEmptyBoxes))
            ans.append(sum(abs(b-i) for b in nonEmptyBoxes))
        return ans