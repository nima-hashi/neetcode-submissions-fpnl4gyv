from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1

        k = 0
        for colour in range(len(hm)):
            repeats = hm[colour]
            for i in range(repeats):
                nums[k] = colour
                k += 1

        