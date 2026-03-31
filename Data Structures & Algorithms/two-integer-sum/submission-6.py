class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # use hashmap

        hm = {}

        for i, n in enumerate(nums):
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i






