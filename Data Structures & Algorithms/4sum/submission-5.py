class Solution:
    def kSum(self, nums, target, start, k):

        res = []

        # base case
        if k == 2:
            l = start
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            return res
        
        for i in range(start, len(nums)):
            if i > start and (nums[i] == nums[i - 1]):
                continue
            possibleSet = self.kSum(nums, target - nums[i], i + 1, k -1)
            for subSet in possibleSet:
                res.append([nums[i]] + subSet)
        return res
                    


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        return self.kSum(nums, target, 0, 4)
        