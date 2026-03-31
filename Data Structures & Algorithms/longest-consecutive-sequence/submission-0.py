class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Input: nums = [2,20,4,10,3,4,5]
        # [2,3,4,4,5,10,20]

        s = set(nums)
        longest = 0

        for num in nums:
            curr_longest = 0
            if num-1 not in s:
                curr_longest = 1
                while num+1 in s:
                    curr_longest += 1
                    num += 1
                longest = max(longest, curr_longest)
        
        return longest
