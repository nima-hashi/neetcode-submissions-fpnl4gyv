from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {} # k: "" v: []

        for word in strs:
            c = "".join(sorted(word))
            #"act"
            #"opst"
            #"opst"
            #....
             
            if c in hm:
                hm[c].append(word)
            else:
                hm[c] = [word]
        
        return list(hm.values())

        