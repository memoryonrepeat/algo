# Given an array of ints, return true if it is possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No loops needed.) 

# groupSum6(0, [5, 6, 2], 8) → true
# groupSum6(0, [5, 6, 2], 9) → false
# groupSum6(0, [5, 6, 2], 7) → false
# groupSum6(0, [5, 3, 6, 1], 15) → true

def groupSum6(start, arr, target):
    if (target<0):
        return False
    if sum(arr)==target:
        return True
    if len(arr)==0:
        if target==0:
            return True
        return False
    if arr[start]==6:
        return groupSum6(start, arr[1:], target-6)
    # Next recursion branch can include the current number at start or not
    return groupSum6(start, arr[1:], target-arr[start]) or groupSum6(start, arr[1:], target) 

print(groupSum6(0, [5, 3, 6, 1], 15))