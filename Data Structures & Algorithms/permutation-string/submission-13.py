class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if len(s1) > len(s2):
        #     return False
        
        # # freq for s1
        # hm1 = {}
        # for char in s1:
        #     hm1[char] = hm1.get(char, 0) + 1
        
        # # freq for s2.. can only be size = len(s1)
        # hm2 = {}
        # l = r = 0

        # while r < len(s2):
        #     #expand window
        #     hm2[s2[r]] = hm2.get(s2[r], 0) + 1
        #     if r - l >= len(s1): # invalid window
        #         if hm2[s2[l]] == 1:
        #             del hm2[s2[l]]
        #         else:
        #             hm2[s2[l]] -= 1
        #         l += 1
        #     if hm2 == hm1:
        #         return True
        #     r += 1
        # return False

        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)): 
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # add right char
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s2Count[index] - 1 == s1Count[index]:
                matches -= 1
            elif s1Count[index] == s2Count[index]:
                matches += 1

            # remove left char
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s2Count[index] + 1 == s1Count[index]:
                matches -= 1
            elif s1Count[index] == s2Count[index]:
                matches += 1
            l += 1
            
        return matches == 26