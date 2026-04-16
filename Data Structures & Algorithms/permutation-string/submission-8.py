class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # freq for s1
        hm1 = {}
        for char in s1:
            hm1[char] = hm1.get(char, 0) + 1
        
        # freq for s2.. can only be size = len(s1)
        hm2 = {}
        l = r = 0

        while r < len(s2):
            if r - l >= len(s1):
                if hm2[s2[l]] == 1:
                    del hm2[s2[l]]
                else:
                    hm2[s2[l]] -= 1
                l += 1
            else:
                hm2[s2[r]] = hm2.get(s2[r], 0) + 1
                r += 1
                if hm2 == hm1:
                    return True
        return False


        