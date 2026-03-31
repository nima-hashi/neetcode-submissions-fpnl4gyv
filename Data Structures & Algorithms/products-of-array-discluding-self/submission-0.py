class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]
        post = [1] * len(nums)
        final = [1] * len(nums)

        for i in range(1,len(nums)):
            pre.append(pre[i-1]*nums[i-1])
        
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
    

        for i in range(len(nums)):
            final[i] = pre[i] * post[i]
        
        return final