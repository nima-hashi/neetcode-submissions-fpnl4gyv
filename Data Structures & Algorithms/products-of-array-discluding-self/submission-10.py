class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        preFix = [1] * len(nums)
        postFix = [1] * len(nums)

        for i in range(1, len(nums)):
            preFix[i] = preFix[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            postFix[i] = postFix[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(preFix[i] * postFix[i])

        return res