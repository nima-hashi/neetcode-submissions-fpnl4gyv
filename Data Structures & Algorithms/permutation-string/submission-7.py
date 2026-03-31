class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        hm1, hm2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            hm1[ord(s1[i]) - ord('a')] += 1
            hm2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if hm1[i] == hm2[i]:
                matches += 1
        
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            hm2[ord(s2[i]) - ord('a')] += 1
            if hm2[ord(s2[i]) - ord('a')] ==  hm1[ord(s2[i]) - ord('a')]:
                matches += 1
            elif hm2[ord(s2[i]) - ord('a')] ==  hm1[ord(s2[i]) - ord('a')] + 1:
                matches -= 1
            
            hm2[ord(s2[l]) - ord('a')] -= 1
            if hm2[ord(s2[l]) - ord('a')] ==  hm1[ord(s2[l]) - ord('a')]:
                matches += 1
            elif hm2[ord(s2[l]) - ord('a')] ==  hm1[ord(s2[l]) - ord('a')] - 1:
                matches -= 1
            l += 1
        return matches == 26

            
            



        