# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

# Idea:
# First, sort the array
# Note that if we encounter a "faulty" subarray with elements increasing by <= 1,
# it means all elements from that subarray need to be increased
# and the minimal increment would make it become [a, a+1, a+2,...a+k]
# -> The total operations to be made is equal to the sum of that "intended" subarray
# minus the sum of original subarray. Then we reset the subarray and repeat.
# Also need to note the case where an element only belongs to that "faulty"
# subarray AFTER modification, i.e [1,2,2,3,5,9] --> [1,2,3,4,5,9] => 5 belongs
# to the sub even when 5 - 3 > 1. => Need line 27 not line 26

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        incSubArr = []
        
        ans = 0
        
        for num in nums:
            if not incSubArr:
                incSubArr.append(num)
            else:
                # if num - incSubArr[-1] <= 1:
                if num - (incSubArr[0] + len(incSubArr) - 1) <= 1:
                    incSubArr.append(num)
                else: # reset incSubArr, increase count
                    if len(incSubArr) == 1:
                        incSubArr = [num]
                    else:
                        a = incSubArr[0]
                        b = a + len(incSubArr) - 1
                        intendedSum = (a+b)*(b-a+1)//2
                        ans += intendedSum - sum(incSubArr)
                        incSubArr = [num]
                                
        if len(incSubArr) > 1:
            a = incSubArr[0]
            b = a + len(incSubArr) - 1
            intendedSum = (a+b)*(b-a+1)//2
            ans += intendedSum - sum(incSubArr)
            incSubArr = [num]
        
        return ans
                    