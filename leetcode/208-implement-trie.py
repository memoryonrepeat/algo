# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.child = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.child:
                current.child[char] = TrieNode(char)
            current = current.child[char]
        current.child['end'] = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.child:
                return False
            current = current.child[char]
        if 'end' in current.child:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.child:
                return False
            current = current.child[char]
        return True

# Alternative solution, no need TrieNode class
class __Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['end'] = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if 'end' in current:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)