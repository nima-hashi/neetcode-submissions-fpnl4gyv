class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # write = 0
        # for read in range(len(nums)):
        #     if nums[read] != val:
        #         nums[write] = nums[read]
        #         write += 1
        # return write

        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n
    
