# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution:
    # Solve using equation
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return []
        beta = 2 * cheeseSlices - tomatoSlices / 2
        alpha = tomatoSlices / 2 - cheeseSlices
        if beta < 0 or alpha < 0:
            return []
        return [int(alpha), int(beta)]