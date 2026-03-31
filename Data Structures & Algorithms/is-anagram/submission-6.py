class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hm = {}

        for char in s:
            hm[char] = hm.get(char, 0) + 1
        
        for char in t:
            hm[char] = hm.get(char, 0) - 1
            if hm[char] == -1:
                return False
        
        return max(hm.values()) == 0
        

        