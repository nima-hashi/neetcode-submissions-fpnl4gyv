class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        s1Perm = {}
        for letter in s1:
            s1Perm[letter] = s1Perm.get(letter, 0) + 1
        
        s2Perm = {}
        l = 0
        for r in range(len(s2)):
            if r - l >= len(s1):
                s2Perm[s2[l]] -= 1
                if s2Perm[s2[l]] == 0:
                    del s2Perm[s2[l]]
                l += 1

            s2Perm[s2[r]] = s2Perm.get(s2[r], 0) + 1
            if s1Perm == s2Perm:
                return True
        
        return False
        


        