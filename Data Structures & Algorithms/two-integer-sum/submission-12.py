class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums.sort()
        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     if nums[i] + nums[j] == target:
        #         return [i, j]
        #     elif nums[i] + nums[j] > target:
        #         j -= 1
        #     else:
        #         i += 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]