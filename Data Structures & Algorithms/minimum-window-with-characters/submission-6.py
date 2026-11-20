class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tCount = {}
        sCount = {}

        for letter in t:
            tCount[letter] = tCount.get(letter, 0) + 1
            sCount[letter] = sCount.get(letter, 0)

        
        minLen = len(s) + 1
        matches = 0
        l = 0
        res = None
        for r in range(len(s)):
            if s[r] in sCount:
                sCount[s[r]] += 1
                if sCount[s[r]] == tCount[s[r]]:
                    matches += 1
            while matches == len(tCount):
                if (r-l+1) < minLen:
                    res = (l, r)
                    minLen = r-l+1

                if s[l] in sCount:
                    sCount[s[l]] -= 1

                    if sCount[s[l]] < tCount[s[l]]:
                        matches -= 1

                l += 1
        if res:
            return s[res[0]:res[1]+1]
        return ""


        