class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newS = []
        
        i = 0
        while i < len(word1):
            newS.append(word1[i])
            if i < len(word2):
                newS.append(word2[i])
            i += 1
        while i < len(word2):
            newS.append(word2[i])
            i+=1
        
        return "".join(newS)
        

        

        