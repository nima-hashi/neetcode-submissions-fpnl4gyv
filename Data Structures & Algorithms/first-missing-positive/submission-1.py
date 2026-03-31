class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # change nums to pos ints
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # assign present nums -> negative
        # ex [2,1,0]. since 1 exists nums[1-0] = negative val

        for i in range(len(nums)):
            if abs(nums[i]) >= 1 and abs(nums[i]) <= len(nums):
                ind = abs(nums[i]) -1
                if nums[ind] == 0:
                    nums[ind] = -nums[i]
                elif nums[ind] > 0:
                    nums[ind] = -nums[ind]

        # find firt missint postive int

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums) + 1



        

        