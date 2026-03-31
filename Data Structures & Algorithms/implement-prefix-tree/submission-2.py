class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        if node and node.isEndOfWord:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None

    def searchPrefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


        
        