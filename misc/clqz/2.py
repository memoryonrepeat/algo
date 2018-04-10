# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter

def solution(K, A):
    # write your code in Python 3.6
    counter = Counter(A)
    count = 0
    for key in counter:
        if K-key in counter:
            count += counter[key]*counter[K-key]
    return count