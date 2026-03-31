class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(mid):
            c = 0
            splits = 1
            for n in nums:
                if (c+n) > mid:
                    splits += 1
                    c = n
                else:
                    c += n
            return splits <= k

        l = max(nums)
        r = sum(nums)

        res = r

        while l <= r:
            mid = (l+r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        


        