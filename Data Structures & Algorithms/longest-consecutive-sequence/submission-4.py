class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        length = 0
        for num in seen:
            possibleLength = 1
            if (num - 1) not in seen: # beginning of seq
                check = num
                while check + 1 in seen:
                    possibleLength += 1
                    check += 1
                length = max(length, possibleLength)
        return length



