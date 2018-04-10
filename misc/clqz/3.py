# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    if N<2:
        return N
    first = 0
    second = 1
    fib = 0
    count = 1
    while(count<N+1):
        fib = (first+second)%10000000
        second = first
        first = fib
        count += 1
    return fib%1000000