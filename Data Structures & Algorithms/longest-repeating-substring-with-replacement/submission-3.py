class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charFreq = {}
        maxLen = 0

        l = 0
        r = 0

        while r < len(s):
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1
            max_val = max(charFreq.values())
            if r - l + 1 - max_val > k:
                charFreq[s[l]] = charFreq[s[l]] - 1
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen






        
