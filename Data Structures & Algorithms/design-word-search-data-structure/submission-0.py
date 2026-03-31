class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
        

    def dfs(self, node, word, i):
        if i == len(word):
            return node.isEndOfWord
        char = word[i]
        return self.process_char(node, char, word, i)
    
    def process_char(self, node, char, word, i):
        if char == ".":
            for child in node.children.values():
                if self.dfs(child, word, i + 1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self.dfs(node.children[char], word, i+1)
        
        
        
