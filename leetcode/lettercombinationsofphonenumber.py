# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        mapping = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        for digit in digits:
            if len(result) == 0:
                result = mapping[digit]
            else:
                result = [x+y for x in result for y in mapping[digit]]
        return result
        