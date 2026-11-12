class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}

        for s in strs:
            if tuple(sorted(s)) not in hm:
                hm[tuple(sorted(s))] = []
            hm[tuple(sorted(s))].append(s)
        
        return list(hm.values())
            
