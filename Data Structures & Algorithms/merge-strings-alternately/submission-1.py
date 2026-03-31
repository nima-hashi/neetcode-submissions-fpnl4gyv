class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newS = []
        
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            newS.append(word1[i])
            newS.append(word2[j])
            i += 1
            j += 1

        newS.extend(word1[i:])
        newS.extend(word2[j:])
        
        return "".join(newS)
        

        

        