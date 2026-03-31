class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeHash(s):
            hm = {}
            for i in s:
                if i in hm:
                    hm[i] += 1
                else:
                    hm[i] = 1
            return tuple(sorted(hm.items()))

        hm = {}
        for s in strs:
            key = makeHash(s)

            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]

        return list(hm.values())