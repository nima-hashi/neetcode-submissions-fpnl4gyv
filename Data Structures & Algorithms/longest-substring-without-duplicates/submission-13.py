class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in letters:
                save = letters[s[r]] + 1
                for i in range(l, save):
                    del letters[s[i]] 
                l = save
            letters[s[r]] = r
            res = max(res, r-l+1)
        return res
        