class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # upper bound

        l = 0
        r = len(nums)
        while l < r:
            m = l + ((r-l)//2)
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        if l > 0 and nums[l-1] == target:
            return l - 1
        return -1


        # def bs(l, r):
        #     if l > r:
        #         return - 1

        #     m = l + ((r-l) // 2)
        #     if nums[m] == target:
        #         return m
        #     if nums[m] > target:
        #         return bs(l,m-1)
        #     if nums[m] < target:
        #         return bs(m+1, r)
        
        # return bs(0, len(nums)-1)



        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     m = l + ((r-l)//2)
        #     if nums[m] == target:
        #         return m
        #     if nums[m] > target:
        #         r = m - 1
        #     else:
        #         l = m + 1
        # return - 1  