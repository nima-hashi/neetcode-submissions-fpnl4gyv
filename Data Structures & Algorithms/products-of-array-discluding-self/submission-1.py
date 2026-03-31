class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        final = [1] * len(nums)

        for i in range(1,len(nums)):
            final[i] = (final[i-1]*nums[i-1])
    
        p = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            #p = final[i]
            final[i] *= p 
            p *= nums[i]
        
        return final