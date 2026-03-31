class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newString = ""
        i = 0
        while i < len(word1) and i < len(word2):
            newString += word1[i] + word2[i]
            i += 1
        
        while i < len(word1):
            newString += word1[i:]
            break
        
        while i < len(word2):
            newString += word2[i:]
            break
        
        return newString

        