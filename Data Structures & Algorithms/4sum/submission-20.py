class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        l = 0
        r = len(nums) - 1

        while l < r:
            totalSum = nums[l] + nums[r]
            if totalSum > target:
                r -= 1
            elif totalSum < target:
                l += 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []
        curSum = []

        def kSum(k, start, target):
            if k == 2:
                pairs  = self.twoSum(nums[start:], target)
                for pair in pairs:
                    res.append(curSum + pair)
                return
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curSum.append(nums[i])
                kSum(k-1, i + 1, target - nums[i])
                curSum.pop()
        
        kSum(4, 0, target)
        return res




        