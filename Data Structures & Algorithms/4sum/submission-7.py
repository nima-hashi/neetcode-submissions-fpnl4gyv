class Solution:
    def kSum(self, nums, target, k, start): 

        res = []
        if k == 2:
            l = start
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
            return res
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue 
            for subSet in self.kSum(nums, target - nums[i], k-1, i + 1):
                res.append([nums[i]] + subSet)
        return res


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4, 0)
