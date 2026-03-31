class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final = defaultdict(list)
        for s in strs:
            hashM = [0] * 26 #a...z

            for c in s:
                hashM[ord(c) - ord("a")] += 1
            
            final[tuple(hashM)].append(s)

        return final.values()
