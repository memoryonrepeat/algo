from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = Counter(s)
        _s = sorted(s, key = lambda k: c[k], reverse = True)
        keypad = {}
        total = 0
        for char in _s:
            if char not in keypad:
                if len(keypad) < 9:
                    keypad[char] = 1
                elif len(keypad) < 18:
                    keypad[char] = 2
                else:
                    keypad[char] = 3
            total += keypad[char]

        return total