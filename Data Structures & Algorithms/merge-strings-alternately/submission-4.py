class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newString = []
        i = 0
        while i < len(word1) and i < len(word2):
            newString.append(word1[i])
            newString.append(word2[i])
            i += 1
        
        newString.append(word1[i:])
        newString.append(word2[i:])
        
        return "".join(newString)

        