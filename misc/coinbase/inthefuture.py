# Complete the function below.


def  minNum(A, K, P):
    if K<=A:
        return -1
    days = 0
    while P>=0:
        P -= (K-A)
        days += 1
    return days