from collections import defaultdict

class FreqStack:
    
    def __init__(self):
        self.stack = []
        self.frequencies = defaultdict(int)

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.frequencies[x] += 1

    def pop(self) -> int:
        topFrequency = max(self.frequencies.values())
        
        # print(self.stack, topFrequency)
        
        for i in range(len(self.stack)-1, -1, -1):
            if self.frequencies[self.stack[i]] == topFrequency:
                result = self.stack[i]
                self.frequencies[result] -= 1
                self.stack.pop(i)
                return result

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()