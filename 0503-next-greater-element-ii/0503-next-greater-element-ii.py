class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        res = [-1] * len(nums)

        for i in range(2 * len(nums)):

            index = i % len(nums)
            num = nums[index]

            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                res[j] = num
        
            if i < len(nums):
                stack.append(index)
        
        return res
        

        