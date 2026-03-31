from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if len(s2) < len(s1):
        #     return False
        
        # l = 0
        # r = len(s1) - 1

        # while r < len(s2):
        #     if Counter(s1) == Counter(s2[l:r + 1]):
        #         return True
        #     l += 1
        #     r += 1
        # return False

        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Remove char at left
            index = ord(s2[l]) - ord('a')
            if s2Count[index] == s1Count[index]:
                matches -= 1
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            l += 1

            # Add new char at right
            index = ord(s2[r]) - ord('a')
            if s2Count[index] == s1Count[index]:
                matches -= 1
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1

        return matches == 26

        