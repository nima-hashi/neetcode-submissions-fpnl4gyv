from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # m * nlogn
        # hm = {} # k: "" v: []

        # for word in strs:
        #     c = "".join(sorted(word))
        #     #"act"
        #     #"opst"
        #     #"opst"
        #     #....
             
        #     if c in hm:
        #         hm[c].append(word)
        #     else:
        #         hm[c] = [word]
        
        # return list(hm.values())

        # o(n*m)
        #[0:, 1:, 2:... 26]
        hm = {}
        for word in strs:
            k = [0] * 26
            for letter in word:
                i = ord(letter) - ord("a")
                k[i] += 1
            if tuple(k) in hm:
                hm[tuple(k)].append(word)
            else:
                hm[tuple(k)] = [word]
        return list(hm.values()) 


        