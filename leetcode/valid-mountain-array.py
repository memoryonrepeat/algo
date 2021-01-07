# https://leetcode.com/problems/valid-mountain-array/
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 1
        pivot = -1
        while i<len(A):
            if A[i] > A[i-1]:
                i += 1
            else:
                break
        if i==1:
            return False
        pivot = i-1
        while pivot<len(A)-1:
            if A[pivot] > A[pivot+1]:
                pivot += 1
            else:
                break
        if pivot < len(A)-1 or pivot == i-1:
            return False
        return True
