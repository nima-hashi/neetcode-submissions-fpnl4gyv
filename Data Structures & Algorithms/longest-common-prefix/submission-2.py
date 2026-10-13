class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        count = 0
        length = len(strs[0])

        i = 0
        while i < length:
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:count]
            i += 1
            count += 1
        return strs[0][:count]