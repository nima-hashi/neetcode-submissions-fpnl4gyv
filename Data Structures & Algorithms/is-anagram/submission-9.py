class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sFreq, tFreq = {}, {}

        for letter in s:
            sFreq[letter] = sFreq.get(letter, 0) + 1
        
        for letter in t:
            tFreq[letter] = tFreq.get(letter, 0) + 1
        
        return sFreq == tFreq



        