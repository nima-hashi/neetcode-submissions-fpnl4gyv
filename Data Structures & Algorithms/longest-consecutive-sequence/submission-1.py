class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        res = 0

        for n in nums:
            if n-1 in nums:
                continue
            i = n
            cur = 0
            while i in nums:
                cur +=1 
                i += 1
            if cur > res:
                res = cur
        return res
            
        