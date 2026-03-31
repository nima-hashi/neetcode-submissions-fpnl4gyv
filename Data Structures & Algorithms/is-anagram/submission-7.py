class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1, hm2 = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hm1[s[i]] = hm1.get(s[i], 0) + 1
            hm2[t[i]] = hm2.get(t[i], 0) + 1

        return hm1 == hm2
        