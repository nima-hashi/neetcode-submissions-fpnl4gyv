class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # left = [1] * len(nums)
        # right = [1] * len(nums)

        # for i in range(1, len(left)):
        #     left[i] = left[i-1] * nums[i-1]
        
        # for j in range(len(right)-2, -1,-1):
        #     right[j] = right[j+1] * nums[j+1]
        
        # for i in range(len(nums)):
        #     nums[i] = left[i] * right[i]
        
        # return nums

        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
