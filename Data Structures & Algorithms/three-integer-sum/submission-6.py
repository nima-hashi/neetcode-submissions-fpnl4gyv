class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        final = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = nums[i]
            l = i+1
            r = len(nums) - 1

            while l < r:

                if target + nums[l] + nums[r] < 0:
                    l += 1
                elif target + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    final.append([target, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return final

        