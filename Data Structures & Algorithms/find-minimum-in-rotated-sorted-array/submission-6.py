class Solution:
    def findMin(self, nums: List[int]) -> int:
        [3,4,5,6,1,2]
        def greater(mid, r):
            if nums[mid] > nums[r]:
                return True
            return False

        l = 0
        r = len(nums) - 1
        curMin = float("inf")

        while l <= r:
            mid = (l + r) // 2
            curMin = min(curMin, nums[mid])
            if greater(mid, r): # 6 > l[0]
                curMin = min(curMin, nums[l])
                l = mid + 1
            else:
                r = mid - 1
        return curMin


        