class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            if 0 < abs(nums[i]) <= len(nums):
                val = abs(nums[i]) - 1
                if nums[val] > 0: 
                    nums[val] = -nums[val]
                elif nums[val] == 0: 
                    nums[val] = -len(nums)

        
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        return len(nums) + 1



        

        
        