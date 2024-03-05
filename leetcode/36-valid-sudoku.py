from functools import reduce

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[(i,j) for j in range(9)] for i in range(9)]
        cols = [[(i,j) for i in range(9)] for j in range(9)]
        boxes = [[\
                (0+x,0+y),\
                (0+x,1+y),\
                (0+x,2+y),\
                (1+x,0+y),\
                (1+x,1+y),\
                (1+x,2+y),\
                (2+x,0+y),\
                (2+x,1+y),\
                (2+x,2+y),\
                ] for x in [0,3,6] for y in [0,3,6]]

        def isValidComponent(c):
            nonEmptyCells = list(filter(lambda cell: board[cell[0]][cell[1]] != ".", c))
            nonEmptyValues = list(map(lambda cell: board[cell[0]][cell[1]] , nonEmptyCells))

            return len(nonEmptyValues) == len(set(nonEmptyValues))

        return all(map(isValidComponent,rows+cols+boxes))