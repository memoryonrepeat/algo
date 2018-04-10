# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    count = next = 0
    visited = {}
    while(next<len(A) and next>=0):
        count += 1
        next += A[next]
        if next in visited:
            return -1
        visited[next] = True
    return count