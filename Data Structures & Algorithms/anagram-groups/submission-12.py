class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in hm:
                hm[sortedS] = []
            hm[sortedS].append(s)
        
        return list(hm.values())
            
