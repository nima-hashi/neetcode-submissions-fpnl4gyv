class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i] # swaps val with wanted vals
                #nums[k] = nums[k], nums[i] # either works. this completely igores nums we dont need
                k += 1
        return k

        