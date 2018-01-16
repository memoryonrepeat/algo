# https://www.interviewbit.com/problems/nextgreater/

# Brute solution involves running an inner loop through to the right to look for next greater element
# Optimized solution: every comparison between 2 numbers are made only once. So the stack will only
# keep a list of increasing number which can potentially be bigger than current one 
# (no point keeping smaller numbers in between as they are smaller than the one at the end of the stack any way 
# --> no need to compare them again).

def nextGreaterElement(arr):
    result = arr[:]
    result[-1] = -1
    stack = [len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        if stack:
            while stack and (arr[i]>arr[stack[-1]]):
                stack.pop()
        if not stack:
            result[i] = -1
        else:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result

print(nextGreaterElement([1,3,2,4]))
print(nextGreaterElement([100,80,60,70,60,75,85]))