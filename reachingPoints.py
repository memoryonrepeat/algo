# https://leetcode.com/problems/reaching-points/submissions/

class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                elif ty == sy:
                    return (tx - sx) % sy == 0
            else:
                if tx > sx:
                    ty %= tx
                elif tx == sx:
                    return (ty - sy) % sx == 0
        return tx == sx and ty == sy