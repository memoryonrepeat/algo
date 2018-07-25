# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

dp_table = {}


def _get_matrix_power(M, n):
    if n == 1:
        return M
    if n in dp_table:
        return dp_table[n]
    for i in range(1, n // 2 + 1):
        print(i, i * 2, i * 2 + 1)
        half = get_matrix_power(M, i)
        full = multiply(half, half)
        dp_table[i * 2] = full
        dp_table[i * 2 + 1] = multiply(full, M)
    return dp_table[n]

# Convert N to base 2, then multiply accordingly to the base 2 digits
# Takes O(logN) since conversion takes O(logN)


def get_matrix_power(M, n):
    if n == 1:
        return M
    result = [[1, 0], [0, 1]]  # identity matrix
    while (n > 0):
        if n % 2 == 1:
            result = multiply(result, M)
        n //= 2
        M = multiply(M, M)
    return result


def multiply(A, B):
    C = [[0 for i in range(len(A))] for j in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j] % 10000000
    return C


def solution(N):
    if N < 2:
        return N
    return get_matrix_power([[1, 1], [1, 0]], N - 1)[0][0] % 1000000


print(solution(2000000000))
