class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        print(nums)

        for i in range(len(nums)):
            val = abs(nums[i])
            if 0 < val < len(nums) + 1:
                if nums[val-1] == 0:
                    nums[val-1] = -nums[i]
                else:
                    if nums[val-1] > 0:
                        nums[val-1] = -nums[val-1]
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1
            

        