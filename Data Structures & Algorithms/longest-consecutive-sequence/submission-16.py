class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums.sort()
        curLongest = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curLongest += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = max(res, curLongest)
                curLongest = 1
        
        return max(curLongest,res)


        