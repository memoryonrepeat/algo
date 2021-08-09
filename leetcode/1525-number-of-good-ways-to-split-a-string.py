# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution:
    # Idea: Keep 2 sets of unique characters in left and right partitions
    # Run a pointer from left to right and update 2 sets along the way.
    # Then increase answer if at some point the length of 2 sets are the same.
    
    # There is one catch: It's easy to keep adding new chars to left set, but
    # how to know when it's time to remove a char from the right set ? There might be
    # cases where current character still appears further to the right side of right partition.

    # Therefore, we can only remove character from right partition if it's the last occurrence
    # (there is no same character further to the right). An easy way to know is to construct
    # a hashmap by going from right to left and record the first apearance of each unique character.

    def numSplits(self, s: str) -> int:
        leftSet = set()
        rightSet = set(s)
        ans = 0
        i = 0
        firstAppear = {}

        for i in range(len(s)-1,-1,-1):
            if s[i] not in firstAppear:
                firstAppear[s[i]] = i

        while i<len(s):
            leftSet.add(s[i])
            if i >= firstAppear[s[i]]:
                rightSet.remove(s[i])
            if len(leftSet) == len(rightSet):
                ans += 1
            i += 1

        return ans
                