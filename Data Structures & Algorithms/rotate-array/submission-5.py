class Solution:
    def reverseList(self, nums: List[int], l, r) -> None:
        """
        Do not return anything, reverse nums in-place instead.
        """

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverseList(nums, 0, n - 1)
        self.reverseList(nums, 0, k - 1)
        self.reverseList(nums, k, n - 1)



