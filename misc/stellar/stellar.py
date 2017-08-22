# Given an array of ints, return true if each int is equal or greater than the one before. 

def solution(arr):
    sorted_arr = arr[:]
    sorted_arr.sort()
    print(arr, sorted_arr)
    if (sorted_arr == arr):
        return True
    return False

print(solution([1,3,2,4]))