class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        for n in nums:
            if result and result[-1][1] == n-1:
                result[-1][1] = n
            else:
                result += [[n,n]]

        return [f'{a}->{b}' if a!=b else f'{a}' for a,b in result]
