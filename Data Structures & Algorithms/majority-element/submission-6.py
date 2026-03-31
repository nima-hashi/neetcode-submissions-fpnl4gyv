class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        x = len(nums) // 2  # majority > x

        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
            if hm[num] > x:
                return num
        