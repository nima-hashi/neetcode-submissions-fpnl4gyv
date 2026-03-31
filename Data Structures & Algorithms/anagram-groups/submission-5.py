from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # {act: [act, cat], opst: [stop, pots], ....}
        hm = defaultdict(list)

        for s in strs:
            #hm[tuple(sorted(s))].append(s)

            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] += 1

            hm[tuple(count)].append(s)
        
        return hm.values()
            
        
       