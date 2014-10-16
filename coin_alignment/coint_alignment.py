# Consider N coins aligned in a row. Each coin is showing either heads or tails. The adjacency of these coins is the number of adjacent pairs of coins with the same side facing up.

# It must return the maximum possible adjacency that can be obtained by reversing exactly one coin (that is, one of the coins must be reversed). Consecutive elements of array A represent consecutive coins in the row. Array A contains only 0s and/or 1s: 0 represents a coin with heads facing up; 1 represents a coin with tails facing up. For example, given array A consisting of six numbers, such that:

#   A[0] = 1  
#   A[1] = 1  
#   A[2] = 0
#   A[3] = 1  
#   A[4] = 0  
#   A[5] = 0
# the function should return 4. The initial adjacency is 2, as there are two pairs of adjacent coins with the same side facing up, namely (0, 1) and (4, 5). After reversing the coin represented by A[2], the adjacency equals 4, as there are four pairs of adjacent coins with the same side facing up, namely: (0, 1), (1, 2), (2, 3) and (4, 5), and it is not possible to obtain a higher adjacency. The same adjacency can be obtained by reversing the coin represented by A[3].

def solution(A):
    n = len(A)
    result = 0
    for i in xrange(n - 1):
        if (A[i] == A[i + 1]):
            result = result + 1
    r = -1
    for i in xrange(n):
        count = 0
        if (i > 0):
            if (A[i - 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        if (i < n - 1):
            if (A[i + 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        r = max(r,count)
    return result + r
