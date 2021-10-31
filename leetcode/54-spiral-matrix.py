# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, top, bottom = 0, cols-1, 0, rows-1
        direction = 0
        result = []
        x,y = 0,0
        while len(result) < rows*cols:
            result.append(matrix[x][y])
            if direction%4 == 0:
                if y+1 <= right:
                    y += 1
                else:
                    right -= 1
                    x += 1
                    direction += 1
            elif direction%4 == 1:
                if x+1 <= bottom:
                    x += 1
                else:
                    bottom -= 1
                    y -= 1
                    direction += 1
            elif direction%4 == 2:
                if y-1 >= left:
                    y -= 1
                else:
                    left += 1
                    x -= 1
                    direction += 1
            else:
                if x-1 > top:
                    x -= 1
                else:
                    top += 1
                    y += 1
                    direction += 1
        return result
                    
                    
                    
                    
                    
                    
                    
        