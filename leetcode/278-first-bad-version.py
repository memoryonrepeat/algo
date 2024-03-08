# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                if mid == 1:
                    return mid
                if not isBadVersion(mid-1):
                    return mid
                high = mid - 1
            else:
                if mid == n-1:
                    return n
                low = mid+1
        
        return -1