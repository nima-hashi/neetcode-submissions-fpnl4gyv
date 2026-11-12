class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        l = 0
        for r in range(len(strs[0])):
            for word in strs[1:]:
                if r >= len(word) or strs[0][r] != word[r]:
                    return res
            res += strs[0][r]
        return res

        