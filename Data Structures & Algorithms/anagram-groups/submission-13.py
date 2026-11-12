class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hm = {}

        # for s in strs:
        #     sortedS = "".join(sorted(s))
        #     if sortedS not in hm:
        #         hm[sortedS] = []
        #     hm[sortedS].append(s)
        
        # return list(hm.values())

        def getFreq(s):
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] += 1
            return tuple(count)

        hm = {}

        for s in strs:
            freq = getFreq(s) # ex. (0,2,1,0.....) len is 26
            if freq not in hm:
                hm[freq] = []
            hm[freq].append(s)
        return list(hm.values())

            
