class Solution:
    def twoSum(self, nums, l, r, target):
        res = []
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([-target, nums[l], nums[r]])
                l += 1
                r -= 1

                # skip duplicates
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []

        l, r = 0, len(nums) -1

        while l < len(nums):
            if (l > 0) and (nums[l-1] == nums[l]):
                l += 1
            else:
                possible = self.twoSum(nums, l+1, r, -nums[l])
                if possible:
                    triplets.extend(possible)
                l += 1
        return triplets
            
        