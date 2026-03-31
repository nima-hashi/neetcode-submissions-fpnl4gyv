class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        length = 0
        for num in seen:
            possibleLength = 0
            check = num
            while check - 1 in seen:
                possibleLength += 1
                check -= 1
            length = max(length, possibleLength + 1)
        return length
