# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowStrength = list(map(lambda e: (sum(e[1]),e[0]), enumerate(mat)))
        heapq.heapify(rowStrength)
        return list(map(lambda e: e[1], heapq.nsmallest(k, rowStrength)))