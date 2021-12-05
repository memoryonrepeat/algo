class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat2flip = [[mat2[j][i] for j in range(len(mat2)) ] for i in range(len(mat2[0]))]
        r = 0
        c = 0
        result = [[None for j in range(len(mat2flip))] for i in range(len(mat1))]
        for r1 in mat1:
            for r2 in mat2flip:
                result[r][c] = sum([a*b for (a,b) in zip(r1,r2)])
                c += 1
            r += 1
            c = 0
        return result