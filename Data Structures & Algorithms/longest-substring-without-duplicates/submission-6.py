class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        letters = {}
        
        for r in range(len(s)):
            if s[r] in letters:
                l = max(l, letters[s[r]] + 1)
            res = max(res, r-l+1)
            letters[s[r]] = r
                
        return res
            

            