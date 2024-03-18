class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        def shoot(acc, curr):
            balloon, shots = acc[0], acc[1]
            if not balloon:
                return [curr, 1]
            if curr[0] <= balloon[1]:
                return [[balloon[0], min(curr[1], balloon[1])] , shots]
            return [curr, shots+1]

        return list(reduce(shoot, points, [[], 0]))[1]