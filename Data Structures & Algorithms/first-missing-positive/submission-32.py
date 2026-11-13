class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #sol4
        nums.sort()
        missing = 1
        for num in nums:
            if num == missing:
                missing += 1
        return missing

        #sol1 
        # contains = [False] * len(nums)

        # for num in nums:
        #     if 0 < num <= len(nums):
        #         contains[num-1] = True
        
        # for i in range(len(contains)):
        #     if not contains[i]:
        #         return i+1
        # return len(nums) + 1
        
        #sol2
        # n = len(nums)

        # for i in range(n):
        #     if nums[i] < 0:
        #         nums[i] = 0
        
        # for i in range(n):
        #     val = abs(nums[i])

        #     if 0 < val <= n:
        #         if nums[val-1] == 0:
        #             nums[val-1] = (-1 * n)
        #         elif nums[val-1] > 0:
        #             nums[val-1] *= -1
        
        # for i in range(n):
        #     if nums[i] < 0:
        #         return i + 1
        
        # return n + 1

        #sol3
        # missing = 1
        # while True:
        #     notFound = True
        #     for num in nums:
        #         if num == missing:
        #             notFound = False

        #     if notFound:
        #         return missing
        #     missing += 1
    