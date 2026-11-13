class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

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


        missing = 1
        while True:
            notFound = True
            for num in nums:
                if num == missing:
                    notFound = False

            if notFound:
                return missing
            missing += 1
        