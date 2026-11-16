class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        res = []

        while l < r:
            curSum = nums[l] + nums[r]

            if curSum > target:
                r -= 1

            elif curSum < target:
                l += 1

            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            tS = self.twoSum(nums[i+1:], -nums[i])

            for pair in tS:
                res.append([nums[i]] + pair)

        return res