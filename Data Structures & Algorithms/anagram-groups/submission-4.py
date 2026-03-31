from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # {act: [act, cat], opst: [stop, pots], ....}
        hm = defaultdict(list)

        for s in strs:
            hm[tuple(sorted(s))].append(s)
        
        return hm.values()
            
        
       