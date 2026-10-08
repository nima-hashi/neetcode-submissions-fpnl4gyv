class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.wordBank(s) == self.wordBank(t)
        
    
    def wordBank(self, word):

        wordCount = {}

        for letter in word:
            wordCount[letter] = wordCount.get(letter, 0) + 1

        return wordCount
        