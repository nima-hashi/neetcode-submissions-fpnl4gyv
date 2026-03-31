class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # def getHashMap(s):
        #     hm = {}
        #     for ch in s:
        #         hm[ch] = hm.get(ch, 0) + 1
        #     return hm

        # anagrams = {}
        # for s in strs:
        #     hm = tuple(sorted(getHashMap(s).items())) # {a:1, c:1, t:1}
        #     if hm not in anagrams:
        #         anagrams[hm] = [s]
        #     else:
        #         anagrams[hm].append(s)
        
        # return list(anagrams.values())

        res = {}
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            res[tuple(count)] = res.get(tuple(count), []) + [s]
        return list(res.values())
            



            
        