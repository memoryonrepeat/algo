# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = ['N','E','S','W']
        facing_index = 0
        facing = directions[facing_index]
        current_pos = [0,0]
        for instruction in instructions:
            if instruction == 'L':
                facing_index += 1
                facing = directions[abs(facing_index)%4]
            elif instruction == 'R':
                facing_index -= 1
                facing = directions[abs(facing_index)%4]
            elif instruction == 'G':
                if facing == 'N':
                    current_pos[1] += 1
                elif facing == 'E':
                    current_pos[0] += 1
                elif facing == 'S':
                    current_pos[1] -= 1
                elif facing == 'W':
                    current_pos[0] -= 1
        return current_pos == [0,0] or facing != 'N'
        