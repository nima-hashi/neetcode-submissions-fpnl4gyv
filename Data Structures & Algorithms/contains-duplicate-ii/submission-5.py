class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        i = 0
        j = 1

        for j in range(1, len(nums)):
        #while j < len(nums):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
            j += 1
            if (j-i) > k:
                i += 1
        return False
            
