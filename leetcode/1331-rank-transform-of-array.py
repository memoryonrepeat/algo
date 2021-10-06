class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr)
        i = 1
        hashMap = {}
        for num in sortedArr:
            if num not in hashMap:
                hashMap[num] = i
                i += 1
        return list(map(lambda num: hashMap[num], arr))