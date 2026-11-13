class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        curLongest = 1
        res = 1

        if len(nums) <= 1:
            return max(len(nums), 0)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curLongest += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                curLongest = 1
            res = max(res, curLongest)
        
        return res


        