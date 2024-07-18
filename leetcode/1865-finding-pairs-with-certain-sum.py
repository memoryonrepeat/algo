class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1.sort()
        self.nums2counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for _, n1 in enumerate(self.nums1):
            if n1 > tot:
                break
            if tot - n1 in self.nums2counter:
                count += self.nums2counter[tot - n1]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)