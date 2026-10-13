class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSeq = 0
        s = set(nums)
        for num in nums:
            possibleLongest = 0
            if num + 1 not in s:
                n = num
                while n in s:
                    possibleLongest += 1
                    n -= 1
                
                longestSeq = max(longestSeq, possibleLongest)
        return longestSeq

                


        