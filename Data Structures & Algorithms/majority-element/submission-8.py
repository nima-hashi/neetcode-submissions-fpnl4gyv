class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        x = len(nums) // 2  # majority > x
        # memory used
        # hm = {}
        # for num in nums:
        #     hm[num] = hm.get(num, 0) + 1
        #     if hm[num] > x:
        #         return num

        cur = None
        count = 0

        for i in range(len(nums)):
            if count == 0:
                count += 1
                cur = nums[i]
            elif nums[i] == cur:
                count += 1
            else:
                count -= 1
        return cur
        