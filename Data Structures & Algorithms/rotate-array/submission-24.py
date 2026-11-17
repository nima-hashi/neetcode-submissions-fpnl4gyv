class Solution:

    def reverse(self, nums: List[int], l, r) -> None:

        l = l
        r = r
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        if k == 0:
            return

        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
    


        # k = k % len(nums)
        # count = 0
        # start = 0

        # while count < len(nums):
        #     current = start
        #     prev = nums[start]
        #     while True:
        #         next_idx = (current + k) % len(nums)
        #         nums[next_idx], prev = prev, nums[next_idx]
        #         current = next_idx
        #         count += 1

        #         if start == current:
        #             break
        #     start += 1

        


        # SOL 1 BUT EXTRA MEMORY
        # temp = [0] * len(nums)

        # for i in range(len(nums)):
        #     index = (i + k) % len(nums)
        #     temp[index] = nums[i]
        
        # for i in range(len(nums)):
        #     nums[i] = temp[i]

