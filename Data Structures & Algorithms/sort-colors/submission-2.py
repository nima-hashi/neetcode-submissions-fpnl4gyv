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
        for i in range(len(hm)):
            repeats = hm[i]
            c = 0 
            while c < repeats:
                nums[k] = i
                k += 1
                c += 1

        