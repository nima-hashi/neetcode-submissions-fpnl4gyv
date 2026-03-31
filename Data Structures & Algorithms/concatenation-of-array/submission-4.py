class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #return nums * 2
        
        # ans = [0] * len(nums) * 2

        # for i in range(len(nums)):
        #     ans[i] = nums[i]
        #     ans[i + len(nums)] = nums[i]
        # return ans

        ans = []

        for j in range(2): # can change to 2n.. 4n.. 5n etc easily
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans
        