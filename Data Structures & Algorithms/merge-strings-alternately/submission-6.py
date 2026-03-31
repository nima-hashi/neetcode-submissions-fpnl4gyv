class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newWord = []
        i, j = 0, 0

        while (i < len(word1)) and (j < len(word2)):
                    newWord.append(word1[i])
                    newWord.append(word2[j])
                    i += 1
                    j += 1

        newWord.append(word1[i:])
        newWord.append(word2[j:])

        # while (i < len(word1)):
        #     newWord.append(word1[i])
        #     i += 1

        # while (j < len(word2)):
        #     newWord.append(word2[j])
        #     j += 1

        
        return "".join(newWord)

