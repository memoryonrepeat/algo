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
            seen = set()
            for x,y in c:
                if board[x][y] != ".":
                    if board[x][y] not in seen:
                        seen.add(board[x][y])
                    else:
                        return False
            return True

        return all([isValidComponent(row) for row in rows]) and all([isValidComponent(col) for col in cols]) and all([isValidComponent(box) for box in boxes])