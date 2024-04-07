class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}

        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            products = list(filter(lambda p: p.find(prefix) == 0, products))
            trie[prefix] = products

        result = []
        print(trie)
        for key in trie:
            if trie[key] is not None:
                result.append(sorted(trie[key])[:3])

        return result